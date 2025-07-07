from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.models import Post

# Create your views here.
def index(request : HttpRequest) -> HttpResponse:


    # qs = [
    #     {"id": 1, "title": "post #1"},
    #     {"id": 2, "title": "post #2"}
    # ]

    # db의 post로 대체
    qs = Post.objects.all()

    return render(
        request,
        "app/index.html",
        {
            "post_list" : qs
        }
    )