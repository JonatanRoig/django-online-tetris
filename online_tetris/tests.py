import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Sesion, Castigo
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_sesion(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["puntos"] = "puntos"
    defaults["velocidad"] = "velocidad"
    defaults["ip"] = "ip"
    defaults.update(**kwargs)
    return Sesion.objects.create(**defaults)


def create_castigo(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "emisor" not in defaults:
        defaults["emisor"] = create_sesion()
    if "receptor" not in defaults:
        defaults["receptor"] = create_sesion()
    return Castigo.objects.create(**defaults)


class SesionViewTest(unittest.TestCase):
    '''
    Tests for Sesion
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sesion(self):
        url = reverse('online_tetris_sesion_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sesion(self):
        url = reverse('online_tetris_sesion_create')
        data = {
            "nombre": "nombre",
            "puntos": "puntos",
            "velocidad": "velocidad",
            "ip": "ip",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sesion(self):
        sesion = create_sesion()
        url = reverse('online_tetris_sesion_detail', args=[sesion.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sesion(self):
        sesion = create_sesion()
        data = {
            "nombre": "nombre",
            "puntos": "puntos",
            "velocidad": "velocidad",
            "ip": "ip",
        }
        url = reverse('online_tetris_sesion_update', args=[sesion.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CastigoViewTest(unittest.TestCase):
    '''
    Tests for Castigo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_castigo(self):
        url = reverse('online_tetris_castigo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_castigo(self):
        url = reverse('online_tetris_castigo_create')
        data = {
            "emisor": create_sesion().pk,
            "receptor": create_sesion().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_castigo(self):
        castigo = create_castigo()
        url = reverse('online_tetris_castigo_detail', args=[castigo.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_castigo(self):
        castigo = create_castigo()
        data = {
            "emisor": create_sesion().pk,
            "receptor": create_sesion().pk,
        }
        url = reverse('online_tetris_castigo_update', args=[castigo.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


