from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages




class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'home.html'

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register', {'form': form})


@login_required
def review_list(request):
    reviews = Review.objects.all()  # Fetch all reviews
    context = {'reviews': reviews}
    return render(request, 'review/review_list.html', context)


@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Set the current user
            review.save()
            return redirect('review_list')  # Redirect to the list view after saving
    else:
        form = ReviewForm()
    
    return render(request, 'review/review_form.html', {'form': form})