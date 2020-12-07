import graphene

from .queries import FollowQuery
from .mutations import CreateFollowMutation, DeleteFollowMutation


class Query(
    FollowQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_follow = CreateFollowMutation.Field()
    delete_follow = DeleteFollowMutation.Field()
