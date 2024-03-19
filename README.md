# 🖥️ GNOME Wallpaper

Tool that automatically sets new wallpapers from Unsplash every new session. Powered by Unsplash API.

### Disclaimer

This application is powered by the Unsplash API, which provides access to a library of photos. All photos provided through this application belong to their respective owners and are distributed under the Unsplash License. For more information about the Unsplash License, please visit: [Unsplash License](https://unsplash.com/license
). Additionally, users can find more information about the Unsplash API and its documentation at: [Unsplash API Documentation](https://unsplash.com/documentation
).

## Installation

### Prerequisites
- python3
- GNOME Shell
- python3-pip

### Installation steps

First things first download the source code

```sh
$ git clone https://github.com/youngling-coder/gnome-wallpaper/
```

Or ZIP archive with source code using GitHub official site.

Do not forget to extract files from archive!

After downloading and extracting files all you need to do is to execute ```setup.sh``` script in source code folder. It contains all necessary stuff to make gnome-wallpapers work properly.

To execute this script run following in terminal:

```sh
$ cd /path/to/source/gnome-wallpaper
$ chmod +x setup.sh
$ ./setup.sh
```

### Unsplash API setup
Paste your Unsplash API token when it will be prompted while script execution.

### GUI Interface

This app is also has GUI powered by PyQt5. To launch GUI Instance of application run in your terminal

```sh
$ ~/.gnome-wallpaper/gnome-wallpaper --gui
```

**If no errors will occur, installation is done!**

### Config Setup

You can also see file called ```config.json``` in source code or in installed app directory. This file is responsible for storing relevant image queries that you would like to see on your desktop. It may be specific topic, query, collection or even an username. For instance, if you want to see photos of apples created by someone with the username @itsmyname, you would modify the file as follows

```json
{
    "app": {
        "wallpaper_filename": "unsplash_wallpaper.jpg",
        "download_directory": "~/.local/share/backgrounds/"
    },

    // modify these parameters
    "image": {
        "query": "apples",
        "nickname": "itsmyname"
    }
}
```

Full list of available parameters you can see **[here](https://unsplash.com/documentation#get-a-random-photo)**.


### Next steps

After all the installation and setup stuff is done we need to end current session and then log back in.

#### Enjoy your new wallpapers!
