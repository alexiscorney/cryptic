from django.shortcuts import render
from django.utils import timezone
from .models import Post, Clue
from .forms import PostForm, ClueForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

from axc680.cryptic.tools import pipeline as pipeline


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    clues = Clue.objects.all()
    return render(request, 'homepage/home.html', {'posts':posts, 'clues':clues})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'homepage/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'homepage/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'homepage/post_edit.html', {'form': form})

def clue_edit(request, pk):
    clue = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ClueForm(request.POST, instance=clue)
        if form.is_valid():
            clue = form.save(commit=False)
            clue.author = request.user
            

            sol = pipeline.test()
            clue.solution = sol

            clue.save()
            return redirect('clue_detail', pk=clue.pk)
    else:
        form = ClueForm(instance=clue)
    return render(request, 'homepage/clue_edit.html', {'form': form})

def clue_detail(request, pk):
    clue = get_object_or_404(Clue, pk=pk)
    return render(request, 'homepage/clue_detail.html', {'clue': clue})

def clue_new(request):
    if request.method == "POST":
        form = ClueForm(request.POST)
        if form.is_valid():
            clue = form.save(commit=False)
            clue.author = request.user
            clue.save()
            return redirect('clue_detail', pk=clue.pk)
    else:
        form = ClueForm()
    return render(request, 'homepage/clue_edit.html', {'form': form})