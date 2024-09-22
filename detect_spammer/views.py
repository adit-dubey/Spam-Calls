from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, SearchForm
from .models import DetectSpammer, Spam


# Function to register new user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def mark_spam(request, phone_number):
    spam_exists = Spam.objects.filter(phone_number=phone_number, reported_by=request.user).exists()
    
    if not spam_exists:
        Spam.objects.create(phone_number=phone_number, reported_by=request.user)
    return redirect('register')


def search(request):
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        if query:
            users_by_name = DetectSpammer.objects.filter(name__icontains=query)
            
            users_by_phone = DetectSpammer.objects.filter(phone_number=query)

            results = users_by_name | users_by_phone
            results = results.distinct()

    return render(request, 'search_results.html', {'form': form, 'results': results})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(DetectSpammer, id=user_id)
    spam_score = Spam.objects.filter(phone_number=user.phone_number).count()
    email = user.email if user in request.user.contacts.all() else '*******'
    return render(request, 'user_detail.html', {
        'user': user,
        'spam_score': spam_score,
        'email': email
    })



