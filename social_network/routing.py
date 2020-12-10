from django.urls import path

from .consumers import GraphqlWsConsumer

ws_urlpatterns = [
    path('graphql', GraphqlWsConsumer.as_asgi()),
]
