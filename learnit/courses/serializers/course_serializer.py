from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
        'id',
        'playlist_title',
        'playlist_image_url',
        'playlist_views',
        'playlist_videos_count',
        'playlist_id',
        'playlist_url',
        'playlist_owner',
        'playlist_owner_url',
        'priority',
        'category',
        'languare',
        'pub_date',
        ]
        