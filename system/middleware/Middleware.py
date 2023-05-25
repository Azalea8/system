from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse

class MiddlewareAuth(MiddlewareMixin):

    # 排除不需要防火墙的URL, 避免一直重定向
    def process_request(self, request):
        if request.path_info in ['/login/', '/image/code/']:
            return None

        info = request.session.get('info')
        # print(info)
        if not info:
            return redirect('/login/')

        # print('M1.进来了')
        # return HttpResponse('无权访问！')



