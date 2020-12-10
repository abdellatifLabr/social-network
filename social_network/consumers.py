import channels_graphql_ws

from .schema import schema


class GraphqlWsConsumer(channels_graphql_ws.GraphqlWsConsumer):
    schema = schema

    async def on_connect(self, payload):
        pass
