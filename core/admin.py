from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *
# Register your models here.
class ArticleAdmin(SummernoteModelAdmin):
  summernote_fields = '__all__'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Email)
