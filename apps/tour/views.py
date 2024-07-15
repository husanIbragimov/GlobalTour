from django.views.generic import TemplateView

from apps.about.models import About
from apps.common.models import Country
from .models import Tour


class IndexView(TemplateView):
    template_name = 'tour/index.html'
    context_object_name = 'tours'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tours'] = self.get_queryset()
        ctx['about'] = About.objects.last()
        ctx['countries'] = Country.objects.filter(parent__isnull=True).order_by('name')
        return ctx

    def get_queryset(self):
        return Tour.objects.prefetch_related('galleries', 'plans').all()


class TourDetailView(TemplateView):
    template_name = 'tour/tour-detail.html'
    context_object_name = 'tour'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tour'] = self.get_queryset().first()
        return ctx

    def get_queryset(self):
        return Tour.objects.prefetch_related('galleries', 'plans').filter(slug=self.kwargs.get('slug'))
