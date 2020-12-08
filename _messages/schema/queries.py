import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from ..models import Message
from .nodes import MessageNode


class MessageQuery(graphene.ObjectType):
    message = graphene.relay.Node.Field(MessageNode)
    messages = DjangoFilterConnectionField(MessageNode)
    my_messages = DjangoFilterConnectionField(MessageNode)

    @login_required
    def resolve_my_messages(self, info, **kwargs):
        user = info.context.user
        return Message.objects.filter(sender=user)
