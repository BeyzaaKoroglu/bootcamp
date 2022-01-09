from django_filters import rest_framework as filters

from baskets.models import Basket, BasketItem


class BasketItemFilter(filters.FilterSet):

    class Meta:
        model = BasketItem
        fields = ("product", "quantity", "price")


class BasketFilter(filters.FilterSet):

    class Meta:
        model = Basket
        fields = ("customer", "status")
