from django import template

from article.models import Article
from author.models import Author
from video.models import Video

register = template.Library()


# Featured blog post feed for home page
@register.inclusion_tag('common/featured_blog_posts_listing.html', takes_context=True)
def featured_blog_post(context):
    articles = Article.objects.filter(live=True, is_blog=True, is_top_post=True).order_by('-created')[:10]
    authors = Author.objects.filter(is_active=True).order_by('?')[:5]

    return {
        'articles': articles,
        'authors': authors,
        'request': context['request'],
    }


# Get one random article for featured blog authors
@register.assignment_tag()
def get_article(author):
    return Article.objects.filter(author=author, live=True, is_blog=True).order_by('?')[:1]


def get_new_articles():
    articles = Article.objects.filter(live=True, is_blog=False, is_top_post=False).order_by('-created')[:10]
    return articles


# Articles feed for home page
# Get the articles which are live and not top post because top post already have it's own section.
@register.inclusion_tag('common/articles_listing.html', takes_context=True)
def new_articles(context):
    articles = get_new_articles()
    return {
        'articles': articles,
        'request': context['request'],
    }


# Top Posts feed for home page
# Get random 10 top post, if there are not 10 top posts, get the remaining random articles and add to the top post
# Make sure the same article is not shown in New Article (Mid-Section)
@register.inclusion_tag('common/top_posts_listing.html', takes_context=True)
def top_posts(context):
    articles = Article.objects.filter(live=True, is_blog=False, is_top_post=True).order_by('?')[:10]
    total_top_posts = articles.count()
    if total_top_posts < 10:
        remaining_post = 10 - total_top_posts
        additional_articles = Article.objects.filter(live=True, is_blog=False, is_top_post=False).order_by('?')
        exclude_new_articles = additional_articles.exclude(pk__in=get_new_articles())[:remaining_post]
        articles = list(articles) + list(exclude_new_articles)

    return {
        'articles': articles,
        'request': context['request'],
    }


@register.inclusion_tag('common/footer_articles.html', takes_context=True)
def footer_articles(context):
    articles = Article.objects.filter(live=True, is_blog=False, is_top_post=False, featured_image__isnull=False).order_by('?')
    articles.exclude(pk__in=get_new_articles())[:9]
    return {
        'articles': articles,
        'request': context['request'],
    }


# Get top 5 random authors to show in the front page and category pages
@register.inclusion_tag('common/huffingtonpost_live.html', takes_context=True)
def get_videos(context):
    videos = Video.objects.filter(live=True).order_by('?')[:10]
    return {
        'videos': videos,
        'request': context['request'],
    }


# Get top 5 random authors to show in the front page and category pages
@register.inclusion_tag('common/random_authors.html', takes_context=True)
def random_authors(context):
    authors = Author.objects.filter(is_active=True).order_by('?')[:5]
    return {
        'authors': authors,
        'request': context['request'],
    }

