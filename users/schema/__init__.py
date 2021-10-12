import graphene
from graphql_auth.schema import MeQuery, UserQuery
from graphql_auth import mutations as graphql_auth_mutations

from .queries import IUserQuery

from .mutations import (
    UpdateUserMutation,
)


class Query(
    MeQuery,
    # UserQuery,
    IUserQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    register = graphql_auth_mutations.Register.Field()
    verify_account = graphql_auth_mutations.VerifyAccount.Field()
    resend_activation_email = graphql_auth_mutations.ResendActivationEmail.Field()
    send_password_reset_email = graphql_auth_mutations.SendPasswordResetEmail.Field()
    password_reset = graphql_auth_mutations.PasswordReset.Field()
    password_change = graphql_auth_mutations.PasswordChange.Field()
    delete_account = graphql_auth_mutations.DeleteAccount.Field()

    # django-graphql-jwt
    token_auth = graphql_auth_mutations.ObtainJSONWebToken.Field()
    verify_token = graphql_auth_mutations.VerifyToken.Field()
    refresh_token = graphql_auth_mutations.RefreshToken.Field()
    revoke_token = graphql_auth_mutations.RevokeToken.Field()

    update_user = UpdateUserMutation.Field()
