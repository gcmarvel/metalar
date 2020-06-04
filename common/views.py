from django.views.generic import TemplateView
from steelwork.models import Service as SteelworkService


class HomePageView (TemplateView):
    template_name = 'steelwork/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = SteelworkService.objects.filter(active=True)
        return context


class PortfolioView (TemplateView):
    template_name = 'steelwork/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = SteelworkService.objects.filter(active=True)
        context['service'] = SteelworkService.objects.get(id=self.kwargs['service'])
        context['images'] = SteelworkService.objects.get(id=self.kwargs['service']).images
        return context
