from django.shortcuts import redirect,render

from blog_app.forms import PostForm
from blog_app.models import Post
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.contrib import messages
from blog_app.forms import SignupForm
#function based views
# class based views

from django.views.generic import ListView,DetailView, CreateView, UpdateView, View
from django.urls import reverse
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at")

        query = self.request.GET.get("q")

        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )

        return posts

# Create your views here.
class PostDetailView(DetailView):
    model = Post
    template_name="post_detail.html"
    context_object_name="post"

    def get_queryset(self):
         queryset = Post.objects.filter(pk=self.kwargs["pk"],published_at__isnull=False)
         
         return queryset

from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name="draft_list.html"
    context_object_name="posts"

    def get_queryset(self):
         queryset = Post.objects.filter(published_at__isnull=True)
         return queryset

class DraftDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name="draft_detail.html"
    context_object_name="post"

    def get_queryset(self):
         queryset = Post.objects.filter(pk=self.kwargs["pk"],published_at__isnull=True)
         return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
     model =Post
     template_name="post_create.html"
     form_class= PostForm

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)
     
     def get_success_url(self):
          return reverse("draft-detail", kwargs={"pk": self.object.pk})

class PostUpdateView(LoginRequiredMixin, UpdateView):
     model =Post
     template_name="post_create.html"
     form_class= PostForm

     def get_success_url(self):
          post = self.get_object()
          if post.published_at:
            return reverse("post-detail", kwargs={"pk": post.pk})
          else:
            return reverse("draft-detail", kwargs={"pk": post.pk})

from django.utils import timezone

class DraftPublishView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk, published_at__isnull=True)
        post.published_at= timezone.now()
        post.save()
        return redirect("post-list")

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        if post.published_at:
            return redirect("post-list")
        else: 
            return redirect("draft-list")

@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    if post.published_at:
        return redirect("post-list")
    else:
        return redirect("draft-list")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            messages.success(request, "Account created successfully!")
            return redirect("post-list")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})