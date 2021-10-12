from django_filters import FilterSet
from django_filters.filters import OrderingFilter
from .models import Post
from django.db.models import Avg, Count, Sum, Q
from django.db.models.functions import Length


class CustomOrderingFilter(OrderingFilter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('rating', 'Rating'),
            ('likes', 'Likes'),
            ('comments', 'Comments'),
            ('word_count', 'Comments'),
        ]

    def filter(self, qs, value):
        if value:
            if 'rating' in value:
                return qs.annotate(_rating=Avg('ratings__value')).order_by('-_rating')

            if 'likes' in value:
                return qs.annotate(likes_count=Count('likes')).order_by('-likes_count')

            if 'comments' in value:
                return qs.annotate(comments_count=Count('comments')).order_by('-comments_count')

            if 'word_count' in value:
                return qs.annotate(word_count=Sum(Length('sections__content'), filter=Q(sections__type='TEXT'))).order_by('-word_count')

        return super().filter(qs, value)


class PostFilterSet(FilterSet):
    order_by = CustomOrderingFilter()

    class Meta:
        model = Post
        fields = {
            'id': ['exact'],
            'created_at': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }
