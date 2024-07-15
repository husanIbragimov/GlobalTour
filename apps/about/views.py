from django.shortcuts import render

from django.views.generic import TemplateView
from .models import About, Team, SocialLink


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['about'] = About.objects.last()
        ctx['teams'] = Team.objects.all()
        ctx['social_links'] = SocialLink.objects.all()
        return ctx
