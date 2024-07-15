from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from apps.article.models import Article
from apps.common.models import Country
from .models import Tour, BookingTour


class IndexView(TemplateView):
    template_name = 'tour/index.html'
    context_object_name = 'tours'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tours'] = self.get_queryset()
        ctx['experiences'] = Article.objects.filter(is_active=True).order_by('-id')[:3]
        ctx['countries'] = Country.objects.filter(parent__isnull=True).order_by('name')
        return ctx

    def get_queryset(self):
        return Tour.objects.prefetch_related('galleries', 'plans').all()


class TourDetailView(View):
    template_name = 'tour/tour-detail.html'

    def get(self, request, *args, **kwargs):
        tour = Tour.objects.prefetch_related('galleries', 'plans').get(slug=kwargs['slug'])
        return render(request, self.template_name, {'tour': tour})

    def post(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        BookingTour.objects.create(
            tour_id=request.POST.get('tour_id'),
            full_name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            people=request.POST.get('people'),
            message=request.POST.get('message', None)
        )
        message = 'Sizning buyurtmangiz qabul qilindi. Tez orada siz bilan bog\'lanamiz.'
        messages.success(request, message, extra_tags='success')
        return redirect(url)


class TourListView(View):
    template_name = 'tour/tours.html'
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        tours = Tour.objects.prefetch_related('galleries', 'plans').all()
        return render(request, self.template_name, {'tours': tours})

    def post(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        BookingTour.objects.create(
            tour_id=request.POST.get('tour_id'),
            full_name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            people=request.POST.get('people'),
            message=request.POST.get('message', None)
        )
        message = 'Sizning buyurtmangiz qabul qilindi. Tez orada siz bilan bog\'lanamiz.'
        messages.success(request, message, extra_tags='success')
        return redirect(url)
