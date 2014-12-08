# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Document, DocumentAuthor, ObservedPerson
from filebrowser.settings import ADMIN_THUMBNAIL


class DocumentAuthorAdmin(admin.ModelAdmin):
    model = DocumentAuthor

class ObservedPersonAdmin(admin.ModelAdmin):
    model = ObservedPerson

class ObservedPersonInline(admin.StackedInline):
    model = ObservedPerson


class DocumentAdmin(admin.ModelAdmin):
    """
    Admin interface for documents
    """
    model = Document
     
    def image_thumbnail(self, obj):
        #if obj.image and obj.image.filetype == "Image":
        if obj.file.filetype == "Image":
            return '<img src="%s" />' % obj.file.version_generate(ADMIN_THUMBNAIL).url
        else:
            return ""
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"
    
    def file_url(self, obj):
        return '<a href="%s">%s</a>' % (obj.file.url, obj.file.filename) 
    file_url.allow_tags = True
    file_url.short_description = 'Lien fichier'

    def observed_persons_names(self, obj):
        persons_string = ""
        for item in obj.observed_persons.values():
            persons_string += item['first_name'] + ', '
        return persons_string
    observed_persons_names.short_description = u"Personnes Observées"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'uploaded_by':
            kwargs['initial'] = request.user.id
        return super(DocumentAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    list_filter = ('author', 'doc_type', 'observed_item', 'creation_date')
    list_display = ('pk', 'doc_type', 'author', 'file_url', 'creation_date', 
                    'observed_item', 'observed_persons_names', 'image_thumbnail', 'uploaded_by')
    #search_fields = ['foreign_key__related_fieldname']
    search_fields = ['file', 'uploaded_by__username', 'doc_type', 'author__name',  
                    'observed_item', 'observed_persons__first_name']
    inlines = [
        ObservedPersonInline,
    ]

admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentAuthor, DocumentAuthorAdmin)
admin.site.register(ObservedPerson, ObservedPersonAdmin)
