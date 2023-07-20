from django.test import TestCase, client
from django.apps import apps
from rest_framework.test import APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status

from app.models import User, Department, Company, Employee, Employment
from app.serializers import UserSerializer, DepartmentSerializer, CompanySerializer, EmployeeSerializer, EmploymentSerializer
from .factory import DataFactory


# Create your tests here.
class TestViews(TestCase, DataFactory):
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def setUp(self) -> None:
        self.create_data()
        su = User.objects.first()
        self.client = client.Client(enforce_csrf_checks=False)
        self.client.login(username="su", password="password")
        self.axios = APIClient()
        self.axios.login(username="su", password="password")
        refresh_token = TokenObtainPairSerializer.get_token(su)
        self.axios.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh_token.access_token))
        return super().setUp()
    
    def test_admin_view(self):
        self.assertEqual(self.client.get(f"/admin/").status_code, 404)
    
    def test_hidden_admin_view(self):
        self.assertLess(self.client.get(f"/hidden-admin/").status_code, 400)

    def test_user_list_view(self):
        res = self.axios.get("/api/user/")
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.data), 1)
        self.assertIn("id", res.data[0].keys())

    def test_user_create_view(self):
        sdata = {
            "role": "User",
            "first_name": "Eddie",
            "last_name": "Guerero",
            "username": "eddie",
            "email": "testuser@gmail.com",
            "password": "hello",
            "is_active": False,
            "is_superuser": False

        }
        res = self.axios.post(f"/api/user/", data=sdata)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        sdata.pop("password")
        self.assertTrue(User.objects.filter(**sdata).exists)

    def test_user_detail_view(self):
        res = self.axios.get(f"/api/user/{self.su.pk}/")
        self.assertEqual(res.status_code, 200)
        data = res.data
        self.assertIn("id", data.keys())
        self.assertEqual("su", data["username"])
        self.assertNotIn("password", data.keys())

    def test_user_update_view(self):
        serialized_su = UserSerializer(instance=self.su)
        sdata = dict(serialized_su.data)
        sdata["last_name"] = "Newlast"
        sdata["password"] = "password"
        sdata.pop("last_login")
        res = self.axios.put(f"/api/user/{self.su.pk}/", data=sdata)
        self.assertEqual(res.status_code, 200)
        self.su.refresh_from_db()
        self.assertTrue(self.su.check_password(sdata["password"]))
        self.assertEqual(self.su.last_name, sdata["last_name"])

    def test_user_delete_view(self):
        res = self.axios.delete(f"/api/user/{self.u2.pk}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_department_list_view(self):
        res = self.axios.get("/api/department/")
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.data), 1)
        self.assertIn("id", res.data[0].keys())

    def test_department_create_view(self):
        sdata = {
            "name": "New Dep"
        }
        res = self.axios.post(f"/api/department/", data=sdata)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Department.objects.filter(**sdata).exists)

    def test_department_detail_view(self):
        res = self.axios.get(f"/api/department/{self.ad_dep.pk}/")
        self.assertEqual(res.status_code, 200)
        data = res.data
        self.assertIn("id", data.keys())
        self.assertEqual(self.ad_dep.name, data["name"])

    def test_department_update_view(self):
        serialized_su = DepartmentSerializer(instance=self.ad_dep)
        sdata = dict(serialized_su.data)
        old_name = self.ad_dep.name
        sdata["name"] = "Administration"
        res = self.axios.put(f"/api/department/{self.ad_dep.pk}/", data=sdata)
        self.assertEqual(res.status_code, 200)
        self.ad_dep.refresh_from_db()
        self.assertNotEqual(self.ad_dep, old_name)

    def test_department_delete_view(self):
        res = self.axios.delete(f"/api/department/{self.un_dep.pk}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)