\#!/usr/bin/bash

# Set installation variables
APP_NAME=gnome-wallpaper

BUILD_DIR=dist/
EXEC_DIR=/bin/
CONFIG_DIR=~/.config/$APP_NAME
ICON_DIR=/usr/share/icons/$APP_NAME
AUTOSTART_DIR=~/.config/autostart

# Installing python3 requirements
pip3 install -r requirements.txt

# Building application
pyinstaller --onefile --noconsole app/main.py --name $APP_NAME

# Make the application executable
chmod +x dist/$APP_NAME

# Create autostart directory if not exists
mkdir -p $AUTOSTART_DIR $CONFIG_DIR $ICON_DIR

# Install necessary files
sudo cp dist/$APP_NAME $EXEC_DIR
cp config.json $CONFIG_DIR
sudo cp app/icon.png $ICON_DIR
cp app/entries/$APP_NAME-autostart.desktop $AUTOSTART_DIR

# Remove building files after install
rm -rf $BUILD_DIR
rm -rf build/
rm *.spec

echo "Installation done!"
