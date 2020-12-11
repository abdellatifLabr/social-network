import graphene


class CountableConnection(graphene.relay.Connection):
    class Meta:
        abstract = True

    count = graphene.Int()

    def resolve_count(self, info, **kwargs):
        return self.iterable.count()
