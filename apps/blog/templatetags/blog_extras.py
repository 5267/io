from django import template
from apps.blog.models import Category, Tag

register = template.Library()

@register.inclusion_tag('categories.html', takes_context=True)
def GetCategories(context):
    categories = Category.objects.all()
    return {'categories':categories}

@register.inclusion_tag('tags.html', takes_context=True)
def GetTags(context):
    tags = Tag.objects.all().order_by('?')
    return {'tags':tags}
