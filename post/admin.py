from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title','owner','created_at')
    search_fields = ['title']
    list_filter = ['title','owner']
    summernote_fields = ('content',)