from django.urls import path
from imaleephotographs import views

app_name = 'imaleephotographs'

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    # path('gallery/',views.gallery,name='gallery'),
    path('<slug:c_slug>/', views.allImgCat, name='image_by_category'),
    path('<slug:c_slug>/<slug:img_slug>/', views.ImgDetail, name='ImgCatDetails'),



]