from django.urls import path
from .views import info_view


urlpatterns = [
        path('v1/', info_view, name='info'),
    ]
