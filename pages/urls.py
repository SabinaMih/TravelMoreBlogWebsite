from django.urls import path
from .views import HomePageView, BlogsPageView, PlanATripPageView, TipsForTravelPageView, TopDestinationsPageView, ContactUsPageView, BlogsDetailPageView    # connecting our views to urls


urlpatterns = [
    path('contact/', ContactUsPageView.as_view(), name='contactUs'),
    path('blogs_detail/', BlogsDetailPageView.as_view(), name='blogs_detail'),
    path('topDestinations/', TopDestinationsPageView.as_view(), name='topDestinations'),
    path('tipsForTravel/', TipsForTravelPageView.as_view(), name='tipsFortravel'),
    path('planATrip/', PlanATripPageView.as_view(), name='planATrip'),
    path('blogs/', BlogsPageView.as_view(), name='blogs'),
    path('', HomePageView.as_view(), name='home'),
]