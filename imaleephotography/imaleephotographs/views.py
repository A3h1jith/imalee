from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Gallery, Category, Image,Messages


# Create your views here.
def home(request):
    gallery = Image.objects.all()
    return  render(request,'index.html',{'gallery':gallery})

def about(request):
    # review =Review.objects.all()
    return render(request,'about.html')

def services(request):
    return  render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        messages=Messages(name=name,email=email,subject=subject,message=message)
        messages.save()
        from django.contrib import messages
        messages.success(request, 'Message sent successfully')
    return render(request,'contact.html')


# def gallery(request):
#     gallery = Gallery.objects.all()
#     return  render(request,'gallery.html',{'gallery':gallery})

def allImgCat(request,c_slug=None):
    c_page = None
    photo_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        photo_list = Image.objects.all().filter(Category=c_page)
    else:
        photo_list = Image.objects.all().filter()
    paginator = Paginator(photo_list,8)
    try:
        page = int(request.GET.get('page',1))
    except:
        page = 1
    try:
        photos = paginator.page(page)
    except (EmptyPage,InvalidPage):
        photos = paginator.page(paginator.num_pages)
    return render(request,'gallery.html',{'category':c_page,'photos':photos})

def ImgDetail(request,c_slug,img_slug):
    try:
        photo = Image.objects.get(Category__slug=c_slug,slug=img_slug)
    except Exception as e:
        raise e
    return render(request,'gallery-single.html',{'photo':photo})



