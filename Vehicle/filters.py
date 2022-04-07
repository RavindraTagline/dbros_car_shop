import django_filters

from .models import Car


class CarFilters(django_filters.FilterSet):

    make = django_filters.CharFilter(lookup_expr='iexact')
    year = django_filters.NumberFilter(field_name='year',)

    class Meta:
        model = Car
        fields = '__all__'
