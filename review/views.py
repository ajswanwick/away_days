from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login,logout
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm




class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'home.html'

# Create your views here.
def login_view(request):
    """
    Custom login view
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # Redirect to the homepage after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Ensure the password is hashed
            user.is_active = True  # Ensure the user is active
            user.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()  # Fetch all reviews
    context = {'reviews': reviews}
    return render(request, 'review/review_list.html', context)


@login_required(login_url='login') 
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


@login_required(login_url='login')  # Redirect to login if not authenticated
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect('review_list')  # Ensure only the owner can edit
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully.")
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/review_form.html', {'form': form})

@login_required(login_url='login')  # Redirect to login if not authenticated
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        raise Http404("You are not authorized to delete this review.")
    if request.method == 'POST':
        review.delete()
        messages.success(request, "Review deleted successfully.")
        return redirect('review_list')
    return render(request, 'review/review_confirm_delete.html', {'review': review})


