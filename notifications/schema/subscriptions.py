import graphene
import channels_graphql_ws
from graphql_jwt.shortcuts import get_user_by_token

from .nodes import NotificationNode


class NotificationSubscription(channels_graphql_ws.Subscription):
    class Arguments:
        token = graphene.String(required=True)

    notification = graphene.Field(NotificationNode)

    @staticmethod
    def subscribe(root, info, token, **kwargs):
        user = get_user_by_token(token)

        if user is None:
            raise PermissionError('You do not have the permission to perform this action')

        group_name = f'notifications@{user.username}'
        return [group_name]

    @staticmethod
    def publish(payload, info, **kwargs):
        return NotificationSubscription(notification=payload)
