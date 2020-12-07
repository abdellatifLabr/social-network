import graphene
from graphql_jwt.decorators import login_required
from graphql_auth.types import ExpectedErrorType

from ..models import Follow
from .nodes import FollowNode


class CreateFollowMutation(graphene.relay.ClientIDMutation):
    class Input:
        followed_id = graphene.ID(required=True)

    follow = graphene.Field(FollowNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, followed_id, **kwargs):
        user = info.context.user

        follow = Follow.objects.create(follower=user, followed_id=followed_id)
        return CreateFollowMutation(success=True, follow=follow)


class DeleteFollowMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            follow = Follow.objects.get(pk=id)
        except Follow.DoesNotExist:
            errors = {
                'follow': [
                    {
                        'message': 'This follow does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return DeleteFollowMutation(success=False, errors=errors)

        if follow.follower != user:
            raise PermissionError('You do not have the permission to perform this action')

        follow.delete()
        return DeleteFollowMutation(success=True)
