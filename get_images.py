import requests
import random
from PIL import Image
from io import BytesIO
from collage import create_collage

#Returns a list of image objects
def search_images(search_term):
    my_key = 'GNav5YztHDAun6NxWxjBVfCL0NbaZv2qkHvXLpZQK8AeZ0M8OuLWKikV'

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": my_key
    }

    random_page = random.randint(1,75) #Randomly determines the page number for search
    image_count = 15 #Determines how many images to retrieve
    
    params = {
        "query": search_term,
        "per_page": image_count, 
        "page": random_page
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        #Get image information
        photos = data['photos']
        random.shuffle(photos) #Shuffles the list of pictures

        #Specifies the number of photos to get
        num_images = 4
        #Grabs specified number of image urls
        image_urls = [photo['src']['large'] for photo in photos[:num_images]]
        
        #Converts the image urls to image objects
        images = [Image.open(BytesIO(requests.get(url).content)) for url in image_urls]
        
        #Collects the image info into a dictionary
        image_info_list = [
        {'image': img,
         'width': img.width,
         'height': img.height}
        for img in images
    ]
        
        #Calls a function to create a collage out of the three images
        collage_image = create_collage(search_term, image_info_list)
        
        
        return collage_image #Returns the image collage


    except Exception as e:
        print(f'An error has occured: {e}')



def main():
    search_images('nature')

if __name__ == "__main__":
    main()