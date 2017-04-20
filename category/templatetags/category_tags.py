from django import template

from article.models import Article

register = template.Library()


# Featured blog post feed for home page
@register.inclusion_tag('common/featured_blog_posts_listing.html', takes_context=True)
def featured_blog_post_category(context, category):
    articles = Article.objects.filter(live=True, is_blog=True, featured_blog_post=True, category=category).order_by('?')[:10]
    return {
        'articles': articles,
        'request': context['request'],
    }


def get_new_articles(category):
    articles = Article.objects.filter(live=True, is_blog=False, is_top_post=False, category=category).order_by('-created')[:10]
    return articles


# Articles feed for home page
# Get the articles which are live and not top post because top post already have it's own section.
@register.inclusion_tag('common/articles_listing.html', takes_context=True)
def new_articles_category(context, category):
    articles = get_new_articles(category)
    return {
        'articles': articles,
        'request': context['request'],
    }


# Top Posts feed for home page
# Get random 10 top post, if there are not 10 top posts, get the remaining random articles and add to the top post
# Make sure the same article is not shown in New Article (Mid-Section)
@register.inclusion_tag('common/top_posts_listing.html', takes_context=True)
def top_posts_category(context, category):
    articles = Article.objects.filter(live=True, is_blog=False, is_top_post=True, category=category).order_by('?')[:10]
    total_top_posts = articles.count()
    if total_top_posts < 10:
        remaining_post = 10 - total_top_posts
        additional_articles = Article.objects.filter(live=True, is_blog=False, is_top_post=False, category=category).order_by('?')
        exclude_new_articles = additional_articles.exclude(pk__in=get_new_articles(category))[:remaining_post]
        articles = list(articles) + list(exclude_new_articles)

    return {
        'articles': articles,
        'request': context['request'],
    }



