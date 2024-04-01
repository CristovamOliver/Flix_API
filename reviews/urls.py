from django.urls import path
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestrowView


urlpatterns = [
    path("review/", ReviewCreateListView.as_view(), name='review-create-list'),
    path("review/<int:pk>", ReviewRetrieveUpdateDestrowView.as_view(),
         name='review-detail-view'),
]
