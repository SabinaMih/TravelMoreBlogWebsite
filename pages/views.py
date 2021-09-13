from django.views.generic import TemplateView

# we have imported a built-in TemplateView to be able to display out templates
# Creating our views.
class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogsPageView(TemplateView):
    template_name = 'blogs.html'

class PlanATripPageView(TemplateView):
    template_name = 'planATrip.html'

class TipsForTravelPageView(TemplateView):
    template_name = 'tipsForTravel.html'

class TopDestinationsPageView(TemplateView):
    template_name = 'topDestinations.html'

class ContactUsPageView(TemplateView):
    template_name = 'contactUs.html'

class BlogsDetailPageView(TemplateView):
    template_name = 'blogs_detail.html'

