from bs4 import BeautifulSoup
import requests

# the url and headers for the amazon product page
url = "https://www.amazon.com.mx/King-6-8Kg-Chocolate-Ronnie-Coleman/dp/B010V80O6U/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3HU8WC4XGEE1P&dib=eyJ2IjoiMSJ9.8zJrbK9-7ryYD1sv6SuB-9kebI1sRsdJjXV1x4TjWurcsuheh1yedYrLZ97__19cY0TZVYDAZT4f6CyDRZFnQm6maMvUhjmJgQc-exONqiJoNdo5s-z8eGnG_oW117HfODYQBkkwA6x7XienYSH-VQRoe5eRAjGv1dBo18eOWoZJKVU8a-mf3o3oDWMUfkud6w2Kb11BHRVnVwfBPp7VL_lqMic8wPUNShVbJqOqY1_IMCLxw_vXsjwIwYmr742mKfK4jHzQQ4BhDdEbQ43-viDFcNJUJ3VgjKp7WaFJCs4.6r3RdcQgrL_awo17kcdqz-ZP9eP4W6equPef6J1Dmlo&dib_tag=se&keywords=king+mass&qid=1709600277&sprefix=king+mass+%2Caps%2C131&sr=8-1&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',   # user-agent of the browser
    'Accept-Language': 'en-US,en;q=0.9'  # preferred languages
}

# sending the http request and creating the beautifulsoup object
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# extract the whole part of the price using the class name 'a-price-whole'
price_whole_element = soup.find("span", class_="a-price-whole")
if price_whole_element:
    price_whole = price_whole_element.get_text(strip=True)  # get text without any child tags and trim whitespace
    print(f"Price whole is: {price_whole}")
else:
    print("Price whole element not found.")  # in case the price element is not found on the page

# extract the decimal part of the price using the class name 'a-price-decimal'
price_decimal_element = soup.find("span", class_="a-price-decimal")
if price_decimal_element:
    price_decimal = price_decimal_element.get_text(strip=True)
    print(f"Price decimal is: {price_decimal}")
else:
    print("Price decimal element not found.")  # in case the price decimal element is not found on the page
