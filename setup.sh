#!/usr/bin/bash

# Set installation variables
APP_NAME=gnome-wallpaper

BUILD_DIR=dist/
GNOME_WALLPAPER_DIR=~/.$APP_NAME
CONFIG_DIR=~/.config/$APP_NAME
ICON_DIR=~/.local/share/icons/$APP_NAME
AUTOSTART_DIR=~/.config/autostart

# Installing python3 requirements
pip3 install -r requirements.txt

# Building application
pyinstaller --onefile --noconsole app/main.py --name $APP_NAME

# Make the application executable
chmod +x dist/$APP_NAME

# Remove installation directories if already exists and create new ones
rm -rf $GNOME_WALLPAPER_DIR $CONFIG_DIR $ICON_DIR
mkdir $GNOME_WALLPAPER_DIR $CONFIG_DIR $ICON_DIR

# Create autostart directory if not exists
mkdir -p $AUTOSTART_DIR

# Install necessary files
cp  dist/$APP_NAME $GNOME_WALLPAPER_DIR
cp config.json $CONFIG_DIR
cp app/icon.png $ICON_DIR
cp app/entries/$APP_NAME-autostart.desktop $AUTOSTART_DIR
cp app/entries/$APP_NAME-gui.desktop ~/.local/share/applications

# Remove building files after install
rm -rf $BUILD_DIR
rm -rf build/
rm *.spec

# Read Unsplash API token
echo "Enter Unsplash API Access Token: "
read token

# Set up Unsplash API token
unset UNSPLASH_API_TOKEN
echo "export UNSPLASH_API_TOKEN=\"$token\"" >> ~/.bashrc

echo "Installation done!"
