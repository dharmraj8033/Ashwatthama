import httpx

class Authentication:
    def __init__(self, login_url, credentials):
        self.login_url = login_url
        self.credentials = credentials
        self.session = httpx.Client()

    def login(self):
        response = self.session.post(self.login_url, data=self.credentials)
        return response.status_code == 200

    def get_authenticated_session(self):
        return self.session