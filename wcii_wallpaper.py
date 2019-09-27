#-*- coding: utf-8 -*-
from ctypes import windll  # 바탕화면 등록 모듈
from os import path
from PIL import Image, ImageDraw, ImageFont  # 이미지 제작 모듈
from wcii_time_lite import *  # 문구 모듈
from WTFerror import *
import wcii_var
from time import sleep
from wcii_time_lite import *

wc = wcii_var.wcii()

def wcii_wallpaper(wciitext=None):
    nowtime = wciitime()
    if wciitext == None:
        nowtext = loadtext()
    else:
        nowtext = wciitext
    print(f"[ 새로고침 ] ({nowtime})")
    ws = wc.appimage
    ffolder = wc.appfont
    ffile = wc.appfontfile
    fsize = wc.fontsize
    wt = wc.apptemp + "temp.png"
    try:
        imagepath = Image.open(ws)
    except:
        appdata_check()
        imagepath = Image.open(ws)

    msg = str(nowtext) + "\n" + str(nowtime)
    font = ImageFont.truetype(path.join(ffolder, ffile), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)

    draw.text(((1920 - w) / 2, (1080 - h) / 2 - 50), msg, fill="white", font=font, align="center")
    imagepath.save(wt)
    imagepath = path.normpath(wt)
    windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)

'''
def stop_wallpaper():
    ws = wc.appimage
    ffolder = wc.appfont
    ffile = wc.appfontfile
    fsize = 60
    wt = wc.apptemp + "close.png"
    try:
        imagepath = Image.open(ws)
    except:
        appdata_check()
        imagepath = Image.open(ws)

    msg = "지금몇시계 영업종료"
    font = ImageFont.truetype(path.join(ffolder, ffile), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)
    draw.text(((1920 - w) / 2, (1080 - h) / 2 - 50), msg, fill="white", font=font, align="center")
    imagepath.save(wt)
    imagepath = path.normpath(wt)
    windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)
'''
def stop_wallpaper():
    windll.user32.SystemParametersInfoW(20, 0, wc.appimage, 0)

def error_wallpaper(e):
    sleep(0.2)
    ws = wc.appimage
    ffolder = wc.appfont
    ffile = wc.appfontfile
    fsize = 30
    wt = wc.apptemp + "error.png"
    try:
        imagepath = Image.open(ws)
    except:
        appdata_check()
        imagepath = Image.open(ws)
    msg = f"문제가 발생했습니다. 이 화면과 함께\n%localappdata%/whatclockisit/lite/log에 있는 파일들과 함께\n지금몇시계 디스코드에 올려주세요!\n지금몇시계 코어가 종료되었습니다.\n종료 에러 : {e}"
    font = ImageFont.truetype(path.join(ffolder, ffile), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)

    draw.text(((1920 - w) / 2, (1080 - h) / 2 - 50), msg, fill="white", font=font, align="center")
    imagepath.save(wt)
    imagepath = path.normpath(wt)
    windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)

def updatetext(hour=None):
    wc_textdata = str(wciitext(hour))
    with open(wc.textdata, "w") as f:
        f.write(wc_textdata)
    return wc_textdata

def loadtext():
    try:
        with open(wc.textdata, "r") as f:
            textdata = f.readline()
    except:
        updatetext()
        with open(wc.textdata, "r") as f:
            textdata = f.readline()
    return textdata



