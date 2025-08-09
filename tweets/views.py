from django.shortcuts import render, redirect
from .forms import TweetForm

def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tweet_success')  # <-- Redirect after successful POST
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_form.html', {'form': form})

def success(request):
    return render(request, 'tweets/success.html')