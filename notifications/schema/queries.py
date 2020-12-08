import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from django.db.models import Q

from ..models import Notification
from .nodes import NotificationNode


class NotificationQuery(graphene.ObjectType):
    notification = graphene.relay.Node.Field(NotificationNode)
    my_notifications = DjangoFilterConnectionField(NotificationNode)

    @login_required
    def resolve_my_notifications(self, info, **kwargs):
        user = info.context.user
        return Notification.objects.filter(
            Q(follow__followed=user) |
            Q(comment__post__user=user) |
            Q(like__post__user=user)
        )
