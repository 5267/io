from django.contrib import admin
from models import Article, Tag, Category
from adminfiles.admin import FilePickerAdmin

admin.site.register(Tag)
admin.site.register(Category)

class PostAdmin(FilePickerAdmin):
    adminfiles_fields = ('text',)

admin.site.register(Article, PostAdmin)