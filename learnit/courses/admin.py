from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html


from .models import Category, ImageStyle, Course, Languare
from .services import image_generator_service, playlist_parser_service
from .forms.course_form import CourseForm
from .forms.category_form import CategoryForm
from .forms.image_style_form import ImageStyleForm

admin.AdminSite.site_header = 'LearnIt'


def html_image_gen(url, width=150, height=100):
    return format_html(f'<img src="{url}"" width="{width}" height="{height}" />')


class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = [
        'image_tag',
        'playlist_title',
        'pub_date',
        'last_update',
        'is_published',
        'category',
        'languare',
        'id',
        'playlist_views',
        'playlist_videos_count',
        'priority',
    ]

    def image_tag(self, obj):
        return html_image_gen(obj.playlist_image_url)



    def save_model(self, request, obj, form, change):
        playlist = playlist_parser_service.playlist_info(obj.playlist_url)
        
        obj.playlist_image_url = playlist.img_url
        obj.playlist_title = playlist.title
        obj.playlist_views = playlist.views
        obj.playlist_id = playlist.playlist_id
        obj.playlist_videos_count = playlist.videos_count
        obj.playlist_owner = playlist.owner
        obj.playlist_owner_url = playlist.owner_url

        super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = [
        'image_tag',
        'name',
        'parent_category',
        'priority',
        'is_published',
        'languare',
    ]

    def image_tag(self, obj):
        return html_image_gen(f'{settings.MEDIA_URL}{obj.image}')

    def save_model(self, request, obj, form, change):
        obj.image = image_generator_service.execute(
            obj.name,
            obj.image_style.watemark,  
            obj.image_style.bg_color, 
            obj.image_style.title_color, 
            obj.image_style.watemark_color,
            )
        super().save_model(request, obj, form, change)

class LanguareAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'priority',
        'is_published',
    ]

class ImageStyleAdmin(admin.ModelAdmin):
    form = ImageStyleForm
    list_display = [
        'image_tag',
        'name',
        'watemark',
    ]
    
    def image_tag(self, obj):
        return html_image_gen(f'{settings.MEDIA_URL}{obj.image}')

    def save_model(self, request, obj, form, change):
        obj.image = image_generator_service.execute(
        'TestCase',
        obj.watemark,  
        obj.bg_color, 
        obj.title_color, 
        obj.watemark_color,
        )
        super().save_model(request, obj, form, change)



admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Languare, LanguareAdmin)
admin.site.register(ImageStyle, ImageStyleAdmin)