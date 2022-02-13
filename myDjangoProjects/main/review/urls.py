from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('review/', ReviewView.as_view(), name="review"),
    path('review/<int:pk>/', DetailReview.as_view(), name="DetailReview"),
    path('review/add_review/', Create_review.as_view(), name="add_review"),
]

