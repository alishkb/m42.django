from django.contrib import admin
from .models import User, Post, Like_Post, Dislike_Post, Comment, Like_Comment, Dislike_Comment, Category, FatherCat, Tag

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Like_Post)
admin.site.register(Dislike_Post)
admin.site.register(Comment)
admin.site.register(Like_Comment)
admin.site.register(Dislike_Comment)
admin.site.register(Category)
admin.site.register(FatherCat)
admin.site.register(Tag)

# Register your models here.
