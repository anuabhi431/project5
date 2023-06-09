from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class getinput(View):
    def get(self,request):
        return render(request,'getinput.html')
class postinput(View):
    def get(self,request):
        return render(request,'postinput.html')
class add(View):
    def get(self,request):
        p=int(request.GET["t1"])
        q=int(request.GET["t2"])
        r=p+q
        return HttpResponse("the sum is :"+str(r))
    def post(self,request):
         x=int(request.POST["g1"])
         y=int(request.POST["g2"])
         z=x+y
         return HttpResponse("the SUM is :"+str(z))

