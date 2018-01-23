from django.shortcuts import render_to_response
from django import forms
from .models import User
from .models import Blog

# Create your views here.


class UserInformation(forms.Form):
    username = forms.CharField(label='用户名称', max_length=300)
    password = forms.CharField(label='密码', max_length=300)
    email = forms.EmailField(label='邮箱')
    phone_number = forms.CharField(label='手机号', max_length=100)
"""
定义一个Form类，用来处理表单。其中代码意义是对表单提交数据进行校验.参数默认必填，如果要设置为选填则加上required=False
这个类定义后产生的对象是一个HTML文件对象：
>>>f = User()
>>> print f.as_ul()
<li><label for="id_subject">Subject:</label> <input type="text" name="subject" id="id_subject" /></li>
<li><label for="id_email">Email:</label> <input type="text" name="email" id="id_email" /></li>
<li><label for="id_message">Message:</label> <input type="text" name="message" id="id_message" /></li>
>>> print f.as_p()
<p><label for="id_subject">Subject:</label> <input type="text" name="subject" id="id_subject" /></p>
<p><label for="id_email">Email:</label> <input type="text" name="email" id="id_email" /></p>
<p><label for="id_message">Message:</label> <input type="text" name="message" id="id_message" /></p>
因此在HTML页面中只要将{{ f.as_ul }}放入代码就会将表单置于指定位置。
---f.is_valid用来验证表单提交的数据是否合法，若缺失数据，则is_valid返回为False
"""
"""---------------------------------------------------------------"""


class UserLogin(forms.Form):
    username = forms.CharField(label='用户名:', max_length=300)
    password = forms.CharField(label='密码', max_length=300)


def login(request):
    return render_to_response('login.html', {})


def online(request):
    return render_to_response('online.html', {})


def blog_list(request):
    blog_list_ = Blog.objects.all()
    return render_to_response('blog_list.html', context={'blog_list': blog_list_})


def blog_detail(request, blog_id):
    post = Blog.objects.get(blog_id=blog_id)
    blog_title = post.blog_title
    blog_text = post.blog_text
    create_date = post.create_date
    return render_to_response('blog_detail.html', {'blog_title': blog_title,
                                                   'blog_text': blog_text,
                                                   'create_date': create_date})

def photos(request):
    return render_to_response('photos.html', {})


def register(request):
    if request.method == 'POST':#先判断请求方式，注册请求方式必须的POST才能允许生效
        ur = UserInformation(request.POST)#使用表单POST内容创建表单实例
        if ur.is_valid():#校验实例
            User.objects.create(username=ur.username, password=ur.password,
                                email=ur.email, phone_number=ur.phone_number)
            return render_to_response('register_success.html', context={'username': ur.username})
        else:
            ur = UserInformation()
            return render_to_response('register.html', context={'ur': ur})
    else:
        ur = UserInformation()
        return render_to_response('register.html', context={'ur': ur})









