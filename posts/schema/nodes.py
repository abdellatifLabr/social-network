import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode

from shared.connections import CountableConnection
from ..models import Post, Like, Comment, Rating, Section
from ..filters import PostFilterSet


class PostNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    created_since = graphene.String(source='created_since')
    rating = graphene.Float(source='rating')
    image_url = graphene.String()
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    def resolve_image_url(self, info, **kwargs):
        if self.image:
            return info.context.build_absolute_uri(self.image.url)

    class Meta:
        model = Post
        filterset_class = PostFilterSet
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)


class SectionNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    file_url = graphene.String()

    def resolve_file_url(self, info, **kwargs):
        if self.file:
            return info.context.build_absolute_uri(self.file.url)

    class Meta:
        model = Section
        filter_fields = {
            'id': ['exact'],
            'post__id': ['exact'],
        }
        connection_class = CountableConnection
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
        connection_class = CountableConnection
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
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)


class RatingNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Rating
        filter_fields = {
            'id': ['exact'],
            'value': ['exact'],
        }
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)
