from django.contrib import admin
from django.urls import  path,include
from users import views as user_views
import myapp.views as ma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('blog/', include('blog.urls')),
    path('getinfo/',ma.getinfo,name='getinfo')
]
