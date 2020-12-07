import graphene

from .queries import (
    PostQuery,
    LikeQuery,
    CommentQuery
)
from .mutations import (
    CreatePostMutation,
    UpdatePostMutation,
    DeletePostMutation,

    CreateLikeMutation,
    DeleteLikeMutation,

    CreateCommentMutation,
    UpdateCommentMutation,
    DeleteCommentMutation,
)


class Query(
    PostQuery,
    LikeQuery,
    CommentQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_post = CreatePostMutation.Field()
    update_post = UpdatePostMutation.Field()
    delete_post = DeletePostMutation.Field()

    create_like = CreateLikeMutation.Field()
    delete_like = DeleteLikeMutation.Field()

    create_comment = CreateCommentMutation.Field()
    update_comment = UpdateCommentMutation.Field()
    delete_comment = DeleteCommentMutation.Field()
