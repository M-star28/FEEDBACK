from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewList.as_view()),
    path("reviews/favourite", views.FavouriteReview.as_view()),
    path("reviews/<int:pk>", views.DetailReviewView.as_view())
    ]
