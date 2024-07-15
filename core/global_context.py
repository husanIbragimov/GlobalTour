from apps.about.models import About

from apps.common.models import Country


def global_context(request):
    return {
        'about': About.objects.last(),
        'countries': Country.objects.filter(parent__isnull=True).order_by('name')
    }
