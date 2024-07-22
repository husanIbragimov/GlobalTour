from modeltranslation.translator import register, TranslationOptions

from .models import Tour, TourPlan


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'slug', 'duration', 'group')
    # required_languages = ('en', 'ru')

    fallback_values = {
        'name': 'uz',
        'description': 'uz',
        'slug': 'uz',
        'duration': 'uz',
        'group': 'uz',
    }

    fallback_undefined = {
        'name': 'uz',
        'description': 'uz',
        'slug': 'uz',
        'duration': 'uz',
        'group': 'uz',
    }

    fallback = {
        'name': 'uz',
        'description': 'uz',
        'slug': 'uz',
        'duration': 'uz',
        'group': 'uz',
    }

    fallback_language = {
        'name': 'uz',
        'description': 'uz',
        'slug': 'uz',
        'duration': 'uz',
        'group': 'uz',
    }


@register(TourPlan)
class TourPlanTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
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

