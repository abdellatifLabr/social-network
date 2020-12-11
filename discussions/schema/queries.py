import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from django.db.models import Q

from ..models import Message, Discussion
from .nodes import MessageNode, DiscussionNode


class DiscussionQuery(graphene.ObjectType):
    discussion = graphene.relay.Node.Field(DiscussionNode)
    discussions = DjangoFilterConnectionField(DiscussionNode)
    my_discussions = DjangoFilterConnectionField(DiscussionNode)

    @login_required
    def resolve_my_discussions(self, info, **kwargs):
        user = info.context.user
        return Discussion.objects.filter(
            Q(sender=user) |
            Q(receiver=user)
        )


class MessageQuery(graphene.ObjectType):
    message = graphene.relay.Node.Field(MessageNode)
    messages = DjangoFilterConnectionField(MessageNode)
    my_messages = DjangoFilterConnectionField(MessageNode)

    @login_required
    def resolve_my_messages(self, info, **kwargs):
        user = info.context.user
        return Message.objects.filter(user=user)
