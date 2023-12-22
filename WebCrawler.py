import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def search_images(query):
    # Search for images using Bing Image Search (you need to get your API key)
    api_key = "YOUR_BING_API_KEY"
    endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    params = {"q": query}
    headers = {"Ocp-Apim-Subscription-Key": api_key}

    response = requests.get(endpoint, params=params, headers=headers)
    data = response.json()

    # Parse the results and extract image URLs
    image_urls = [item["contentUrl"] for item in data.get("value", [])]

    return image_urls

def display_images(image_urls):
    for url in image_urls:
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.show()
        except Exception as e:
            print(f"Error displaying image from {url}: {e}")

def main():
    query = input("Enter your search query: ")
    image_urls = search_images(query)

    if not image_urls:
        print("No images found.")
    else:
        display_images(image_urls)

if __name__ == "__main__":
    main()