import sys
import requests
from config import CONFIG, load_config, write_config
import os

# This application is powered by the Unsplash API
# All the photos provided are belong to their owners
# All the photos provided are distributed under the Unsplash License
# Unsplash License: https://unsplash.com/license
# More info about Unsplash API: https://unsplash.com/documentation

# Initializing Unsplash API token and url
API_TOKEN = os.getenv("UNSPLASH_API_TOKEN")
API_URL = "https://api.unsplash.com/photos/random"

# Reading command line arguments
args = sys.argv

# Setting up basic config store parameters
config_filename = os.path.expanduser("~/.config/gnome-wallpaper/config.json")

# Check if config file exists and create one if not
if not os.path.exists(config_filename) or os.path.isdir(config_filename):
    write_config(config_filename)
else:
    load_config(config_filename)

# Initializing downloading parameters
WALLPAPER_DIRECTORY = os.path.expanduser(CONFIG["app"]["download_directory"])
BASE_IMAGE_NAME = CONFIG["app"]["wallpaper_filename"]
DONWLOAD_PATH = os.path.join(WALLPAPER_DIRECTORY, BASE_IMAGE_NAME)


def set_wallpaper() -> None:
    """Sets a new wallpaper for GNOME shell."""

    # ATTENTION!
    #
    # Code below is only working for GNOME shell! If you have
    # any other Desktop Environment, this code is not supposed
    # to work properly or work at all.

    # Commands to set wallpaper for dark and light themes
    commands = [f"gsettings set org.gnome.desktop.background picture-uri \"file://{DONWLOAD_PATH}\"",
                f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{DONWLOAD_PATH}\""]

    # Running commands
    for command in commands:
        os.system(command=command)


def save_image(content: bytes) -> str:
    """Saves image locally. Returns downloaded file location"""

    # Set up download directory if not exists
    if not os.path.exists(WALLPAPER_DIRECTORY):
        os.mkdir(WALLPAPER_DIRECTORY)


    # Writing data to the image
    with open(DONWLOAD_PATH, "wb") as write_image:
        write_image.write(content)


def get_image_url() -> str:
    """Get image url."""

    # Setting up parameters & headers
    headers = {
        "Authorization": f"Client-ID {API_TOKEN}"
    }

    params = CONFIG["image"]

    # Generating response from API
    response = requests.get(API_URL, headers=headers, params=params)

    # Return image url
    return response.json()[0]


def get_image_as_bytes(url: str) -> bytes | None:
    """Parse image from url and returns image data as bytes."""

    # Parse image url
    response = requests.get(url=url)

    # Return content as bytes
    if response.status_code == 200:
        return response.content


if __name__ == "__main__":

    # Get image url to work with
    image_url = get_image_url()

    # Obtain image as bytes collection for further processing
    img_content = get_image_as_bytes(url=image_url)

    # Save image and return downloaded image path
    save_image(img_content)

    # Set new wallpapers
    set_wallpaper()
