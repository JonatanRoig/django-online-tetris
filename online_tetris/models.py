from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Sesion(models.Model):

    # Fields
    nombre = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    puntos = models.IntegerField(default=0)
    velocidad = models.IntegerField(default=3)
    ip = models.GenericIPAddressField(blank=True,null=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('online_tetris_sesion_detail', args=(self.slug,))

    def augmentar_velocidad(self):

        if self.velocidad < 8:
            self.velocidad += 1


    def reducir_velocidad(self):

        if self.velocidad > 1:
            self.velocidad -= 1


    def get_update_url(self):
        return reverse('online_tetris_sesion_update', args=(self.slug,))


class Castigo(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='emisor', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    emisor = models.ForeignKey('online_tetris.Sesion', related_name="emisor")
    receptor = models.ForeignKey('online_tetris.Sesion', related_name="receptor")

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('online_tetris_castigo_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('online_tetris_castigo_update', args=(self.slug,))


