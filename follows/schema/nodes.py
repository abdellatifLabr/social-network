import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode
from graphql_jwt.decorators import login_required

from ..models import Follow


class FollowNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    follower = graphene.Field(UserNode)
    followed = graphene.Field(UserNode)

    def resolve_follower(self, info, **kwargs):
        return self.follower

    def resolve_followed(self, info, **kwargs):
        return self.followed

    class Meta:
        model = Follow
        filter_fields = {
            'id': ['exact'],
            'follower__id': ['exact'],
            'follower__full_name': ['exact', 'icontains'],
            'followed__id': ['exact'],
            'followed__full_name': ['exact', 'icontains']
        }
        interfaces = (graphene.relay.Node,)

    @classmethod
    @login_required
    def get_node(cls, info, id, **kwargs):
        user = info.context.user
        follow = Follow.objects.get(pk=id)

        if follow.follower != user or follow.followed != user:
            return None

        return follow
