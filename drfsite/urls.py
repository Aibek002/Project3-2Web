from django.contrib import admin
from django.urls import path, include

from women.views import *

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    path('', home, name='home'),
    path('addpage/', addpage, name='add_page'),
    path("upload", entry, name='addbeast'),
    path('/<slug:post_slug>/', show_post, name='post'),
    path('admin/', admin.site.urls),
    path('women/', WomenAPIList.as_view()),
    path('register',registerPage,name='register'),
    path('login',loginPage,name='login'),
    path('logout',logout,name='logout'),
    path('<int:pk>/update', update.as_view(), name='update'),
    path('<slug:slug>/',delete,name='delete'),
    path('women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]
