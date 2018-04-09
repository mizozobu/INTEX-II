from django.test import TestCase
from account import models as amod
from django.contrib.auth.models import Group, Permission, ContentType


class UserModelTest(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        # read from json
        self.u1 = amod.User.objects.get(email='hamc.m.so.j12@gmail.com')

    def test_user_create_save_load(self):
        '''Tests round trip of User model data to/from database'''
        u2 = amod.User.objects.get(email='hamc.m.so.j12@gmail.com')
        self.assertEquals(self.u1.first_name, u2.first_name)
        self.assertEquals(self.u1.last_name, u2.last_name)
        self.assertEquals(self.u1.email, u2.email)
        self.assertEquals(self.u1.city, u2.city)
        self.assertEquals(self.u1.state, u2.state)
        self.assertEquals(self.u1.zip, u2.zip)
        self.assertTrue(u2.check_password("nanakuni0914"))

    def test_add_groups_add_permissions(self):
        '''Tests adding a group to a user and add a permission to the group'''
        p1 = Permission()
        p1.name = 'Can Create'
        p1.codename = 'can_create'
        p1.content_type = ContentType.objects.get(id=1)
        p1.save()

        g1 = Group()
        g1.name = "employee"
        g1.save()
        g1.permissions.add(p1)
        g1.save()

        p2 = Permission()
        p2.name = 'Can Delete'
        p2.codename = 'can_delete'
        p2.content_type = ContentType.objects.get(id=1)
        p2.save()

        g2 = Group()
        g2.name = "manager"
        g2.save()
        g2.permissions.add(p2)
        g2.save()

        self.u1.groups.add(g1)
        self.u1.groups.add(g2)
        self.assertTrue(self.u1.groups.filter(name="employee"))
        self.assertTrue(self.u1.groups.filter(name="manager"))
        self.assertTrue(self.u1.has_perm(p1.name))
        self.assertTrue(self.u1.has_perm(p2.name))

    def test_add_permissions_to_user(self):
        '''Tests adding a permission to a user'''
        p1 = Permission()
        p1.name = 'Can Create'
        p1.codename = 'can_create'
        p1.content_type = ContentType.objects.get(id=1)
        p1.save()

        p2 = Permission()
        p2.name = 'Can Delete'
        p2.codename = 'can_delete'
        p2.content_type = ContentType.objects.get(id=1)
        p2.save()

        self.u1.user_permissions.add(p1)
        self.u1.user_permissions.add(p2)

        self.assertTrue(self.u1.has_perm(p1.name))
        self.assertTrue(self.u1.has_perm(p2.name))

    def test_user_password(self):
        '''Tests user password'''
        self.assertTrue(self.u1.check_password("nanakuni0914"))

    def test_change_user_info(self):
        '''Tests changing user info'''
        self.u1.first_name = "Jocab"
        self.u1.last_name = "Lee"
        self.u1.email = "JLEE@gmail.com"
        self.u1.city = "San Francisco"
        self.u1.state = "CA"
        self.u1.zip = "99999"
        self.u1.set_password("password")
        self.u1.save()

        self.assertEquals(self.u1.first_name, "Jocab")
        self.assertEquals(self.u1.last_name, "Lee")
        self.assertEquals(self.u1.email, "JLEE@gmail.com")
        self.assertEquals(self.u1.city, "San Francisco")
        self.assertEquals(self.u1.state, "CA")
        self.assertEquals(self.u1.zip, "99999")
        self.assertTrue(self.u1.check_password("password"))
