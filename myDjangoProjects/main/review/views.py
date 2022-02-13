from .models import Review
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from django.views.generic import DetailView, ListView, CreateView


class DetailReview(DetailView):
    model = Review
    template_name = 'review/detail_review.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        title_object = Review.title
        context['title'] = title_object


class ReviewView(ListView):
    model = Review
    template_name = 'review/review.html'
    context_object_name = 'review'
    paginate_by = 2


class Create_review(CreateView):
    form_class = ReviewForm
    template_name = 'review/add_review.html'




# def add_review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('review')
#     else:
#         form = ReviewForm()
#     return render(request, 'review/add_review.html', {'form': form})
