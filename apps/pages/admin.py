from django.contrib import admin
from .models import UserPost, Comment

# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(UserPost, PostAdmin)
admin.site.register(Comment)