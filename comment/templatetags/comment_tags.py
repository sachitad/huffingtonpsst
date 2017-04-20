from django import template

from article.models import Article

register = template.Library()


@register.filter(name='active')
def get_active_comments(comments_object):
    total_comment = 0
    for comment in comments_object:
        if comment.is_active:
            total_comment += 1

    return total_comment


@register.simple_tag()
def count_comments(article):
    try:
        article = Article.objects.get(pk=article)
    except Article.DoesNotExist:
        return 0
    total_count = article.related_comments.all().count()
    if total_count > 0:
        return '(%s)' % total_count
    else:
        return ''


@register.simple_tag()
def count_comments_neat(article):
    try:
        article = Article.objects.get(pk=article)
    except Article.DoesNotExist:
        return 0
    return article.related_comments.all().count()