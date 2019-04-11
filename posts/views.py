from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.decorators.http import require_POST

# Create your views here.
def create(request):
    if request.method == "POST":
        #작성된 post를 DB에 적용
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:  # GET
        # post를 작성하는 form을 보여줌
        form = PostForm()
        return render(request, 'posts/create.html', {'form':form})
        
        
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})
    

@require_POST
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('posts:list')
        
        
def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        # 실제 DB에 수정 반영
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:  # GET
        form = PostForm(instance=post)
        return render(request, 'posts/update.html', {'form':form})