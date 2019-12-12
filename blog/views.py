from django.shortcuts import render

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
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'post_list.html', context)


def post_detail(request):
    return render(request, 'post_detail.html')
