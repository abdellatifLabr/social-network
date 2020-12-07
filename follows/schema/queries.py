import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from ..models import Follow
from .nodes import FollowNode


class FollowQuery(graphene.ObjectType):
    follow = graphene.relay.Node.Field(FollowNode)
    follows = DjangoFilterConnectionField(FollowNode)

    @login_required
    def resolve_follows(self, info, **kwargs):
        user = info.context.user

        return Follow.objects.filter(follower=user)
