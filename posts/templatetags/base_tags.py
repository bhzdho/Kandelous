from django import template
from ..models import CategoryModel
register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"


@register.inclusion_tag("posts/partial/navbar.html")
def category_navbar():
    return {
            "category":CategoryModel.objects.filter(status = True)
    }
