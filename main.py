import asyncio

import aiohttp


async def query(link: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            print(response.status)
            print(await response.text())


async def main():
    task = asyncio.create_task(coro=query('https://www.google.com'), name='Task1')
    await task

if __name__ == '__main__':
    asyncio.run(main())
