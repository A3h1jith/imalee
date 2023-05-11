from django.contrib import admin

# Register your models here.
from . models import Gallery,Category,Image,Messages
admin.site.register(Gallery)
admin.site.register(Messages)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'Category']
    # list_editable = ['description', 'category']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Image,ImageAdmin)
