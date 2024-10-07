from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import CreateView, ListView

from .forms import ProfileForm
from .models import UserProfile


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfile
    context_object_name = 'profiles'













# def store_file(file):
#     with open("temp/image.jpg", "wb+") as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             user_profile = UserProfile(image=request.FILES['user_image'])
#             user_profile.save()
#             store_file(request.FILES['image'])
            # return HttpResponseRedirect('/profiles')
        #
        # return render(request, "profiles/create_profile.html", {
        #     "form": submitted_form
        # })