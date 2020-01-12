from django.shortcuts import render

def video_list(request):
    return render(request,r'videos/video_list.html')


