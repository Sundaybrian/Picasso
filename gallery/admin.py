from django.contrib import admin
from .models import Location,Category,Image,tags,Photographer

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Photographer)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)

