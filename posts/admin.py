from django.contrib import admin
from .models import Post, Like_Post, Dislike_Post, Comment, Like_Comment, Dislike_Comment, Category, FatherCat, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'approving')
    list_filter = ('user',)
    actions = ('make_approved',)

    def make_approved(self, request, queryset):
        n = queryset.update(approving=True)
        self. message_user(request, f'{n} پست تایید شد')
    make_approved.short_description = 'تایید پست های انتخاب شده'

admin.site.register(Like_Post)
admin.site.register(Dislike_Post)
admin.site.register(Comment)
admin.site.register(Like_Comment)
admin.site.register(Dislike_Comment)
admin.site.register(Category)
admin.site.register(FatherCat)
admin.site.register(Tag)

# Register your models here.
