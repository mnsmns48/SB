import asyncio
import aiohttp
import fake_useragent
import requests

user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
link = 'https://jacochef.ru/api/site/test_app.php'


# link_token = 'https://shop.vsk.ru/ajax/auth/checkPostSms/'


async def query(link_: str, headers_: dict, data: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=link_,
                                headers=headers_,
                                data=data) as response:
            print('url:', link_)
            print('headers:', headers_)
            print('data:', data)
            print(response.text)
            await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(coro=query(link_=link,
                                          headers_=headers,
                                          data={'phoneNumber': '+79786776533'}
                                          ),
                               name='Task1')

    await task


if __name__ == '__main__':
    # asyncio.run(main())
    response = requests.post(link, headers=headers,
                             data={"number": "89784024301", "token": "", "type": "create_profile"})
    print(response.text)
