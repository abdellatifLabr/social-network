import graphene
from graphql_jwt.decorators import login_required
from graphql_auth.types import ExpectedErrorType
from graphene_file_upload.scalars import Upload
from django.core.exceptions import ValidationError

from ..models import Message, Discussion
from .nodes import MessageNode, DiscussionNode
from .subscriptions import DiscussionSubscription


class CreateDiscussionMutation(graphene.relay.ClientIDMutation):
    class Input:
        receiver_id = graphene.ID(required=True)

    discussion = graphene.Field(DiscussionNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, receiver_id, **kwargs):
        user = info.context.user

        discussion = Discussion(sender=user, receiver_id=receiver_id, **kwargs)

        try:
            discussion.full_clean()
        except ValidationError as e:
            return CreateDiscussionMutation(success=False, errors=e.message_dict)

        discussion.save()
        return CreateDiscussionMutation(success=True, discussion=discussion)


class CreateMessageMutation(graphene.relay.ClientIDMutation):
    class Input:
        discussion_id = graphene.ID(required=True)
        message = graphene.String(required=True)

    message = graphene.Field(MessageNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, discussion_id, **kwargs):
        user = info.context.user

        try:
            discussion = Discussion.objects.get(pk=discussion_id)
        except Discussion.DoesNotExist:
            errors = {
                'discussion': [
                    {
                        'message': 'This discussion does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return CreateMessageMutation(success=False, errors=errors)

        if discussion.sender != user and discussion.receiver != user:
            raise PermissionError('You do not have the permission to perform this action')

        message = Message(user=user, discussion=discussion, **kwargs)

        try:
            message.full_clean()
        except ValidationError as e:
            return CreateMessageMutation(success=False, errors=e.message_dict)

        message.save()

        group_name = f'discussion@{message.discussion.id}'
        DiscussionSubscription.broadcast(
            group=group_name,
            payload=message
        )

        return CreateMessageMutation(success=True, message=message)


class DeleteMessageMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            message = Message.objects.get(pk=id)
        except Message.DoesNotExist:
            errors = {
                'message': [
                    {
                        'message': 'This message does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return DeleteMessageMutation(success=False, errors=errors)

        if message.user != user:
            raise PermissionError('You do not have the permission to perform this action')

        message.delete()
        return DeleteMessageMutation(success=True)
