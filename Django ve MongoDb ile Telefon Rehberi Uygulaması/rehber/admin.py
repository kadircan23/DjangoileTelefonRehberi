from django.contrib import admin
from .models import rehber
# Register your models here.



class RehberAdmin(admin.ModelAdmin):
        class Meta:
            model=rehber

admin.site.register(rehber,RehberAdmin)