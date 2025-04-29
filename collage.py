from PIL import Image

#Takes the emotion and list of image objects
def create_collage(emotion, image_info_list):
    
    buffer = 75

    #Calculates the dimensions for the background
    background_dimensions, row_height = get_background_dimensions(image_info_list, buffer)
    
    
    #Calls a function to retrieve the background color based on the emotion
    background_color = get_background_color(emotion)

    #Creates an image to act as a background for the collage
    collage_background = Image.new('RGB', background_dimensions, background_color)

    offset_x = buffer
    offset_y = buffer

    #Loops through the images and places them on the background
    for i, img in enumerate(image_info_list):
        copy_image(img, collage_background, offset_x, offset_y)
        offset_x += img['width'] + buffer

        if (1 + i) == (len(image_info_list)//2): #Once half the images are placed, moves to next rows
            offset_x = buffer
            offset_y += row_height + buffer
        

    
    return collage_background

#Function to calculate the optimal background size for the collage
def get_background_dimensions(img_info, padding=100):

    num_images = len(img_info) #Collects the total number of images

    #Splits the images into two rows
    half = (num_images + 1) // 2 #Rounds up for odd numbers
    top_row = img_info[:half]
    bottom_row = img_info[half:]

    #Calculates the total width of each row
    top_row_width = sum(img['width'] for img in top_row) + padding * (len(top_row) - 1)
    bottom_row_width = sum(img['width'] for img in bottom_row) + padding * (len(bottom_row) - 1)

    #Finds the image with the greatest height in each row
    top_row_height = max(img['height'] for img in top_row)
    bottom_row_height = max(img['height'] for img in bottom_row)

    #Gets the final background dimensions
    background_width = max(top_row_width, bottom_row_width) + padding * 2
    background_height = top_row_height + bottom_row_height + padding * 2

    return(background_width, background_height), top_row_height

#Function to get the background color based off of the emotion
def get_background_color(emotion):
    
    #happy, sad, neutral, mad, anxious

    if emotion.lower() == 'happy':
        background_color = (255,200,100) #Light orange
    elif emotion.lower() == 'sad':
        background_color = (100, 149, 237) #Cool blue
    elif emotion.lower() == 'angry':
        background_color = (220, 20, 60) #Crimson red
    elif emotion.lower() == 'neutral':
        background_color = (200, 200, 200) #Scandinavian prison wall
    elif emotion.lower() == 'anxious':
        background_color = 	(255, 228, 225) #Misty rosecolage.py: 
    else:
        background_color = (255, 255, 255) #White
    
    return background_color

#Function to perform the image copying
def copy_image(img, target_img, offset_x, offset_y):
    copy_img = img['image']

    target_img.paste(copy_img, (offset_x, offset_y))


def main():
    pass

if __name__ == "__main__":
    main()