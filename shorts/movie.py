# Path: shorts/parkour.py
import random
from moviepy.editor import *
import PIL.Image as Image
import os

def double_image_size(input_image_path, output_image_path, x):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Get the original dimensions
        width, height = img.size

        # Double the size by multiplying width and height by 2
        new_width = width * x
        new_height = height * x

        # Resize the image to the new dimensions
        doubled_image = img.resize((new_width, new_height))

        # Save the doubled size image
        doubled_image.save(output_image_path)

# Replace 'input_image.jpg' and 'output_image.jpg' with your image file paths
input_image_path = 'subscribe.png'
output_image_path = 'subscribe-xl.png'

double_image_size(input_image_path, output_image_path, 3)

input_image_path = 'reddit.png'
output_image_path = 'reddit-xl.png'

double_image_size(input_image_path, output_image_path, 2)


#get a random 60 second clip from parkour.mp4
def get_clip():
    clip = VideoFileClip('parkour.mp4', audio=False)
    clip.fps = 30
    clip.size = (1920, 1080)
    start = random.randint(0, 60)
    end = start + 60
    new_clip = clip.subclip(start, end)
    new_clip.write_videofile('new_clip.mp4', fps=30)
    new_clip.close()

#add subscribe.mov on top of new_clip.mp4 at the end of new_clip.mp4
def add_subscribe():
    clip = VideoFileClip('new_clip.mp4', audio=False)
    clip.fps = 30
    subscribe = ImageClip('subscribe-xl.png', duration=5)
    subscribe.fps = 30
    final_clip = CompositeVideoClip([clip, # starts at t=0
                                    subscribe.set_start(55).set_position(("center")) # starts at t=55 CHANGE THIS BACK TO 55 WHEN DONE TESTING
                                    ])
    final_clip.write_videofile('final_clip.mp4', fps=30)
    final_clip.close()
    subscribe.close()
    clip.close()
    # os.remove('new_clip.mp4')

#add the reddit.png on top of final_clip.mp4 for the first 5 seconds
def add_reddit():
    clip = VideoFileClip('final_clip.mp4', audio=False)
    clip.fps = 30
    reddit = ImageClip('reddit-xl.png').set_position(("left", "top")).set_duration(5)
    reddit.fps = 30
    final_clip = CompositeVideoClip([clip, # starts at t=0
                                    reddit.set_start(0).set_position(("center")) # starts at t=0
                                    ])
    final_clip.write_videofile('shorts.mp4', fps=30)
    final_clip.close()
    reddit.close()
    clip.close()
    # os.remove('new_clip.mp4')

get_clip()
add_subscribe()
add_reddit()
