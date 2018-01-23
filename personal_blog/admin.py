from django.contrib import admin
from .models import Blog

# Register your models here.
admin.site.register(Blog)#将博客模型注册到后台，使可以在后台进行控制

