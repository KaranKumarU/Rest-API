import requests
import time


def test_public_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Response Content:")
        print(response.text)

    except requests.RequestException as e:
        print(f"Error: {e}")


# Example
url_to_test = "https://openai.com/"

while True:
    test_public_url(url_to_test)
    time.sleep(900)
