from locust import between
from locust import HttpUser
from locust import task


class CheckUser(HttpUser):
    host = 'http://127.0.0.1:8000'
    weight = 1
    wait_time = between(1, 5)

    def on_start(self):
        self.client.post(
            url='/auth/token', data={
                'username': 'test', 'password': 'test', 'scope': 'profile',
            },
        )

    @task(2)
    def get_profile(self):
        self.client.get('/auth/users/1')

    @task
    def get_all_users(self):
        self.client.get('/auth/users')
