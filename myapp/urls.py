from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default page with buttons
    path('pjm/', views.pjm, name='pjm'),  # PJM page
    path('nyiso/', views.nyiso, name='nyiso'),  # NYISO page
    path('isone/', views.isone, name='isone'),  # ISONE page
]
