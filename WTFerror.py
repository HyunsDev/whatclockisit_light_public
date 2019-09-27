#-*- coding: utf-8 -*-
from ctypes import windll
from os import getenv, path, makedirs  # 파일 위치
import datetime
import sys
import shutil
import wcii_var
from time import sleep

wc = wcii_var.wcii()

def appdata_check():
    #백업용
    appdata_error = False

    dimage = "dsource/wcii_dimage.png"
    dfont = "dsource/font.otf"
    dflicense = "dsource/font_license.txt"
    ddata = "dsource/data.wcii"
    ddatalive = "dsource/core_live.wcii"

    localappdata = getenv('localappdata')
    if not path.isdir(str(localappdata + "/whatclockisit/lite/")):
        makedirs(path.join(localappdata + "/whatclockisit/lite"))
        makedirs(path.join(localappdata + "/whatclockisit/lite/data"))
        makedirs(path.join(localappdata + "/whatclockisit/lite/log"))
        makedirs(path.join(localappdata + "/whatclockisit/lite/temp"))
        makedirs(path.join(localappdata + "/whatclockisit/lite/font"))
        makedirs(path.join(localappdata + "/whatclockisit/lite/image"))
        print("lite 디렉터리 발견못함, 전체 디렉터리 생성")
        appdata_error = True

    if not path.isdir(str(localappdata + "/whatclockisit/lite/log")):
        print("로그 디렉터리 발견 실패, 디렉터리 생성")
        makedirs(path.join(localappdata + "/whatclockisit/lite/log"))
        appdata_error = True

    if not path.isdir(str(localappdata + "/whatclockisit/lite/temp")):
        print("temp 디렉터리 발견실패, 디렉터리 생성")
        makedirs(path.join(localappdata + "/whatclockisit/lite/temp"))
        appdata_error = True

    appdatafolder = getenv('localappdata') + "/whatclockisit/lite/"
    appdatafolder = appdatafolder.replace("\\", "/").replace("\\", "/").replace("\\", "/").replace("\\", "/")

    appdata = appdatafolder + "data/data.wcii"
    appcorelive = appdatafolder + "data/core_live.wcii"
    appfont = appdatafolder + "font/"
    appimage = appdatafolder + "image/"
    applog = appdatafolder + "log/"
    apptemp = appdatafolder + "temp/"
    appfontfile = "font.otf"

    if not path.isfile(appimage + "wcii_wall.png"):
        try: makedirs(path.join(localappdata + "/whatclockisit/lite/image"))
        except: pass
        shutil.copyfile(dimage, appimage + 'wcii_wall.png')
        print("배경화면 발견실패, 기본이미지로 대체함")
        appdata_error = True

    if not path.isfile(appfont + appfontfile):
        try: makedirs(path.join(localappdata + "/whatclockisit/lite/font"))
        except: pass
        shutil.copyfile(dfont, appfont + appfontfile)
        shutil.copyfile(dflicense, appfont + "font_license.txt")
        print("폰트 발견실패, 기본폰트로 대체함")
        appdata_error = True

    if not path.isfile(appdata):
        try: makedirs(path.join(localappdata + "/whatclockisit/lite/data"))
        except: pass
        shutil.copyfile(ddata, appdata)
        print("데이터 파일 발견실패, 데이터 파일 생성")
        appdata_error = True

    if not path.isfile(appcorelive):
        try: makedirs(path.join(localappdata + "/whatclockisit/lite/data"))
        except: pass
        shutil.copyfile(ddatalive, appcorelive)
        print("코어 라이브 파일 발견실패, 데이터 파일 생성")
        appdata_error = True

    if appdata_error == True:
        return True
    elif appdata_error == False:
        return False

def errorwindow(e, pos=None, logname="error", uselog="yes", mes=None, title="야생의 Bug가 나타났다!"): #반드시 먼저 appdata_check() 가 필요함
    #에러 발생 위치
    if pos == None:
        if __name__ == "wcii_core_lite":
            logname = "core_error"
            pos = "코어"
        if __name__ == "wcii_gui_lite":
            logname = "gui_error"
            pos = "설정"
        if __name__ == "wcii_wallpaper":
            logname = "wallpaper_error"
            pos = "배경화면 생성 과정"
    elif pos == "코어":
        logname = "core_error"
    elif pos == "설정":
        logname = "gui_error"
    else:
        pos = "프로그램"
        logname = __name__ + "_error"

    #로그 작성
    if uselog is "yes":
        lognow = datetime.datetime.now()
        try:
            with open(getenv('localappdata') + f"/whatclockisit/lite/log/{logname}.log", "a") as f:
                f.write(f"{lognow.year}/{lognow.month}/{lognow.day} {lognow.hour}:{lognow.minute}:{lognow.second} 오류 내용 : {e}\n")
        except FileNotFoundError:
            with open(getenv('localappdata') + f"/whatclockisit/lite/log/{logname}.log", "w") as f:
                f.write(
                    f"{lognow.year}/{lognow.month}/{lognow.day} {lognow.hour}:{lognow.minute}:{lognow.second} 오류 내용 : {e}\n")

    #창 내용
    if appdata_check() is True:
        if uselog == "no":
            mes = f"{pos}에 버그가 있었지만 해결했어요! (하지만 다시 실행해야 해요..)\n혹시 이 창이 또다시 나온다면 이 창을 캡쳐해서 지금몇시계 디스코드에 보내주세요!\n나쁜 버그의 이름 : {e}"
        else:
            mes = f"{pos}에 버그가 있었지만 해결했어요! (하지만 다시 실행해야 해요..)\n혹시 이 창이 또다시 나온다면 이 창을 캡쳐해서 지금몇시계 디스코드에 보내주세요!\n나쁜 버그의 이름 : {e}\n(이건 비밀인데 %localappdata%whatclockisit/lite/log/ 에 있는 파일을\n 함께 보내주면 더 잘 해치워준데요!"
    elif mes is None:
        if uselog == "no":
            mes = f"{pos}에 나쁜 Bug가 나타났어요!\n이 화면을 캡쳐하고 지금몇시계 디스코드에 올려서\n이 Bug를 해치워주세요!\n나쁜 버그의 이름 : {e}"
        else:
            mes = f"{pos}에 나쁜 Bug가 나타났어요!\n이 화면을 캡쳐하고 지금몇시계 디스코드에 올려서\n이 Bug를 해치워주세요!\n나쁜 버그의 이름 : {e}\n(이건 비밀인데 %localappdata%whatclockisit/lite/log/ 에 있는 파일을\n 함께 보내주면 더 잘 해치워준데요!"

    #에러창 띄우기
    windll.user32.MessageBoxW(None, str(mes), str(title), 0)
    sys.exit(0)

def writelog(logfile, logtext, plus=None): #반드시 먼저 appdata_check()가 필요함
    appdata_check()
    lognow = datetime.datetime.now()
    try:
        with open(getenv('localappdata') + f"/whatclockisit/lite/log/{logfile}.log", "a") as f:
            msg = f"{lognow.year}/{lognow.month}/{lognow.day} {lognow.hour}:{lognow.minute}:{lognow.second} {plus} 내용 : {logtext}\n"
            f.write(msg)
    except FileNotFoundError:
        with open(getenv('localappdata') + f"/whatclockisit/lite/log/{logfile}.log", "w") as f:
            msg = f"{lognow.year}/{lognow.month}/{lognow.day} {lognow.hour}:{lognow.minute}:{lognow.second} {plus} 내용 : {logtext}\n"
            f.write(msg)
def corelive():
    try:
        with open(wc.appcorelive, "w") as f:
            f.write("r u already live?")
        sleep(0.5)
        with open(wc.appcorelive, "r") as f:
            livedata = f.readline()

        if livedata == "already":
            return True
        else:
            sleep(0.5)
            with open(wc.appcorelive, "r") as f:
                livedata = f.readline()
                if livedata != "already":
                    return False
    except:
        with open(wc.appcorelive, "w") as f:
            f.write("r u already live?")
        sleep(0.5)
        with open(wc.appcorelive, "r") as f:
            livedata = f.readline()

        if livedata == "already":
            return True
        else:
            sleep(0.5)
            with open(wc.appcorelive, "r") as f:
                livedata = f.readline()
                if livedata != "already":
                    return False




if __name__ == '__main__':
    print(appdata_check())