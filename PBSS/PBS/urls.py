"""PBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from form_fba import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import client
from contact.views import contact
from users.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
#from fbaform.views import fbaformfunc, addBehaviour, addTrigger Updated upstream
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std/', views.std, name='std'),
    path('view/', views.view),
    path('freefbaform/', include('freefbaform.urls')),
    path('positivebehaviour/', include('positivebehaviour.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path('fbaform/', include('fbaform.urls')),
    path('freefbaform/', include('freefbaform.urls')),
    #path('userfba/', include('userfba.urls')),
    path('contact/', contact, name="contact"),
    path('client/', PostListView.as_view(), name="client"),
    path('client/<str:username>', UserPostListView.as_view(), name="user-client"),
    path('client/<int:pk>/', PostDetailView.as_view(), name="profile"),
    path('client/new/', PostCreateView.as_view(), name="client-create"),
    path('client/<int:pk>/update/', PostUpdateView.as_view(), name="client-update"),
    path('client/<int:pk>/delete/', PostDeleteView.as_view(), name="client-delete"),
    #  path('newsletter/', include('newsletter.urls')),


# fbaform url

    #path('fbaform/', fbaformfunc),
   # path('addBehaviour/', addBehaviour),
   # path('addTrigger/', addTrigger),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
