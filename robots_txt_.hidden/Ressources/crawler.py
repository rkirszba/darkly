import sys
import asyncio
import aiohttp
import re

BASE_URL = ''
LINK_REGEX = r'href=[\'"]?([^\'" >]+)'

async def get_readme(session, url):
	try:
		async with session.get(url + 'README') as resp:
			text = await resp.text()
			if 'Tu veux de l\'aide ? Moi aussi !' not in text\
					and 'ton voisin de gauche' not in text\
					and 'ton voisin de droite' not in text\
					and 'ton voisin du dessous' not in text\
					and 'ton voisin du dessus' not in text\
					and 'Non ce n\'est toujours pas bon ...' not in text\
					and 'tu vas craquer non' not in text:
				print(url)
				print(text)
	except:
		pass

async def get_links(session, url):
	async with session.get(url) as resp:
		text = await resp.text()
		new_urls = [url + link for link in re.findall(LINK_REGEX, text) if not link.startswith('..') and link != 'README']
		return new_urls

async def explore_links(session, urls):
	tasks_readme = []
	tasks_new_urls = []
	
	for url in urls:
		tasks_readme.append(asyncio.create_task(get_readme(session, url)))
		tasks_new_urls.append(asyncio.create_task(get_links(session, url)))
	
	await asyncio.gather(*tasks_readme)
	new_urls_list = await asyncio.gather(*tasks_new_urls)
	tasks_explore_links = []
	for new_urls in new_urls_list:
		tasks_explore_links.append(asyncio.create_task(explore_links(session, new_urls)))
	await asyncio.gather(*tasks_explore_links)	


async def main():
	async with aiohttp.ClientSession() as session:
		await explore_links(session, [BASE_URL])

if __name__ == '__main__':
	BASE_URL = sys.argv[1] + '.hidden/'
	asyncio.run(main())