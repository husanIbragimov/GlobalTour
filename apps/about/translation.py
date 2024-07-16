from modeltranslation.translator import register, TranslationOptions

from .models import About


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
    # required_languages = ('en', 'ru')

    fallback_values = {
        'name': 'uz',
        'description': 'uz',
    }

    fallback_undefined = {
        'name': 'uz',
        'description': 'uz',
    }

    fallback = {
        'name': 'uz',
        'description': 'uz',
    }

    fallback_language = {
        'name': 'uz',
        'description': 'uz',
    }
