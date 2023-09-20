from django.contrib import admin
from .models import Post, Resource, Engage
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)} # new
admin.site.register(Post, PostAdmin)
admin.site.register(Resource)
admin.site.register(Engage)