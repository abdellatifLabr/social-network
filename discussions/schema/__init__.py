import graphene

from .queries import MessageQuery, DiscussionQuery
from .mutations import (
    CreateDiscussionMutation,

    CreateMessageMutation,
    DeleteMessageMutation,
)
from .subscriptions import DiscussionSubscription


class Query(
    DiscussionQuery,
    MessageQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_discussion = CreateDiscussionMutation.Field()

    create_message = CreateMessageMutation.Field()
    delete_message = DeleteMessageMutation.Field()


class Subscription(graphene.ObjectType):
    discussion = DiscussionSubscription.Field()
