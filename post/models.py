from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.


class User(models.Model):
    class Meta:
        verbose_name = 'کاربر وبلاگ'
        verbose_name_plural = 'کاربرهای وبلاگ'
    username = models.CharField(verbose_name='نام کاربری', max_length=20, unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=100)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=100)
    email = models.EmailField(verbose_name='پست الکتریکی', unique=True)
    # phone = PhoneField(verbose_name='تلفن همراه', blank=True,
    #                    help_text='Contact Phone Number!', unique=True)
    phone = models.CharField(verbose_name='تلفن همراه', blank=True, unique=True, max_length=15)
    image = models.ImageField(verbose_name='تصویر', upload_to='img/users/', null=True, blank=True)
    start_time = models.DateField(verbose_name='زمان ثبت نام', blank=True)
    login_time = models.DateField(verbose_name='زمان آخرین بازدید', blank=True)
    password = models.CharField(verbose_name='کلمه عبور', max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class FatherCat(models.Model):
    class Meta:
        verbose_name = 'بالا دسته بندی'
        verbose_name_plural = 'بالا دسته بندی ها'

    name = models.CharField(verbose_name='بالادسته', max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    name = models.CharField(verbose_name='دسته', max_length=100, unique=True)
    fatherCat = models.ForeignKey(FatherCat, on_delete=models.CASCADE, verbose_name='بالا دسته بندی')

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    name = models.CharField(verbose_name='چسب', max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    title = models.CharField(verbose_name='عنوان', max_length=100)
    text = models.TextField(verbose_name='متن', max_length=1000)
    user = models.ForeignKey(User, verbose_name='کاربر',
                             on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField(verbose_name='تصویر', upload_to='img/posts/')
    category = models.ForeignKey(
        Category, verbose_name='دسته بندی', on_delete=models.CASCADE)
    comment = models.ManyToManyField(User, through='Comment', through_fields=(
        'post', 'user'), verbose_name='نظر', default=None, related_name='post_comment')
    like_dislike = models.ManyToManyField(User, through='Like_Post', through_fields=(
        'post', 'user'), verbose_name='پسند', default=None, related_name='post_selection')
    tag = models.ManyToManyField(Tag, verbose_name='برچسب')
    approving = models.BooleanField(verbose_name='تایید پست', default=False)
    activate = models.BooleanField(verbose_name='قابلیت نمایش', default=True)
    pub_date = models.DateTimeField(verbose_name='زمان انتشار', blank=True, default=timezone.now)

    def __str__(self):
        return self.title


class Like_Post(models.Model):
    class Meta:
        verbose_name = 'پسند پست'
        verbose_name_plural = 'پسند پست ها'
        # unique_together = ['user', 'post']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    selection = models.BooleanField(verbose_name='پسند', null=True, blank=True)

    def __str__(self):
        return self.user + ' ' + self.post


class Comment(models.Model):
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    text = models.CharField(verbose_name='متن', max_length=500)
    approving = models.BooleanField(verbose_name='تایید پست', default=False)
    post = models.ForeignKey(Post, verbose_name='پست',
                             on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, verbose_name='کاربر',
                             on_delete=models.CASCADE, related_name='comment_user')
    like_dislike = models.ManyToManyField(User, through='Like_Comment', through_fields=(
        'comment', 'user'), verbose_name='پسند', default=None, related_name='selection')

    def __str__(self):
        return self.text[:50] + '...'


class Like_Comment(models.Model):
    class Meta:
        verbose_name = 'پسند نظر'
        verbose_name_plural = 'پسند نظر ها'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    selection = models.BooleanField(verbose_name='پسند', null=True, blank=True)

    def __str__(self):
        return self.user + ' ' + self.comment








# class Like(models.Model):
#     is_like = models.BooleanField(verbose_name='پسند', blank=True, null=True)
#     user = models.ForeignKey(verbose_name='کاربر', on_delete=models.CASCADE)
#     post = models.ForeignKey(verbose_name='پست', on_delete=models.CASCADE)
# 
    # def __str__(self):
    #     return
