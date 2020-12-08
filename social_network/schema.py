import graphene

import users.schema
import follows.schema
import posts.schema
import _messages.schema


class Query(
    users.schema.Query,
    follows.schema.Query,
    posts.schema.Query,
    _messages.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    follows.schema.Mutation,
    posts.schema.Mutation,
    _messages.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
