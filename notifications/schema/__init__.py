import graphene

from .queries import NotificationQuery
from .mutations import (
    CreateNotificationMutation,
    UpdateNotificationMutation,
    DeleteNotificationMutation,
)
from .subscriptions import NotificationSubscription


class Query(
    NotificationQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_notification = CreateNotificationMutation.Field()
    update_notification = UpdateNotificationMutation.Field()
    delete_notification = DeleteNotificationMutation.Field()


class Subscription(graphene.ObjectType):
    notification_subscription = NotificationSubscription.Field()
