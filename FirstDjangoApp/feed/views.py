from django.views.generic import TemplateView
from .models import Posts

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['posts'] = Posts.objects.all()
        return context