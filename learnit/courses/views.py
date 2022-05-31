from django_filters import rest_framework as filters
from rest_framework import generics

from .models import Category, Course, Languare
from .serializers.category_serializer import CategorySerializer
from .serializers.course_serializer import CourseSerializer
from .serializers.languare_serializer import LanguareSerializer


class CourseListView(generics.ListAPIView):
    """
    Returns a list of courses with the ability to filter by the fields languare, category, id.

    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all().filter(is_published=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'languare', 'id')


class CategoryListView(generics.ListAPIView):
    """
    Returns a list of categories with the ability to filter by the fields languare, parent_category, id.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all().filter(is_published=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('parent_category', 'languare', 'id')

class LanguareListView(generics.ListAPIView):
    """
    Returns a list of courses selectable by ID.
    """
    serializer_class = LanguareSerializer
    queryset = Languare.objects.all().filter(is_published=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id',)

