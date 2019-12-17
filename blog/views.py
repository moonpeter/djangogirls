from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post


def post_list(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }

    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return HttpResponse('없음')

    context = {
        'post': post,
    }

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        text = request.POST['text']

        post = Post.objects.create(
            author=author,
            title=title,
            text=text,
        )
        result = f'title: {post.title}, created_date: {post.created_date}'
        # post_list_url = reverse('url-name-post-list')
        # return HttpResponseRedirect('/posts/')
        return redirect('url-name-post-list')
    else:
        return render(request, 'post_add.html')


def post_delete_confirm(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_delete_confirm.html', context)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()

        return redirect('url-name-post-list')
