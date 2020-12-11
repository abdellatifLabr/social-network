import graphene
import channels_graphql_ws
from graphql_jwt.shortcuts import get_user_by_token
from graphql_auth.types import ExpectedErrorType

from ..models import Discussion
from .nodes import MessageNode


class DiscussionSubscription(channels_graphql_ws.Subscription):
    class Arguments:
        token = graphene.String(required=True)
        discussion_id = graphene.ID(required=True)

    message = graphene.Field(MessageNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @staticmethod
    def subscribe(root, info, token, discussion_id, **kwargs):
        user = get_user_by_token(token)

        if user is None:
            raise PermissionError('You do not have the permission to perform this action')

        try:
            discussion = Discussion.objects.get(pk=discussion_id)
        except Discussion.DoesNotExist:
            return 'This discussion does not exist'

        if discussion.sender != user and discussion.receiver != user:
            raise PermissionError('You do not have the permission to perform this action')

        group_name = f'discussion@{discussion.id}'
        return [group_name]

    @staticmethod
    def publish(payload, info, **kwargs):
        return DiscussionSubscription(success=True, message=payload)
