import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def time_counter():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(time_counter())
    return HttpResponse("Non-blocking time counter started")

def sync_view(request):
    for num in range(1, 6):
        sleep(1)
        print(num)
    return HttpResponse("Blocking time counter finished")