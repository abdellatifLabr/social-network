import graphene
from graphql_jwt.decorators import login_required
from graphql_auth.types import ExpectedErrorType
from django.core.exceptions import ValidationError

from ..models import Notification
from .nodes import NotificationNode


class CreateNotificationMutation(graphene.relay.ClientIDMutation):
    class Input:
        follow_id = graphene.ID()
        comment_id = graphene.ID()
        like_id = graphene.ID()

    notification = graphene.Field(NotificationNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, follow_id=None, comment_id=None, like_id=None, **kwargs):
        user = info.context.user

        if not (follow_id or comment_id or like_id):
            errors = {
                'notification': [
                    {
                        'message': 'Please specify a follow or a comment of a like.',
                        'code': 'invalid'
                    }
                ]
            }
            return CreateNotificationMutation(success=False, errors=errors)

        notification = Notification(author=user, **kwargs)

        try:
            notification.full_clean()
        except ValidationError as e:
            return CreateNotificationMutation(success=False, errors=e.message_dict)

        notification.save()
        return CreateNotificationMutation(success=True, notification=notification)


class UpdateNotificationMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        seen = graphene.Boolean()

    notification = graphene.Field(NotificationNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            notification = Notification.objects.get(pk=id)
        except Notification.DoesNotExist:
            errors = {
                'notification': [
                    {
                        'message': 'This notification does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return UpdateNotificationMutation(success=False, errors=errors)

        if not (notification.follow.user == user or notification.comment.user == user or notification.like.user == user):
            raise PermissionError('You do not have the permission to perform this action')

        for field, value in kwargs.items():
            setattr(notification, field, value)

        try:
            notification.full_clean()
        except ValidationError as e:
            return UpdateNotificationMutation(success=False, errors=e.message_dict)

        notification.save()
        return UpdateNotificationMutation(success=True, notification=notification)


class DeleteNotificationMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            notification = Notification.objects.get(pk=id)
        except Notification.DoesNotExist:
            errors = {
                'notification': [
                    {
                        'message': 'This notification does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return DeleteNotificationMutation(success=False, errors=errors)

        if notification.author != user:
            raise PermissionError('You do not have the permission to perform this action')

        notification.delete()
        return DeleteNotificationMutation(success=True)
