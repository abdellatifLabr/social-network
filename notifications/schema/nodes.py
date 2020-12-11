import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode

from shared.connections import CountableConnection
from ..models import Notification


class NotificationNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    author = graphene.Field(UserNode)

    def resolve_author(self, info, **kwargs):
        return self.author

    class Meta:
        model = Notification
        filter_fields = {
            'id': ['exact']
        }
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)
