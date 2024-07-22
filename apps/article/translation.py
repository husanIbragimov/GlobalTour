from modeltranslation.translator import register, TranslationOptions

from .models import Article


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'content',)
    # required_languages = ('en', 'ru')

    fallback_values = {
        'name': 'uz',
        'slug': 'uz',
        'content': 'uz',
    }

    fallback_undefined = {
        'name': 'uz',
        'slug': 'uz',
        'content': 'uz',
    }

    fallback = {
        'name': 'uz',
        'slug': 'uz',
        'content': 'uz',
    }

    fallback_language = {
        'name': 'uz',
        'slug': 'uz',
        'content': 'uz',
    }
