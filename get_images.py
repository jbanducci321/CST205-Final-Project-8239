'''Takes a string input and returns a specified number of images, using an API, which is then passed to the
collage function and returns a collage
Worked on by: Jacob Banducci
5/1/2025'''

import requests
import random
from PIL import Image
from io import BytesIO
from collage import create_collage

#Returns a list of image objects
def search_images(search_term):
    my_key = 'IpmqoqVdVAOhRx4hemlJT50lhHjux8HY3ImCokenhmRO5gGgxqcACKGT'

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": my_key
    }

    image_count = 40 #Determines how many images to retrieve
    max_tries = 60 #Number of tries to get the images before giving up
    try_count = 0
    
    while True:
        random_page = random.randint(1,40)
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
                try_count+=1
                if try_count == max_tries:
                    search_term = 'Neutral'
                continue
            
            #Collects unique image urls to prevent duplicates
            unique_urls = []
            seen = set() #Creates a set to store urls for sorting
            for photo in photos:
                url = photo['src']['medium'] #Other image sizes: source(largest), large, medium, small
                if url not in seen: #Checks if the url isn't in the set
                    seen.add(url) #Adds url to the set
                    unique_urls.append(url) #Adds the url to the unique url list
                if len(unique_urls) == num_images:
                    break #Ends the loop once the specified number of image urls are collected
            
            
            #Converts the image urls to pil image objects
            images = [Image.open(BytesIO(requests.get(url).content)) for url in unique_urls]
            

            #Collects the image info into a dictionary
            image_info_list = [
            {'image': img, #Image object
            'width': img.width, #Image width
            'height': img.height} #Image height
            for img in images]
            
            #Compares widtdh and height to get a pictures orientation
            for img in image_info_list:
                if img['width'] > img['height']:
                    img['orientation'] = 'landscape'
                else:
                    img['orientation'] = 'portrait'
            
            #Calls a function to create a collage out of the specified number of images
            collage_image = create_collage(search_term, image_info_list)
            
            
            return collage_image, search_term #Returns the image collage


        except Exception as e:
            print(f'An error has occured: {e}')



def main():
    img = search_images('anxious')
    img.show()

if __name__ == "__main__":
    main()