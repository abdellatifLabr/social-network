from django_filters.filterset import FilterSet
from django_filters.filters import OrderingFilter
from .models import User
from django.db.models import Count


class CustomOrderingFilter(OrderingFilter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('most_liked', 'Most likes'),
            ('most_followers', 'Most Followers'),
            ('posts_count', 'Posts count'),
        ]

    def filter(self, qs, value):
        if value:
            if 'most_liked' in value:
                return qs.annotate(likes_count=Count('likes')).order_by('-likes_count')

            if 'most_followers' in value:
                return qs.annotate(followers_count=Count('followers')).order_by('-followers_count')

            if 'posts_count' in value:
                return qs.annotate(posts_count=Count('posts')).order_by('-posts_count')

        return super().filter(qs, value)


class UserFilterSet(FilterSet):
    order_by = CustomOrderingFilter()

    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'created_at': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }
