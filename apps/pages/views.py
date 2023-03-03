from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from .models import UserPost, Comment
from .forms import UserPostForm

# Create your views here.

class PostListView(ListView):
    model = UserPost
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = UserPost
    template_name = 'post_detail.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = UserPost
    form_class = UserPostForm
    template_name = 'post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = UserPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    model = UserPost
    form_class = UserPostForm
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class CommentCreateView(LoginRequiredMixin ,CreateView):
    model = Comment
    fields = ('author', 'body',)
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.userpost_id = self.kwargs['pk']
        return super().form_valid(form)