from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from info import views as info_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
    # Logout should redirect to login page instead of rendering a template
     # Use a simple logout view that accepts GET and redirects to login
     path('accounts/logout/', info_views.logout_redirect, name='logout'),
]
