import graphene

import users.schema
import follows.schema
import posts.schema


class Query(
    users.schema.Query,
    follows.schema.Query,
    posts.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    follows.schema.Mutation,
    posts.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
