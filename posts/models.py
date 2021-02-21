from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from accounts.models import User
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


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
    fatherCat = models.ForeignKey(FatherCat, on_delete=models.CASCADE, null=True, blank=True, verbose_name='بالا دسته بندی')

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
        ordering = ('-pub_date', )
        # permission = [
        #     ("view_post_appact", "مشاهده پست های تایید شده و فعال"),
        #     ("approve_post", "تایید پست ها")
        # ]

    title = models.CharField(verbose_name='عنوان', max_length=100)
    text = models.TextField(verbose_name='متن', max_length=1000)
    user = models.ForeignKey(User, verbose_name='کاربر',
                             on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField(verbose_name='تصویر', upload_to='img/posts/', null=True, blank=True)
    category = models.ForeignKey(
        Category, verbose_name='دسته بندی', on_delete=models.CASCADE)
    user_comments = models.ManyToManyField(User, through='Comment', through_fields=(
        'post', 'user'), verbose_name='نظر', default=None, related_name='post_comment')
    user_likes = models.ManyToManyField(User, through='Like_Post', through_fields=(
        'post', 'user'), verbose_name='پسند', default=None, related_name='post_selection')
    tag = models.ManyToManyField(Tag, verbose_name='برچسب')
    approving = models.BooleanField(verbose_name='تایید پست', default=False)
    activate = models.BooleanField(verbose_name='قابلیت نمایش', default=True)
    pub_date = models.DateTimeField(verbose_name='زمان انتشار', auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.text[:30]}'


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
        # ordering = ('',)

    text = models.TextField(verbose_name='متن', max_length=500)
    approving = models.BooleanField(verbose_name='تایید پست', default=False)
    post = models.ForeignKey(Post, verbose_name='پست',
                             on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, verbose_name='کاربر',
                             on_delete=models.CASCADE, related_name='comment_user')
    like_dislike = models.ManyToManyField(User, through='Like_Comment', through_fields=(
        'comment', 'user'), verbose_name='پسند', default=None, related_name='selection')
    pub_date = models.DateTimeField(verbose_name='زمان انتشار', auto_now_add=True)

    def __str__(self):
        return self.text[:50] + '...'


class Like_Comment(models.Model):
    class Meta:
        verbose_name = 'پسند نظر'
        verbose_name_plural = 'پسند نظر ها'
        # unique_together = ['user', 'comment']
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