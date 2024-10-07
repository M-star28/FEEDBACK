from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, \
    ListView, DetailView, FormView, CreateView

from .forms import ReviewForm

from django.views import View

# Create your views here.
from .models import Review


class ReviewView(CreateView):
    model = Review
    # you can define the fields=__all__
    # to let Django create the form //or// use form_class but
    # you must use a model form then!! and it will able you to configure more than fields...
    # like labels and error messages
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # no need for a validator createview will
    # save data automatically when it's valid
    # def form_valid(self, form):
    #      form.save()
    #      return super().form_valid(form)

    #   form = ReviewForm()
    #   return render(request, "reviews/review.html", {
    #      "form": form})


# def post(self, request):
#   form = ReviewForm(request.POST)
#  if form.is_valid():
#   form.save()
#   print(form.cleaned_data)
# return HttpResponseRedirect("/thank-you")
# else:
# return render(request, "reviews/review.html", {
#    "form": form})


class ThankYouView(TemplateView):
    # def get(self,request):
    # return render(request, "reviews/thank_you.html")
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['message'] = " It works!"
        return context


class ReviewList(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #   base_query=super().get_queryset()
    #  data =base_query.filter(rating__gt=4)
    #   return data


###/def get_context_data(self, **kwargs):
## context = super().get_context_data()
# reviews = Review.objects.all()
# context['reviews'] = reviews
# return context


class DetailReviewView(DetailView):
    template_name = "reviews/detail-review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        request = self.request
        fav_review = request.session.get("favourite_review")
        loaded_object = self.object
        context['is_favourite'] = fav_review == str(loaded_object.id)
        return context


#   def get_context_data(self, **kwargs):
#   context =super().get_context_data()
#  review_id = kwargs['id']
#  selected_review=Review.objects.get(id=review_id)
# context['review'] = selected_review
# return context

class FavouriteReview(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)