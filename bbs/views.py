from django.shortcuts import render,redirect
from django.http.response import JsonResponse

from django.views import View
from .models import Topic

class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.order_by("sort")

        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect("bbs:index")

index   = IndexView.as_view()



class SortView(View):
    def post(self, request, *args, **kwargs):
    
        
        ids = request.POST.getlist("id");

        print(ids)
        print(type(ids))

        for i in range(len(ids)):
            topic       = Topic.objects.filter(id=ids[i]).first()
            topic.sort  = i
            topic.save()

    
        return JsonResponse({})


sort    = SortView.as_view()


