import requests
import random
from PIL import Image
from io import BytesIO

#Returns a list of image objects
def search_images(search_term):
    my_key = 'GNav5YztHDAun6NxWxjBVfCL0NbaZv2qkHvXLpZQK8AeZ0M8OuLWKikV'

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": my_key
    }

    random_page = random.randint(1,50)
    params = {
        "query": search_term,
        "per_page": 10, #Determines how many images to retrieve
        "page": random_page
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        #Get image information
        photo = data['photos']

        random_photo = random.choice(photo)

        image_response = requests.get(random_photo['src']['original'])
        image = Image.open(BytesIO(image_response.content))
        return image


    except Exception as e:
        print(f'An error has occured: {e}')


def main():
    pass

if __name__ == "__main__":
    main()