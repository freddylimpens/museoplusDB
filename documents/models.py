# -*- coding: utf-8 -*-

import os
import time
from hashlib import sha1

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import get_valid_filename
from django.utils.translation import ugettext as _

#from taggit.managers import TaggableManager
from filebrowser.sites import site
from filebrowser.fields import FileBrowseField

class DocumentAuthor(models.Model):
    class Meta:
        verbose_name = u"Auteur de document"
        verbose_name_plural = u"Auteurs de document"

    name = models.CharField(_(u"Nom"), max_length=50)
    first_name = models.CharField(_(u"Prénom"),max_length=250, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Document(models.Model):
    """
    A  document
    """
    TYPE_CHOICES = (
        ('PHOTO', _(u"Photo")),
        ('DESSIN', _(u"Dessin")),
        ('VIDEO', _(u"Vidéo")),
        ('EYETRACKING', _(u"Eyetracking")),
        ('OBSERVATION', _(u"Observation")),
        ('ENTRETIEN', _(u"Entretien")),
        ('RECIT', _(u"Récit rétrospectif")),
        ('SIGNALETIQUE', _(u"Fiche signalétique")),
        ('QUESTIONNAIRE', _(u"Questionnaire")),
        ('CONSENTEMENT_EYETRACKING', _(u"Consentement eyetracking")),
        ('DROIT_IMAGE', _(u"Droit à l'image")),
    )

    doc_type = models.CharField(_(u"Type de document"), max_length=30, choices=TYPE_CHOICES)
    author = models.ForeignKey(DocumentAuthor, verbose_name="Auteur", related_name='author_of')
    file = FileBrowseField(_(u"Fichier attaché"), max_length=255, 
            directory=getattr(settings, "UPLOADS_DIR"), blank=False, null=False)
    creation_date = models.DateField(_(u"Date de prise de vue ou création"), null=True, blank=True)
    uploaded_on = models.DateTimeField(_("Date envoi"), auto_now_add=True)
    #filename = models.CharField(max_length=2048, null=True, blank=True)
    observed_item = models.CharField(_(u"Nom de structure ou famille observée"),max_length=2048, null=True, blank=True)
    #observed_person = models.CharField(_(u"Personne observée (séparées par une virgule)"),max_length=2048, null=True, blank=True)
    uploaded_by = models.ForeignKey(User, verbose_name="Envoyé par", related_name='uploader_of')


class ObservedPerson(models.Model):
    class Meta:
        verbose_name = u"Personne Observée"
        verbose_name_plural = u"Personnes Observées"

    number = models.IntegerField(_(u"Référence de la personne observée"), blank=True, default=0, null=True)
    first_name = models.CharField(_(u"Prénom"),max_length=250)
    document = models.ForeignKey(Document, verbose_name=u"Personne Observée", related_name='observed_persons')

    def __unicode__(self):
        return u'%s' % (self.first_name)
