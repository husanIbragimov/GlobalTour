from django.urls import path

from .views import IndexView, TourDetailView, TourListView

app_name = 'tour'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tour/<slug:slug>/', TourDetailView.as_view(), name='tour_detail'),
    path('tours/list', TourListView.as_view(), name='tour_list'),
]
