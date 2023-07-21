from locust import HttpUser, task, TaskSet
from locust.clients import HttpSession


class ApplicationUser(HttpUser):
    def on_start(self):
        self.login()
        return super().on_start()
    
    def login(self):
        data = {"username": "su", "password": "password"}
        res = self.client.post("/auth/get/", data)
        self.client.headers.update({"Authorization": f"Bearer {res.json()['access']}"})
    
    @task(1)
    def dashboard(self):
        self.client.get("/api/admin/")
    
    @task(2)
    def user(self):
        self.client.get("/api/user/")
    
    @task(3)
    def department(self):
        self.client.get("/api/department/")
    
    @task(4)
    def company(self):
        self.client.get("/api/company/")
    
    @task(5)
    def employee(self):
        self.client.get("/api/employee/")
    
    @task(6)
    def employment(self):
        self.client.get("/api/employment/")
