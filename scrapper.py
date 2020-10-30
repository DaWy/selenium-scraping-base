import browser, json, hashlib, os

# This enable using Telegram.sh script (https://github.com/fabianonline/telegram.sh) 
# for sending a Telegram Notification over a Bot
# This requires the Script installed and BOT setted up correclty first.

TELEGRAM_ENABLED=False

b = browser.Browser()

url_list = [
	{
	'url': 'https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080,RTX%203070&manufacturer=NVIDIA&gpu_filter=RTX%203090~0,RTX%203080~1,RTX%203070~0,RTX%202080%20Ti~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20SUPER~0,GTX%201650~0',
	'desc': 'RTX 3080 Web NVIDIA',
	'css_selector': 'div.NVGFT080',
	},
	{
	'url': 'https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080,RTX%203070&manufacturer=NVIDIA&gpu_filter=RTX%203090~1,RTX%203080~1,RTX%203070~1,RTX%202080%20Ti~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20SUPER~0,GTX%201650~0',
	'desc': 'RTX 3070 Web NVIDIA',
	'css_selector': 'div.NVGFT070',
	}
]

json_dict = {}

for url in url_list:
	print("Scrapping: %s => %s... (selector: %s)" % (url['desc'], url['url'][8:40], url['css_selector']))
	m = hashlib.md5(url['url'].encode('utf-8'))
	
	passed = False
	while not passed:
		try:
			b.browser.get(url['url'])
			element = b.browser.find_element_by_css_selector(url['css_selector'])
			element_html = element.get_attribute('innerHTML')
			passed = True
		except:
			print("Failed to scrap! Retriying...")
			pass
	
	json_dict[m.hexdigest()]=hashlib.md5(element_html.encode('utf-8')).hexdigest()
	try:
		with open('data.txt') as json_file:
			data = json.load(json_file)
			try:
				if data[m.hexdigest()] != json_dict[m.hexdigest()]:
					print('Website (%s) has changed!' % url['url'])
					if TELEGRAM_ENABLED:
						try:
							os.system('telegram "%s changed! Checkout! => %s"' % (url['desc'], url['url']))
						except:
							print('Telegram support is not working. Checkout Telegram.sh installation!')
			except:
				print("URL: %s not in file!" % url['url'])
				pass
	except:
		print("First run! Generating data.txt...")

with open('data.txt', 'w') as outfile:
	json.dump(json_dict, outfile)



