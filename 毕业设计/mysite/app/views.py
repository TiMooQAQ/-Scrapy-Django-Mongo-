from django.shortcuts import render
from .models import tianqi
# Create your views here.
def weather_list(request):
    context = {}
    context['weather'] =  tianqi.objects.all()#模板语法中对象
    return render(request,'1.html',context)#将返回的request，通过模板语法载入1.html

def weather_detail(request,city):
    try:
        context = {}
        context['weather'] =  tianqi.objects.get(city=city)#模板语法中对象
        return render(request,'weather.html',context)#将返回的request，通过模板语法载入weather.html
    except tianqi.DoesNotExist:
        return render(request,'404.html')#如果url没有这个地址就会返回404这页面
