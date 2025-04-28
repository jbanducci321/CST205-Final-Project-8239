from PIL import Image

#Takes the emotion and list of image objects
def create_collage(emotion, image_info_list):
    
    total_width = 0
    total_height = 0
    
    #Gets the sum of width and height of all the images
    for img in image_info_list:
        total_width += img['width']
        total_height += img['height']
    
    #Calls a function to retrieve the background color based on the emotion
    background_color = get_background_color(emotion)

    #Creates an image to act as a background for the collage (ADJUST DIMENSIONS)
    collage_background = Image.new('RGB', (total_width, total_height), background_color)

    offset_x = 0
    offset_y = 0

    for img in image_info_list:
        copy_image(img, collage_background, offset_x, offset_y)
        offset_x += img['width']
        offset_y += img['height']

    
    return collage_background

#Function to get the background color based off of the emotion
def get_background_color(emotion):
    
    if emotion: #Place holder code for emotion background colors
        background_color = (255,255,255)
    
    return background_color

#Function to perform the image copying
def copy_image(img, target_img, offset_x, offset_y):
    copy_img = img['image']

    target_x = offset_x
    for source_x in range(img['width']):
        target_y = offset_y
        for source_y in range(img['height']):
            p = copy_img.getpixel((source_x, source_y))
            target_img.putpixel((target_x, target_y), p)
            target_y += 1
        target_x += 1


def main():
    pass

if __name__ == "__main__":
    main()