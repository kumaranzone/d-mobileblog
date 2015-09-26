from django.views import generic
from . import models
from django.utils import timezone


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['posts'] = models.Entry.objects.published()
        context["blog_title"] = "D-Mobile Blog"
        return context


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context["blog_title"] = "D-Mobile Blog"
        context['posts'] = models.Entry.objects.published()
        return context