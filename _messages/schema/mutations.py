import graphene
from graphql_jwt.decorators import login_required
from graphql_auth.types import ExpectedErrorType
from graphene_file_upload.scalars import Upload
from django.core.exceptions import ValidationError

from ..models import Message
from .nodes import MessageNode


class CreateMessageMutation(graphene.relay.ClientIDMutation):
    class Input:
        receiver_id = graphene.ID(required=True)
        message = graphene.String(required=True)

    message = graphene.Field(MessageNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, **kwargs):
        user = info.context.user

        message = Message(sender=user, **kwargs)

        try:
            message.full_clean()
        except ValidationError as e:
            return CreateMessageMutation(success=False, errors=e.message_dict)

        message.save()
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

        if message.sender != user:
            raise PermissionError('You do not have the permission to perform this action')

        message.delete()
        return DeleteMessageMutation(success=True)
