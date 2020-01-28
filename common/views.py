from django.views.generic import TemplateView
from steelwork.models import Service


class HomePageView (TemplateView):
    template_name = 'steelwork/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context



