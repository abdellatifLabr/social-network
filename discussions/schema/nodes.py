import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode

from shared.connections import CountableConnection
from ..models import Message, Discussion


class DiscussionNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    sender = graphene.Field(UserNode)
    receiver = graphene.Field(UserNode)

    def resolve_sender(self, info, **kwargs):
        return self.sender

    def resolve_receiver(self, info, **kwargs):
        return self.receiver

    class Meta:
        model = Discussion
        filter_fields = {
            'id': ['exact'],
            'sender__id': ['exact'],
            'receiver__id': ['exact'],
        }
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)


class MessageNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Message
        filter_fields = {
            'id': ['exact'],
            'discussion__id': ['exact'],
            'user__id': ['exact']
        }
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)
