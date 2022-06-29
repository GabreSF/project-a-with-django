from django.urls import path

from tips.views import home, my_view

urlpatterns = [
    path('about/', my_view),
    path('', home),
]
