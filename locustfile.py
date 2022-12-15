from locust import HttpUser
from locust import task


class CheckUser(HttpUser):
    @task
    def get_users(self):
        self.client.get('/auth/users')
        self.client.get('/auth/users/1')
