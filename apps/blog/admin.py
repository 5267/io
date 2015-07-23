from django.contrib import admin
from .models import Article, Tag, Category

# Register your models here.

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)


#class ArticleAdmin(admin.ModelAdmin):
#        readonly_fields = ('create_date',)
    

#admin.site.register(Article, ArticleAdmin)
