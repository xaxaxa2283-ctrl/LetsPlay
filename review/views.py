from django.shortcuts import render

from django.views.generic import DetailView

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Reviews

# Create your views here.
def review(request):
    review = Reviews.objects.all()
    return render(request,'review/review.html',{'review':review})


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = 'review/review_detail.html'
    context_object_name = 'review'








