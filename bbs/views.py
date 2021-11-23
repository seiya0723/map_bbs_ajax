from django.shortcuts import render,redirect

from django.views import View

from .models import Topic
from .forms import TopicForm

from django.http.response import JsonResponse


class BbsView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

index   = BbsView.as_view()

class MappingView(View):

    def get(self, request, *args, **kwargs):

        #辞書型のリスト型に仕立てる。
        topics  = list(Topic.objects.all().values())
    
        #contextと同じように辞書型にさせる
        json    = { "topics":topics }
        return JsonResponse(json)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)

        if form.is_valid():
            print("OK")
            form.save()

        return redirect("bbs:index")

mapping = MappingView.as_view()


