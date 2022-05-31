from django.urls import path 

from .views import CourseListView
from .views import CategoryListView
from .views import LanguareListView

app_name = 'courses'

urlpatterns = [
    path('courses', CourseListView.as_view(), name='courses'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('languages', LanguareListView.as_view(), name='languares'),
]