
from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'docfile',
    )
    date_hierarchy = 'date'
    list_filter = (
        'docfile',
    )


# Register your models here.
admin.site.register(Document, DocumentAdmin)
