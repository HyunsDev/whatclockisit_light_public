#-*- coding: utf-8 -*-
from os import getenv

class wcii():
    def __init__(self):
        appdatafolder = getenv('localappdata') + "/whatclockisit/lite/"
        appdatafolder = appdatafolder.replace("\\", "/").replace("\\", "/").replace("\\", "/").replace("\\", "/")

        self.datafolder = appdatafolder
        self.appdata = appdatafolder + "data/data.wcii"
        self.appcorelive = appdatafolder + "data/core_live.wcii"
        self.textdata = appdatafolder + "data/text_data.wcii"
        self.appfont = appdatafolder + "font/"
        self.appfontfile = "font.otf"
        self.appimage = appdatafolder + "image/wcii_wall.png"
        self.applog = appdatafolder + "log/"
        self.apptemp = appdatafolder + "temp/"
        self.wallpaper_address = appdatafolder + "image/wcii_wall.png"
        self.dimage = "dsource/wcii_dimage.png"

        self.fontsize = 55