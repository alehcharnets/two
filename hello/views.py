from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from django.contrib.auth.models import User
from . import form
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def hello(request):
    return HttpResponse("!!!HELLO!!!")


def names(request):
    return render(
        request,
        'mytemplate.html',
        {"name": "PETR", "lastname": "PETROV"}
    )


def ShowAll(request):
    content = []  # [[vid, [все коментарии]], [vid, [все коментарии]],
    # [vid, [все коментарии]]]
    for vid in Video.objects.all():
        oneVid = [vid]
        comments_ = Comment.objects.filter(Comment_Video_id=vid.id)
        # [video, [(comment, name),(comment, name),(comment, name)]
        # oneVid.append(comments_)
        list_name = []
        for com in comments_:
            list_name.append(User.objects.get(id=com.Comment_User.id))
        comments_names = list(zip(comments_, list_name))
        oneVid.append(comments_names)
        content.append(oneVid)

    # пагинация страниц
    pagination = Paginator(content, 1)
    page_number = request.GET.get('page', 1)
    page = pagination.get_page(page_number)

    other_pages = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        "content": page,
        "other_pages": other_pages,
        "previous_url": previous_url,
        "next_url": next_url
    }

    return render(request, "AllVideos1.html", context=context)


def Search(request, *args, **kwargs):
    search_query = request.GET.get('search')
    found = Video.objects.filter(Q(Video_name__icontains=search_query))

    context = {
        "found": found,
        "args": args,
        "kwargs": kwargs
    }

    return render(request, "Search.html", context=context)


def OneVideo(request, video_id):
    # print(request.user.id)
    args = {}
    comment_form = form.CommentsForm
    args.update(csrf(request))
    args["form"] = comment_form
    args["video"] = Video.objects.get(id=video_id)
    args["Comment"] = Comment.objects.filter(Comment_Video_id=video_id)
    return render(request, "OneVideo.html", args)


def LikeaJax(request):
    if request.GET:
        idvideo = request.GET['addlike']
        video = Video.objects.get(id=idvideo)
        video.Video_likes += 1
        video.save()
    return HttpResponse(video.Video_likes)


def DisLikeaJax(request):
    print("1111")
    if request.GET:
        idvideo = request.GET['adddislike']
        video = Video.objects.get(id=idvideo)
        video.Video_dislikes += 1
        video.save()
    print("1111")
    return HttpResponse(video.Video_dislikes)


def AddComment(request, video_id):
    if request.POST:
        forma = form.CommentsForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            comment.Comment_User = User.objects.get(id=request.user.id)
            forma.save()
    return redirect("/video/get/" + str(video_id) + "/")


def Registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = authenticate(
                username=new_user_form.cleaned_data['username'],
                password=new_user_form.cleaned_data['password2']
            )
            login(request, new_user)
            return redirect("/video/all/")
        else:
            args["form"] = new_user_form
            args["errorlist"] = "The two password fields didn't match"
    return render(request, "Registration.html", args)


def Login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/video/all/")
        else:
            args["login_error"] = "User not found"
            return render(request, "Login.html", args)
    else:
        return render(request, "Login.html", args)


def Logout(request):
    logout(request)
    return redirect('video_all_url')


# Create your views here.
