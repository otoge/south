from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    script = filters.CharFilter(label='セリフ', lookup_expr='contains')

    # order_by = MyOrderingFilter(
    #
    #     fields=(
    #         ('script', 'script'),
    #     ),
    #     # field_labels={
    #     #     'script': 'セリフ',
    #     # },
    #     # label='並び順'
    # )

    class Meta:
        model = Item
        fields = ('script',)
