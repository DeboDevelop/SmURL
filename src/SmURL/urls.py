from django.contrib import admin
from django.urls import include, path

from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<str:token>', views.route, name='route'),
    path('api/', include('API.urls')),
]

