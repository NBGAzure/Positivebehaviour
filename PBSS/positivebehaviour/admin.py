
# Register your models here.
from django.contrib import admin

# Register your models here.
from.models import NewsletterUsers

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_added')

admin.site.register(NewsletterUsers, NewsletterAdmin)
