from PIL import Image

#Takes the emotion and list of image objects
def create_collage(emotion, image_info_list):
    
    total_width = 0
    total_height = 0
    
    #Gets the sum of width and height of all the images
    for img in image_info_list:
        total_width += img['width']
        total_height += img['height']
    
    #Calls a function to retrieve the background color
    background_color = get_background_color(emotion)

    #Creates an image to act as a background for the collage (ADJUST DIMENSIONS)
    collage_background = Image.new('RGB', (total_width, total_height), background_color)
    
    return collage_background

#Function to get the background color based off of the emotion
def get_background_color(emotion):
    
    if emotion: #Place holder code for emotion background colors
        background_color = (255,255,255)
    
    return background_color

def main():
    pass

if __name__ == "__main__":
    main()