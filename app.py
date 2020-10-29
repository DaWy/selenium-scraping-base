# This is an example of a basic app using selenium and this scrapper base!
# This files scraps google.es and save it html source code hash into a file in JSON format
# Then, every execution will compare this MD5 and printout a "website has changed" if json dict has changed

import browser, json, hashlib

b = browser.Browser()

url_list = [
	'https://google.es',
]

json_dict = {}

for url in url_list:
	m = hashlib.md5(url.encode('utf-8'))
	b.browser.get(url)
	json_dict[m.hexdigest()]=hashlib.md5(b.browser.page_source.encode('utf-8')).hexdigest()
	with open('data.txt') as json_file:
		data = json.load(json_file)
		try:
			if data[m.hexdigest()] != json_dict[m.hexdigest()]:
				print('Website (%s) has changed!' % url)
		except:
			print("URL: %s not in file!" % url)
			pass

print("Writing URL contents to data.txt")
with open('data.txt', 'w') as outfile:
	json.dump(json_dict, outfile)



