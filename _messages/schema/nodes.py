import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode

from ..models import Message


class MessageNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    sender = graphene.Field(UserNode)
    receiver = graphene.Field(UserNode)

    def resolve_sender(self, info, **kwargs):
        return self.sender

    def resolve_receiver(self, info, **kwargs):
        return self.receiver

    class Meta:
        model = Message
        filter_fields = {
            'id': ['exact'],
            'sender__id': ['exact'],
            'receiver__id': ['exact']
        }
        interfaces = (graphene.relay.Node,)
