from django.contrib import admin
from .models import Post, Category, Comment
# from django.contrib.auth.admin import UserAdmin


    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'featured_image')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'email', 'comment_body', 'created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(CustomUser,UserAdmin)