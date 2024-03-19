import json

# Config variable
CONFIG = {
    "app": {
        "wallpaper_filename": "unsplash_wallpaper.jpg",
        "download_directory": "~/.local/share/backgrounds/"
    },
    "image": {
        "orientation": "landscape",
        "count": 1
    }
}


def load_config(filename: str):
    """Load config from file as a dict object."""

    global CONFIG

    # Reading config from file specified
    with open(filename) as json_config:
        CONFIG = json.load(json_config)


def write_config(filename: str):
    """Write existing config dict object to file."""

    global CONFIG

    # Write new config to the file
    with open(filename, "w") as json_config:
        json.dump(CONFIG, json_config, indent=4)
