from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"  # Changed from "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"  # Changed from