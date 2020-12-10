import graphene

import users.schema
import follows.schema
import posts.schema
import _messages.schema
import notifications.schema


class Query(
    users.schema.Query,
    follows.schema.Query,
    posts.schema.Query,
    _messages.schema.Query,
    notifications.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    follows.schema.Mutation,
    posts.schema.Mutation,
    _messages.schema.Mutation,
    notifications.schema.Mutation,
    graphene.ObjectType
):
    pass


class Subscription(
    notifications.schema.Subscription,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
