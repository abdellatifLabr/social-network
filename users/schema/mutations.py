import graphene
from graphql_auth.types import ExpectedErrorType
from graphql_jwt.decorators import login_required
from graphql_auth.schema import UserNode
from graphene_file_upload.scalars import Upload
from django.core.exceptions import ValidationError

from ..forms import UpdateUserForm


class UpdateUserMutation(graphene.relay.ClientIDMutation):
    class Input:
        email = graphene.String()
        username = graphene.String()
        full_name = graphene.String()
        image = Upload()
        cover = Upload()
        is_online = graphene.Boolean()

    user = graphene.Field(UserNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, *args, **kwargs):
        user = info.context.user
        update_user_form = UpdateUserForm(kwargs)

        if not update_user_form.is_valid():
            return UpdateUserMutation(success=False, errors=update_user_form.errors.get_json_data())

        for field, value in kwargs.items():
            setattr(user, field, value)

        try:
            user.full_clean()
        except ValidationError as e:
            return UpdateUserMutation(success=False, errors=e.message_dict)

        user.save()
        return UpdateUserMutation(success=True, user=user)
