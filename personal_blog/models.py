from django.db import models#引入数据库模型定义模块
from django.utils import timezone#引入时区模块
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_id = models.CharField(primary_key=True, max_length=200)
    blog_title = models.CharField(max_length=500)
    blog_text = models.TextField()#文本类型，无最大长度
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)#时间类型
    author = models.ForeignKey(User, on_delete=models.CharField)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.blog_title


"""
1、models.AutoField　　自增列 = int(11)
　　如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、models.CharField　　字符串字段
　　必须 max_length 参数
3、models.BooleanField　　布尔类型=tinyint(1)
　　不能为空，Blank=True
4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar
　　继承CharField，所以必须 max_lenght 参数
5、models.DateField　　日期类型 date
　　对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、models.DateTimeField　　日期类型 datetime
　　同DateField的参数
7、models.Decimal　　十进制小数类型 = decimal
　　必须指定整数位max_digits和小数位decimal_places
8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar
　　对字符串进行正则表达式
9、models.FloatField　　浮点类型 = double
10、models.IntegerField　　整形
11、models.BigIntegerField　　长整形
　　integer_field_ranges = {
　　　　'SmallIntegerField': (-32768, 32767),
　　　　'IntegerField': (-2147483648, 2147483647),
　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
　　　　'PositiveSmallIntegerField': (0, 32767),
　　　　'PositiveIntegerField': (0, 2147483647),
　　}
12、models.IPAddressField　　字符串类型（ip4正则表达式）
13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
　　参数protocol可以是：both、ipv4、ipv6
　　验证时，会根据设置报错
14、models.NullBooleanField　　允许为空的布尔类型
15、models.PositiveIntegerFiel　　正Integer
16、models.PositiveSmallIntegerField　　正smallInteger
17、models.SlugField　　减号、下划线、字母、数字
18、models.SmallIntegerField　　数字
　　数据库中的字段有：tinyint、smallint、int、bigint
19、models.TextField　　字符串=longtext
20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]
21、models.URLField　　字符串，地址正则表达式
22、models.BinaryField　　二进制
23、models.ImageField   图片
24、models.FilePathField 文件
-----------------------------------------------------------------
1、null=True
　　数据库中字段是否可以为空
2、blank=True
　　django的 Admin 中添加数据时是否可允许空值
3、primary_key = False
　　主键，对AutoField设置主键后，就会代替原来的自增 id 列
4、auto_now 和 auto_now_add
　　auto_now   自动创建---无论添加或修改，都是当前操作的时间
　　auto_now_add  自动创建---永远是创建时的时间
5、choices
GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
gender = models.CharField(max_length=2,choices = GENDER_CHOICE)
6、max_length   最大长度
7、default　　默认值
8、verbose_name　　Admin中字段的显示名称
9、name|db_column　　数据库中的字段名称
10、unique=True　　不允许重复
11、db_index = True　　数据库索引
12、editable=True　　在Admin里是否可编辑
13、error_messages=None　　错误提示
14、auto_created=False　　自动创建
15、help_text　　在Admin中提示帮助信息
16、validators=[]
17、upload_to   定义上传根目录
---------------------------------------------------------------------
连表结构：
一对多：models.ForeignKey(其他表)
多对多：models.ManyToManyField(其他表)
一对一：models.OneToOneField(其他表)
---------------------------------------------------------------------
# 增
#
# models.Tb1.objects.create(c1='xx', c2='oo')  增加一条数据，可以接受字典类型数据 **kwargs
# obj = models.Tb1(c1='xx', c2='oo')
# obj.save()

# 查
#
# models.Tb1.objects.get(id=123)         # 获取单条数据，不存在则报错（不建议）
# models.Tb1.objects.all()               # 获取全部
# models.Tb1.objects.filter(name='seven') # 获取指定条件的数据

# 删
#
# models.Tb1.objects.filter(name='seven').delete() # 删除指定条件的数据

# 改
# models.Tb1.objects.filter(name='seven').update(gender='0')  # 将指定条件的数据更新，均支持 **kwargs
# obj = models.Tb1.objects.get(id=1)
# obj.c1 = '111'
# obj.save() 
------------------------------------------------------------------------
    #save添加
    # obj = UserType(caption="管理员")
    # obj.save()

    # #create添加
    # UserType.objects.create(caption="普通用户")

    # #字典添加
    # user_dict = {"caption":"超级管理员"}
    # UserType.objects.create(**user_dict)
    这里用到了字典添加方法：
     # 添加字典方法一
    user_info_dict1 = {
        "user": "alex",
        "email": "alex123@163.com",
        "pwd": 123,
        "user_type":UserType.objects.get(nid=1)
    }
    UserInfo.objects.create(**user_info_dict1)

    # 添加字典方法二
    user_info_dict2 = {
        "user": "eric",
        "email": "alex123@163.com",
        "pwd": 123,
        "user_type_id": 1
    }
    UserInfo.objects.create(**user_info_dict2)  
------------------------------------------------------------------------------
查询---
使用all():
    ret = UserType.objects.all()
    print(type(ret),ret,ret.query)  
    #type(ret)是QuerySet。ret是列表里面封装每一条数据的对象。 ret.query查看SQL语句
    for item in ret:
        print(item,item.nid,item.caption)  #item是对象
使用all().values():
        ret1 = UserType.objects.all().values("nid")  #获取UserType表中nid的值
    print(type(ret1),ret1,ret1.query)  #type(ret1)是QuerySet。ret1是列表里面有字典
    for item in ret1:
        print(item,type(item))  #item是字典
        print(item["nid"])  #获取nid的值
-------------------------------------------------------------------------------
进阶查询，基于双下划线的过滤：
# 获取个数
    #
    # models.Tb1.objects.filter(name='seven').count()

    # ----大于gt，小于----
    #
    # models.Tb1.objects.filter(id__gt=1)              # 获取id大于1的值  gt=greater than
    # models.Tb1.objects.filter(id__lt=10)             # 获取id小于10的值 lt= little than
    # models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值

    #----in---
    #
    # models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
    # models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in

    #----contains----
    #
    # models.Tb1.objects.filter(name__contains="ven") 包含
    # models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
    # models.Tb1.objects.exclude(name__icontains="ven")

    # ----range----
    #
    # models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and

    # ----其他类似----
    #
    # startswith，istartswith, endswith, iendswith,

    # ----order by----
    #
    # models.Tb1.objects.filter(name='seven').order_by('id')    # asc
    # models.Tb1.objects.filter(name='seven').order_by('-id')   # desc

    # ----limit 、offset----
    #
    # models.Tb1.objects.all()[10:20]

    # ----group by----
    from django.db.models import Count, Min, Max, Sum
    # models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))#annotate()就是order_by
    # SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"
    
"""