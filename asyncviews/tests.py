from django.test import TestCase, Client


class AsyncViewTests(TestCase):
    def test_async_view(self):
        client = Client()
        response = client.get('/async-counter/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Non-blocking time counter started")
    
    def test_sync_view(self):
        client = Client()
        response = client.get('/sync-counter/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blocking time counter finished")