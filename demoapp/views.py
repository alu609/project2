from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#创建视图函数
def index(request):
	#返回响应对象
	return HttpResponse("这是第一个子应用的视图函数功能展示")
