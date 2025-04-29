import requests
import random
from PIL import Image
from io import BytesIO
from collage import create_collage
import time #For testing

#Returns a list of image objects
def search_images(search_term):
    my_key = 'GNav5YztHDAun6NxWxjBVfCL0NbaZv2qkHvXLpZQK8AeZ0M8OuLWKikV'

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": my_key
    }

    image_count = 55 #Determines how many images to retrieve
    
    while True:
        random_page = random.randint(1,80)
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
            
            #Specifies the number of photos to be used for the collage
            num_images = 6
            
            #Makes sure that there is the minimum required amount of images
            if len(photos) < num_images:
                continue
            
            #Collects unique image urls to prevent duplicates
            unique_urls = []
            seen = set()
            for photo in photos:
                url = photo['src']['medium'] #Other image sizes: source(largest), large, medium, small
                if url not in seen: #Checks if the url isn't in the set
                    seen.add(url) #Adds url to the set
                    unique_urls.append(url) #Adds the url to the unique url list
                if len(unique_urls) == num_images:
                    break #Ends the loop once the specified number of image urls are collected
            
            #Converts the image urls to image objects
            images = [Image.open(BytesIO(requests.get(url).content)) for url in unique_urls]
            
            if __name__ == "__main__":
                for i, img in enumerate(images):
                    print(f"Image {i+1}: size = {img.width}x{img.height}")
                    #img.show()
                    #time.sleep(1)

            #Collects the image info into a dictionary
            image_info_list = [
            {'image': img, #Image object
            'width': img.width, #Image width
            'height': img.height} #Image height
            for img in images]
            
            #Calls a function to create a collage out of the specified number of images
            collage_image = create_collage(search_term, image_info_list)
            
            
            return collage_image #Returns the image collage


        except Exception as e:
            print(f'An error has occured: {e}')



def main():
    search_images('anxious')

if __name__ == "__main__":
    main()