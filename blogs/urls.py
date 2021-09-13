from django.urls import path
from blogs import views


# import our views needed in this app
from .views import (
    BlogsListView,
    BlogsUpdateView,
    BlogsDetailView,
    BlogsDeleteView,
    BlogsCreateView,
    SearchResultsListView
)


urlpatterns = [
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('blogs/<uuid:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<uuid:pk>/edit/',
        BlogsUpdateView.as_view(), name='blogs_edit'),
    path('<uuid:pk>/',
        BlogsDetailView.as_view(), name='blogs_detail'),
    path('<uuid:pk>/delete',
        BlogsDeleteView.as_view(), name='blogs_delete'),
    path('new/', BlogsCreateView.as_view(), name='blogs_new'),
    path('', BlogsListView.as_view(), name='blogs_list'),
]