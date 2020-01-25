from django.shortcuts import render
from .models import Videos
from accounts.models import UserProfileInfo
from .forms import VideosToUploadForm

def index_landing_page(request):
    return render(request,'pages/index_landing_page.html')


def homepage(request):
    videos = Videos.objects.filter(active_flag=True).order_by('-created_date')
    print("hey")
    if request.user.is_authenticated:
        print("user autheticated")
        try:
            account = UserProfileInfo.objects.get(user=request.user)
            print(account.full_name)
        except:
            account = "NULL"
    else:
        account = "NULL"
    context = {
        'videos': videos,
        'account': account
    }
    return render(request,'pages/homepage.html',context)

def upload_videos(request):
    if request.method == 'POST':
        form = VideosToUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'pages/upload_videos_page.html',{'video_upload_form':VideosToUploadForm()})
        else:
            return render(request,'pages/upload_videos_page.html',{'video_upload_form':form})
    else:
        return render(request,'pages/upload_videos_page.html',{'video_upload_form':VideosToUploadForm()})