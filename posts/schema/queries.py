import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from ..models import Post, Like, Comment
from .nodes import PostNode, LikeNode, CommentNode


class PostQuery(graphene.ObjectType):
    post = graphene.relay.Node.Field(PostNode)
    posts = DjangoFilterConnectionField(PostNode)
    my_posts = DjangoFilterConnectionField(PostNode)

    @login_required
    def resolve_my_posts(self, info, **kwargs):
        user = info.context.user
        return Post.objects.filter(user=user)


class LikeQuery(graphene.ObjectType):
    like = graphene.relay.Node.Field(LikeNode)
    likes = DjangoFilterConnectionField(LikeNode)


class CommentQuery(graphene.ObjectType):
    comment = graphene.relay.Node.Field(CommentNode)
    comments = DjangoFilterConnectionField(CommentNode)
