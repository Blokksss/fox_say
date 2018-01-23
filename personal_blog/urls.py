from django.urls import path
from personal_blog import views#引入视图所在文件

urlpatterns = [
               path(r'login/', views.login, name='login'),
               path(r'blog/', views.login, name='login'),
                ]

