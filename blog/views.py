from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # .는 현재 디렉토리 또는 애플리케이션을 의미. 동일한 디렉터리 내 views.py, models.py파일이 있기 때문에 .파일명(.py 확장자를 붙이지 않아도)으로 내용을 가져올 수 있다.
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # 글 목록을 게시일(published_date)기준으로 정렬하기.
	return render(request, 'blog/post_list.html', {'posts': posts})

#Post.objects.get(pk=pk)
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
#def post_new(request):
#	if request.method == "POST":
#		form = PostForm(request.POST)
#		if form.is_valid():
#			post = form.save(commit=False)
#			post.author = request.user
#			post.published_date = timezone.now()
#			post.save()
#			return redirect('post_detail', pk=post.pk)
#		else:
#			form = PostForm()
##		return render(request, 'blog/post_edit.html', {'form': form})
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
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        #form = PostForm(request.POST, instance=post)
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(request, 'blog/post_edit.html', {'form': form})