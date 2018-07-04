__author__ = 'likeyang'
__date__ = '2018/6/25 17:58'

import django_filters
from .models import Goods
from django.db.models import Q

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤
    """
    pricemin = django_filters.NumberFilter(name="shop_price",lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price",lookup_expr='lte')
    top_category = django_filters.NumberFilter(method="top_category_filter")

    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))


    class Meta:
        model = Goods
        fields = ['pricemin','pricemax']
