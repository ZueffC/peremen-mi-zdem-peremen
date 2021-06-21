from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import *


class IndexPage(ListView):
    
    #основная логика CBV
    model = BlogModel
    template_name = 'index.html'
    
    #Контекст
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['latest_posts'] = BlogModel.objects.order_by("-id")[0:3]
        return context
    

class DetailPostView(DetailView):
    model = BlogModel
    template_name = 'post.html'

class PostsPage(ListView):
    model = BlogModel
    template_name = 'all.html'
    
    
def about_view(request):
    about = AboutModel.objects.last()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)

