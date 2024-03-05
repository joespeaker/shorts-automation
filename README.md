# Parkour Shorts

This Python script generates short video clips with parkour footage, adds branding elements, and creates a final compilation video.

## Requirements

- Python 3
- moviepy
- PIL (Python Imaging Library)

## Usage

1. Place the script `parkour.py` in a directory with your parkour video file (`parkour.mp4`) and branding images (`subscribe.png`, `reddit.png`).
2. Make sure the branding images are named `subscribe.png` and `reddit.png`.
3. Run the script `parkour.py` using Python.

## Features

- **Double Image Size:** The script doubles the size of the input images `subscribe.png` and `reddit.png` and saves them as `subscribe-xl.png` and `reddit-xl.png`, respectively.

- **Get Clip:** It extracts a random 60-second clip from the parkour video (`parkour.mp4`) and saves it as `new_clip.mp4`.

- **Add Subscribe:** It adds the `subscribe-xl.png` branding image to the end of `new_clip.mp4` and saves the final clip as `final_clip.mp4`.

- **Add Reddit:** It adds the `reddit-xl.png` branding image to the beginning of `final_clip.mp4` for the first 5 seconds and saves the resulting short video as `shorts.mp4`.

## How to Run

To run the script, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Install the required dependencies by running `pip install moviepy pillow`.
3. Place the script `parkour.py` in the same directory as your parkour video (`parkour.mp4`) and branding images (`subscribe.png`, `reddit.png`).
4. Open a terminal or command prompt in the directory containing the script and run `python parkour.py`.

The generated short video will be saved as `shorts.mp4`.

## Notes

- Adjust the script according to your specific file paths and requirements.
- Remember to replace placeholder image and video file names with your actual file names.

