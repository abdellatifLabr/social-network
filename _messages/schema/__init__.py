import graphene

from .queries import MessageQuery

from .mutations import (
    CreateMessageMutation,
    DeleteMessageMutation,
)


class Query(
    MessageQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_message = CreateMessageMutation.Field()
    delete_message = DeleteMessageMutation.Field()
