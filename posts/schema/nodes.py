import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode

from ..models import Post, Like, Comment


class PostNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Post
        filter_fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
            'body': ['exact', 'icontains']
        }
        interfaces = (graphene.relay.Node,)


class LikeNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Like
        filter_fields = {
            'id': ['exact'],
            'user__id': ['exact'],
            'post__id': ['exact']
        }
        interfaces = (graphene.relay.Node,)


class CommentNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Comment
        filter_fields = {
            'id': ['exact'],
            'user__id': ['exact'],
            'post__id': ['exact']
        }
        interfaces = (graphene.relay.Node,)
