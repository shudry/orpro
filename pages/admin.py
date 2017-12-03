from django.contrib import admin
from .models import *
# Register your models here.


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)


admin.site.register(Post, TinyMCEAdmin)
admin.site.register(Offers, TinyMCEAdmin)
admin.site.register(AboutCompany, TinyMCEAdmin)
admin.site.register(Category )
admin.site.register(Subtags)
admin.site.register(Tags)
admin.site.register(MainBaner)
admin.site.register(FBlocks)
admin.site.register(LBlocks)
admin.site.register(TopOffers)
admin.site.register(Support)
admin.site.register(Personal)
admin.site.register(HeaderPhoto)
admin.site.register(Footer)
admin.site.register(Availability)
admin.site.register(Images)
admin.site.register(Publish)
admin.site.register(Reviews)