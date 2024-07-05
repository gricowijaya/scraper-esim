from requests_html import HTMLSession
import csv

def scrape_digi_travel_esim_instan():
	session = HTMLSession()

	url = "https://digitravel.store/esim-instan/"

	try:
		response = session.get(url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")

		response.html.render(sleep=5, keep_page=True, scrolldown=2)

		products = response.html.find('.product-content')
		for product in products:
			name = product.find('.caption .name a', first=True).text
			price = product.find('.price-wrapper .woocommerce-Price-amount bdi', first=True).text
			print(f"Name: {name}\nPrice: {price}\n")

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)
	finally:
		session.close()
		print("session closed scraping success")
