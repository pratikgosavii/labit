import django_filters
from .models import lab_test

class LabTestFilter(django_filters.FilterSet):
    test = django_filters.NumberFilter(field_name="test__id")  # Filter by test ID
    min_price = django_filters.NumberFilter(field_name="b2b_price", lookup_expr="gte")  # Min price
    max_price = django_filters.NumberFilter(field_name="b2b_price", lookup_expr="lte")  # Max price
    max_processing_time = django_filters.NumberFilter(field_name="processing_time", lookup_expr="lte")  # Max processing time
    category = django_filters.NumberFilter(field_name="test__category__id")  # Filter category by ID

    class Meta:
        model = lab_test
        fields = ['test', 'min_price', 'max_price', 'max_processing_time', 'category']