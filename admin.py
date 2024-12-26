from django.contrib import admin
from .models import Post

admin.site.register(Post)


from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here. 


class HomeView(ListView):
    model = Post
    template_name= 'home.html'

class PostViewDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddView(CreateView):
    model = Post
    template_name = 'add.html'


# Create your views here. 

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'sections': 'dashboard'})

