from django.contrib import admin
from news.models import New


class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


admin.site.register(New, NewAdmin)
