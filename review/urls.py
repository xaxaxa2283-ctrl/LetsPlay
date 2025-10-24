from django.urls import path
from . import views
urlpatterns = [
    path('', views.review, name='rewiew'),
    path('<int:pk>', views.ReviewsDetailView.as_view(), name='rewiews_detail'),


]

