import graphene
from graphql_auth.schema import UserNode
from ..models import User
from shared.connections import CountableConnection
from ..filters import UserFilterSet


class IUserNode(UserNode):
    pk = graphene.Int(source='pk')
    image_url = graphene.String(source='image_url')

    class Meta:
        model = User
        exclude = [
            'password'
        ]
        filterset_class = UserFilterSet
        connection_class = CountableConnection
        interfaces = (graphene.relay.Node,)
