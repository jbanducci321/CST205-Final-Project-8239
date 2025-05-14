'''Collage Generator
CST-205
Takes a specified number of images and uses them to create a collage. Background color changes 
depending on the emotion that is passed
Worked on by: Jacob Banducci
5/10/2025'''

from PIL import Image
from color_pick import get_emotion_color

#Takes the emotion and list of image objects
def create_collage(emotion, image_info_list):
    
    buffer = 50

    #Calculates the dimensions for the background
    background_dimensions, row_height = get_background_dimensions(image_info_list, buffer)
    
    
    #Calls a function to retrieve the background color based on the emotion
    background_color = get_background_color(emotion)

    #Creates an image to act as a background for the collage
    collage_background = Image.new('RGB', background_dimensions, background_color)

    #Splits the image list into two rows
    half = len(image_info_list)//2
    top_row = image_info_list[:half] #Stores first half of the list
    bot_row = image_info_list[half:] #Stores second half of the list
    
    #Checks if either row has only portraits and sets the row-specific buffer sizes
    if check_all_portrait(top_row):
        top_row_buffer = int(buffer + buffer*1.6)
    else:
        top_row_buffer = buffer

    if check_all_portrait(bot_row):
        bottom_row_buffer = int(buffer + buffer*1.6)
    else:
        bottom_row_buffer = buffer

    #Initial position to place the first images
    offset_x = buffer
    offset_y = buffer - buffer//2

    #Loops through the images and places them on the background
    for i, img in enumerate(image_info_list):
        copy_image(img, collage_background, offset_x, offset_y) #Pastes the image
        
        if i < half: #Selects the buffer based on the row
            row_buffer = top_row_buffer
        else:
            row_buffer = bottom_row_buffer
        
        #Updates the x offset
        offset_x += img['width'] + row_buffer

        #Once half the images are placed, moves to next rows
        if (1 + i) == half: 
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
    
    background_color = get_emotion_color(emotion)
    #happy, sad, neutral, mad, anxious
    '''
    if emotion.lower() == 'happy':
        background_color = (255,200,100) #Light orange
    elif emotion.lower() == 'sad':
        background_color = (100, 149, 237) #Cool blue
    elif emotion.lower() == 'angry':
        background_color = (220, 20, 60) #Crimson red
    elif emotion.lower() == 'neutral':
        background_color = (200, 200, 200) #Neutral gray
    elif emotion.lower() == 'anxious':
        background_color = 	(255, 228, 225) #Misty rosecolage.py: 
    else:
        background_color = (255, 255, 255) #White'''
    
    return background_color

#Function to perform the image copying
def copy_image(img, target_img, offset_x, offset_y):
    copy_img = img['image']

    target_img.paste(copy_img, (offset_x, offset_y))

#Checks if a row of images contains only portrait images (returns a bool value)
def check_all_portrait(row):
    #Stores all the portrait images from a row into a list
    portrait_check = [img for img in row if img['orientation'] == 'portrait']
    
    #Checks if the row contains only portrait images
    if len(portrait_check) == len(row):
        return True
    else:
        return False

def main():
    pass

if __name__ == "__main__":
    main()