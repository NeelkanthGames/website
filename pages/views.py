from django.shortcuts import render
from django.forms import modelformset_factory

from .models import Videos, CurrentProject, CurrentProjectImages
from accounts.models import UserProfileInfo
from .forms import VideosToUploadForm, CurrentProjectForm, CurrentProjectImageForm


def index_landing_page(request):
    return render(request,'pages/index_landing_page.html')


def homepage(request):
    currentProject = CurrentProject.objects.get()
    currentProjectImages = CurrentProjectImages.objects.filter(title=currentProject)
    videos = Videos.objects.filter(active_flag=True).order_by('-created_date')
    if request.user.is_authenticated:
        try:
            account = UserProfileInfo.objects.get(user=request.user)
            print(account.full_name)
        except:
            account = "NULL"
    else:
        account = "NULL"
    context = {
        'currentProject': currentProject,
        'currentProjectImages': currentProjectImages,
        'videos': videos,
        'account': account,
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


def upload_current_project(request):
    if request.method == 'POST':
        projectForm = CurrentProjectForm(request.POST)
        image_form = CurrentProjectImageForm(request.POST,request.FILES)
        images = request.FILES.getlist('image')
        if projectForm.is_valid() and image_form.is_valid():
            CurrentProject.objects.all().delete()
            CurrentProjectImages.objects.all().delete()
            instance = projectForm.save(commit=False)
            instance.title = request.POST.get('title')
            instance.save()
            for i in images:
                image_instance = CurrentProjectImages(image=i, title = instance)
                image_instance.save()
            return homepage(request)
        else:
            return render(request, 'pages/upload_current_project.html',
                          {'currentProjectForm': projectForm,
                           'imageForm': image_form})
    currentProject = CurrentProject.objects.get()
    return render(request, 'pages/upload_current_project.html',
                  {'currentProjectForm': CurrentProjectForm(initial={'title':currentProject.title,'desc':currentProject.desc}),
                   'imageForm': CurrentProjectImageForm()}
                  )
