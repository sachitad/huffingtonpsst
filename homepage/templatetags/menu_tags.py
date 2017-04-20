from django import template

register = template.Library()

from article.models import Article
from category.models import Category


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    if page.get_children().filter(live=True, show_in_menus=True):
        return True
    else:
        return False


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('menu/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().filter(live=True, show_in_menus=True)
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('menu/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.filter(live=True, show_in_menus=True)

    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        #'tags': tags,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('menu/all_sections.html', takes_context=True)
def all_sections(context):
    categories = Category.objects.filter(live=True)
    return {
        'categories': categories,
        'request': context['request']
    }



@register.assignment_tag()
def get_tags(category):
    articles = category.get_children()
    articles = articles.filter(live=True, show_in_menus=True)
    articles = Article.objects.filter(pk__in=articles)
    tags = []
    for article in articles:
        for tag in article.tags.all():
            tags.append(tag.name)

    tags = list(set(tags))[:7]
    return tags


@register.assignment_tag()
def sub_vertical_menu():
    return Category.objects.filter(live=True, show_in_sub_menu=True)
