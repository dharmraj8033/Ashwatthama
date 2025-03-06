import httpx

class Scanner:
    def __init__(self, url, params, payload_manager, session=None):
        self.url = url
        self.params = params
        self.payload_manager = payload_manager
        self.session = session or httpx.Client()

    def run_scan(self):
        results = []
        for param in self.params:
            for payload in self.payload_manager.get_payloads("xss"):  # Example with XSS
                attack_url = f"{self.url}?{param}={payload}"
                response = self.session.get(attack_url)
                if payload in response.text:
                    results.append({
                        "param": param,
                        "payload": payload,
                        "response": response.text[:200]
                    })
        return results