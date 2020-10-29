import browser, json, hashlib

b = browser.Browser()

url_list = [
	{
		'url': 'https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080,RTX%203070&manufacturer=NVIDIA&gpu_filter=RTX%203090~0,RTX%203080~1,RTX%203070~0,RTX%202080%20Ti~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20SUPER~0,GTX%201650~0',
		'css_selector': 'div.NVGFT080',
	},
	{
		'url': 'https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080,RTX%203070&manufacturer=NVIDIA&gpu_filter=RTX%203090~1,RTX%203080~1,RTX%203070~1,RTX%202080%20Ti~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20SUPER~0,GTX%201650~0',
		'css_selector': 'div.NVGFT070',
	}
]

json_dict = {}

for url in url_list:
	m = hashlib.md5(url['url'].encode('utf-8'))
	b.browser.get(url['url'])
	element = b.browser.find_element_by_css_selector(url['css_selector'])
	element_html = element.get_attribute('innerHTML')
	json_dict[m.hexdigest()]=hashlib.md5(element_html.encode('utf-8')).hexdigest()
	with open('data.txt') as json_file:
		data = json.load(json_file)
		try:
			if data[m.hexdigest()] != json_dict[m.hexdigest()]:
				print('Website (%s) has changed!' % url['url'])
		except:
			print("URL: %s not in file!" % url['url'])
			pass

with open('data.txt', 'w') as outfile:
	json.dump(json_dict, outfile)



