from django.contrib import admin
from .models import Post, Like_Post, Dislike_Post, Comment, Like_Comment, Dislike_Comment, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'approving', 'activate')
    list_filter = ('user',)
    actions = ('make_approved', 'make_activate')

    def make_approved(self, request, queryset):
        n = queryset.update(approving=True)
        self. message_user(request, f'{n} پست تایید شد')
    make_approved.short_description = 'تایید پست های انتخاب شده'

    def make_activate(self, request, queryset):
        n = queryset.update(activate=True)
        self.message_user(request, f'{n} پست قابل نمایش شد')
    make_activate.short_description = 'قابل نمایش کردن پست های انتخاب شده'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_fcat', 'fatherCat')
    actions = ('update_to_fcat', 'update_to_cat')

    def update_to_fcat(self, request, queryset):
        n = queryset.update(is_fcat=True)
        self.message_user(request, f'{n} پست، بالا دسته بندی شد')
    update_to_fcat.short_description = 'تبدیل به بالا دسته بندی'

    def update_to_cat(self, request, queryset):
        n = queryset.update(is_fcat=False)
        self.message_user(request, f'{n} پست، دسته بندی شد')
    update_to_cat.short_description = 'تبدیل به دسته بندی'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'approving', 'activate')
    list_filter = ('user', 'post')
    actions = ('make_approved', 'make_activate')

    def make_approved(self, request, queryset):
        n = queryset.update(approving=True)
        self. message_user(request, f'{n} نظر تایید شد')
    make_approved.short_description = 'تایید نظرهای انتخاب شده'

    def make_activate(self, request, queryset):
        n = queryset.update(activate=True)
        self.message_user(request, f'{n} نظر قابل نمایش شد')
    make_activate.short_description = 'قابل نمایش کردن نظرهای انتخاب شده'
    

admin.site.register(Like_Post)
admin.site.register(Dislike_Post)
admin.site.register(Like_Comment)
admin.site.register(Dislike_Comment)
admin.site.register(Tag)

# Register your models here.
