"""Views demonstrating async vs sync behavior in Django"""
import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def time_counter():
    """Async task that counts to 5 and makes an HTTP request"""
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

async def async_view(request):
    """Non-blocking async view that starts a background task"""
    loop = asyncio.get_event_loop()
    loop.create_task(time_counter())
    return HttpResponse("Non-blocking time counter started")

def sync_view(request):
    """Blocking sync view that counts to 5"""
    for num in range(1, 6):
        sleep(1)
        print(num)
    return HttpResponse("Blocking time counter finished")