from django.urls import path,include
from .views import *
urlpatterns = [
    path("category/",CategoryViews.as_view()),
    path("categorydetail/<int:pk>",CategoryViews.as_view())
]
