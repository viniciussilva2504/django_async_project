from django.test import AsyncTestCase
from django.urls import reverse
from httpx import AsyncClient

class AsyncViewTests(AsyncTestCase):
    async def test_async_view(self):
        async with AsyncClient() as client:
            response = await client.get(reverse('async_view_name'))  # Replace 'async_view_name' with the actual name of your async view
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Non-blocking HTTP request")