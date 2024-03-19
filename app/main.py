#!/usr/bin/python3

import sys
from core import core
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QImage
from app_ui import Ui_MainWindow


class GNOME_Wallpaper(QMainWindow):
    def __init__(self) -> None:
        super(GNOME_Wallpaper, self).__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set current image as None
        self.current_image = None

        # Connect slots to methods
        get_wallpaper = lambda: self.getWallpaperButtonClicked(gui_mode=True)
        self.ui.getWallpaperButton.clicked.connect(get_wallpaper)
        self.ui.setWallpaperButton.clicked.connect(self.setWallpaperButtonClicked)


    def getWallpaperButtonClicked(self, gui_mode: bool = True):

        # Fetch new random image
        self.current_image = core.get_image_url()

        if gui_mode:
            # Select scaled image for preview
            image_data = core.get_image_as_bytes(url=self.current_image["urls"]["regular"])

            # Create pixmap for selected image
            image = QImage().fromData(image_data)
            pixmap = QPixmap().fromImage(image)

            # Generate credits for a photo
            credits_link = f"Captured by <a href=\"{self.current_image["user"]["links"]["html"]}\">{self.current_image["user"]["name"]}</a>"

            # Show photo with credits
            self.ui.creditsLabel.setText(credits_link)
            self.ui.imageArea.setPixmap(pixmap)


    def setWallpaperButtonClicked(self):

        # Get full image
        image_data = core.get_image_as_bytes(url=self.current_image["urls"]["full"])

        # Save image and set as wallpaper
        core.save_image(content=image_data)
        core.set_wallpaper()



if __name__ == "__main__":

    # Read console args
    args = sys.argv

    # Create application and main window instances
    app = QApplication([])
    main_window = GNOME_Wallpaper()

    # Show main window if gui argument specified,
    # otherwise automatically download and set wallpaper
    if "--gui" in args:
        main_window.show()
        sys.exit(app.exec())
    else:
        main_window.getWallpaperButtonClicked(gui_mode=False)
        main_window.setWallpaperButtonClicked()

        app.exit()
