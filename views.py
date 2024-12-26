from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostViewDetails(DetailView):
    model = Post
    template = 'post_details.html'

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})
    

