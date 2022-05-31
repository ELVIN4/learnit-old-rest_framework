from django.urls import reverse
from rest_framework.test import APITestCase
from django.utils import timezone
from courses.serializers.course_serializer import CourseSerializer
from courses.models import Course, Category, Languare
