# -*- coding:utf-8 -*-
from ctypes import windll #바탕화면 등록 모듈
from os import path, getenv #파일 위치
from time import sleep #sleep
import datetime #현재 시간 모듈
from PIL import Image, ImageDraw, ImageFont #이미지 제작 모듈
from wcii_time_light import wciitime, wciitext #문구 모듈
#appdata 불러오기
appdatafolder = getenv('localappdata') + "/whatclockisit/light/"
appdatafolder = appdatafolder.replace("\\","/").replace("\\","/").replace("\\","/").replace("\\","/")
appdata = appdatafolder + "data/data.wcii"
appfont = appdatafolder + "font/"
appimage = appdatafolder + "image/"
applog = appdatafolder + "log/"
apptemp = appdatafolder + "temp/"
appfontfile = "NotoSansCJKkr-Black.otf"

dimage = appimage + "wcii_dimage.png"
wallpaper_address = appimage + "wcii_wall.png"

# 배경화면 생성 및 등록 함수 (메인 함수)
def wcii_wallpaper(wciitext):
    print("[ 새로고침 ]")
    nowtime = wciitime()
    nowtext = wciitext
    ws = wallpaper_address
    ffolder = appfont
    ffile = appfontfile
    fsize = 60
    wt = apptemp + "temp.png"
    try:
        imagepath = Image.open(ws)
    except:
        imagepath = Image.open(dimage)

    msg = str(nowtext) + "\n" + str(nowtime)
    font = ImageFont.truetype(path.join(ffolder, ffile), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)

    draw.text(((1920 - w) / 2, (1080 - h ) / 2 - 50), msg, fill="white", font=font, align="center")
    imagepath.save(wt)
    imagepath = path.normpath(wt)
    windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)

def stop_wallpaper():
    ws = wallpaper_address
    ffolder = appfont
    ffile = appfontfile
    fsize = 60
    wt = apptemp + "close.png"
    try:
        imagepath = Image.open(ws)
    except:
        imagepath = Image.open(dimage)

    msg = "지금몇시계 영업종료"
    font = ImageFont.truetype(path.join(ffolder, ffile), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)
    draw.text(((1920 - w) / 2, (1080 - h) / 2 - 50), msg, fill="white", font=font, align="center")
    imagepath.save(wt)
    imagepath = path.normpath(wt)
    windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)

def error_wallpaper(error):
    ws = wallpaper_address
    ffolder = appfont
    ffile = appfontfile
    fsize = 30
    wt = apptemp + "error.png"
    try:
        imagepath = Image.open(ws)
    except:
        imagepath = Image.open(dimage)

    msg = error
    font = ImageFont.truetype(path.join(ffolder, ffile), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)
    draw.text(((1920 - w) / 2, (1080 - h) / 2 - 50), msg, fill="white", font=font, align="center")
    imagepath.save(wt)
    imagepath = path.normpath(wt)
    windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)

#메인 코드
try:
    print("지금몇시계 라이트 작동 시작")
    wciitextnow = wciitext()
    lognow = datetime.datetime.now()
    wcii_wallpaper(wciitextnow)

    with open(applog + "wakeup.log", "a") as f:
        f.write("%s년 %s월 %s일 %s시 %s분 %s초에 지금몇시계 라이트가 일어났어요!\n" % (
        lognow.year, lognow.month, lognow.day, lognow.hour, lognow.minute, lognow.second))

    with open(appdata, "w") as f:
        f.write("live")
    while True: #반복
        try:
            # 메인 코드 시작
            with open(appdata, "r") as f:
                killdata = f.readline()

            now = datetime.datetime.now()
            if killdata == "kill":
                stop_wallpaper()
                with open(appdata, "w") as f:
                    f.write("dead")
                break
            else:
                nowmin = now.strftime('%M') #30분마다 문구 불러오기
                if nowmin == '59':
                    korean_nowtext = wciitext()
                elif nowmin == '29':
                    korean_nowtext = wciitext()

                if now.strftime('%S') == "00": #실행
                    wcii_wallpaper(wciitextnow)
                sleep(0.9)

        #메인 코드 끝
        except Exception as e:
            lognow = datetime.datetime.now()
            with open(applog + "error.log", "a") as f:
                f.write(f"{lognow.year}년 {lognow.month}월 {lognow.day}일 {lognow.hour}시 {lognow.minute}분 {lognow.second}초 오류 내용 : {e}\n")
            print("실행 에러 : " + str(e))
            error_wallpaper(f"문제가 발생했습니다.\n이 화면을 캡쳐해서 지금몇시계 디스코드에 보내주세요!\n별다른 문제가 없으면 이 화면은 잠시 뒤 사라집니다.\n실행 에러 : {e}")
            pass

except Exception as e:
    lognow: datetime = datetime.datetime.now()
    with open(applog + "error.log", "a") as f:
        f.write(f"{lognow.year}년 {lognow.month}월 {lognow.day}일 {lognow.hour}시 {lognow.minute}분 {lognow.second}초 심각한 오류 내용 : {e}\n")
    print("심각한 에러 : " + str(e))
    error_wallpaper(f"문제가 발생했습니다.\n이 화면을 캡쳐해서 지금몇시계 디스코드에 보내주세요!\n추가로 지금몇시계 코어가 종료되었습니다.\n종료 에러 : {e}")

