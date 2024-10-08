import asyncio
import aiohttp
from contextlib import asynccontextmanager

# Custom metaclass to automatically register classes
class AutoRegisterMeta(type):
    _registry = {}

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        cls._registry[name] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return cls._registry

# Base class using the metaclass
class AutoRegisterClass(metaclass=AutoRegisterMeta):
    pass

# Example class registered automatically
class MyScraper(AutoRegisterClass):
    def __init__(self, url):
        self.url = url

    async def fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.text()

# Context manager to manage async sessions
@asynccontextmanager
async def web_scraper(url):
    scraper = MyScraper(url)
    try:
        yield scraper
    finally:
        print("Session closed.")

# Async generator to handle multiple scraping tasks
async def async_scraper(urls):
    async for url in async_url_generator(urls):
        async with web_scraper(url) as scraper:
            data = await scraper.fetch()
            print(f"Data fetched from {url[:30]}: {data[:50]}...")

# Generator function for URLs
async def async_url_generator(urls):
    for url in urls:
        await asyncio.sleep(0.1)  # Simulate some delay
        yield url

# Function to run the async scraper
async def run_scraper():
    urls = [
        'https://example.com',
        'https://httpbin.org/get',
        'https://jsonplaceholder.typicode.com/posts'
    ]
    await async_scraper(urls)

# Running the async function
if __name__ == '__main__':
    asyncio.run(run_scraper())
