from django.shortcuts import render
from jobsApp.models import *
import os,os.path

# Create your views here.
def index(request):
    return render(request,'jobsApp/index.html')


def jobs(request):
    area = ['Hyderabad','Pune','Delhi']
    area_msg = ' Jobs Info'
    path = str(request.path_info)
    if 'hydjobs' in path:
        area_msg = area[0] + area_msg
        hyd_jobs =  hydjobs.objects.order_by('date')
        img_1 = 'images/hyd_images/hyd_1.jpg'
        img_2 = 'images/hyd_images/hyd_2.jpg'
        img_3 = 'images/hyd_images/hyd_3.jpg'
        hyd_dict = {'jobs_list':hyd_jobs,
                    'area_msg':area_msg,
                     'img_1':img_1,
                     'img_2':img_2,
                     'img_3':img_3,}
        return render(request,'jobsApp/jobs.html',context = hyd_dict)

    if 'punejobs' in path:
        area_msg = area[1] + area_msg
        pune_jobs =  punejobs.objects.order_by('date')
        img_1 = 'images/pune_images/pune_1.jpg'
        img_2 = 'images/pune_images/pune_2.jpg'
        img_3 = 'images/pune_images/pune_3.jpg'
        pune_dict = {'jobs_list':pune_jobs,
                    'area_msg':area_msg,
                     'img_1':img_1,
                     'img_2':img_2,
                     'img_3':img_3,}
        return render(request,'jobsApp/jobs.html',context = pune_dict)

    if 'delhijobs' in path:
        area_msg = area[2] + area_msg
        delhi_jobs =  delhijobs.objects.order_by('date')
        img_1 = 'images/delhi_images/delhi_1.jfif'
        img_2 = 'images/delhi_images/delhi_2.jfif'
        img_3 = 'images/delhi_images/delhi_3.jpg'
        delhi_dict = {'jobs_list':delhi_jobs,
                    'area_msg':area_msg,
                     'img_1':img_1,
                     'img_2':img_2,
                     'img_3':img_3,}
        return render(request,'jobsApp/jobs.html',context = delhi_dict)

'''
def hyd_jobs(request):
    jobs_list = hydjobs.objects.order_by('date')
    area_msg = 'Hyderabad Jobs Info'
    img_1 = 'images/hyd_images/hyd_1.jpg'
    img_2 = 'images/hyd_images/hyd_2.jpg'
    img_3 = 'images/hyd_images/hyd_3.jpg'
    hyd_dict = {'jobs_list':jobs_list,
                'area_msg':area_msg,
                 'img_1':img_1,
                 'img_2':img_2,
                 'img_3':img_3,}
    print(request.path_info)
    return render(request,'jobsApp/jobs.html',context = hyd_dict)

def pune_jobs(request):
    jobs_list = punejobs.objects.order_by('date')
    area_msg = 'Pune Jobs Info'
    img_1 = 'images/pune_images/pune_1.jpg'
    img_2 = 'images/pune_images/pune_2.jpg'
    img_3 = 'images/pune_images/pune_3.jpg'
    pune_dict = {'jobs_list':jobs_list,
                'area_msg':area_msg,
                 'img_1':img_1,
                 'img_2':img_2,
                 'img_3':img_3,}
    return render(request,'jobsApp/jobs.html',context = pune_dict)

def delhi_jobs(request):
        jobs_list = delhijobs.objects.order_by('date')
        area_msg = 'Delhi Jobs Info'
        img_1 = 'images/delhi_images/delhi_1.jfif'
        img_2 = 'images/delhi_images/delhi_2.jfif'
        img_3 = 'images/delhi_images/delhi_3.jpg'
        delhi_dict = {'jobs_list':jobs_list,
                    'area_msg':area_msg,
                     'img_1':img_1,
                     'img_2':img_2,
                     'img_3':img_3,}
        return render(request,'jobsApp/jobs.html',context = delhi_dict)
'''
