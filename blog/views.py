from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blog.models import Post


def post_list(request):
    # Template을 찾을 경로에서
    #  post_list.html을 찾아서
    #  그 파일을 text로 만들어서 HttpResponse형태로 돌려준다.
    # 위 기능을 하는 shortcut함

    # 1. posts라는 변수에 전체 Post를 가지는 QuerySet객체를 할당
    #    hint) Post.objects.무언가.....를 실행한 결과는 QuerySet객체가 된다
    # 2. context라는 dict를 생성하며, 'posts'키에 위 posts변수를 value로 사용하도록 한다.
    # 3. render의 3번째 위치인자로 위 context변수를 전달한다.
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


def post_delete(reqeust, pk):
    if reqeust.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()

        return redirect('url-name-post-list')