from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Blogs, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.db.models import Q

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs_list.html'

class BlogsDetailView(LoginRequiredMixin, DetailView):
    model = Blogs
    template_name = 'blogs_detail.html'

class BlogsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blogs
    fields = ('title', 'body', 'cover')
    template_name = 'blogs_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blogs
    template_name = 'blogs_delete.html'
    success_url = reverse_lazy('blogs_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogsCreateView(LoginRequiredMixin, CreateView):
    model = Blogs
    fields = ('title', 'body', 'cover')
    template_name = 'blogs_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# function for our comments
def add_comment_to_post(request, pk):
    blogs = get_object_or_404(Blogs, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blogs = blogs
            comment.author = request.user
            comment.save()
            return redirect('blogs_detail', pk=blogs.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})



# class for search
class SearchResultsListView(ListView):
    model = Blogs
    template_name = 'search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Blogs.objects.filter(Q(title__icontains=query) | Q(title__icontains=query))