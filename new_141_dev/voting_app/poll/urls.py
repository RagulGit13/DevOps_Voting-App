from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list_view, name='poll_list'),  # Add this line
    path('<int:poll_id>/vote/', views.vote_view, name='vote'),
    path('<int:poll_id>/results/', views.results_view, name='results'),
]
