#-*- coding: utf-8 -*-
from time import sleep  # sleep
import datetime  # 현재 시간 모듈
from wcii_time_lite import *  # 문구 모듈
import sys
from wcii_wallpaper import *
from WTFerror import *
import wcii_var

try:
    appdata_check()
    wc = wcii_var.wcii()
    last_e = ""
    #라이트 테스트
    if corelive() == True:
        writelog("core_error", "이미 실행된 상태", "이미 실행된 상태")
        sys.exit(1)

    # 메인 코드
    try:
        errorcount = 0 #에러 누적
        print("지금몇시계 라이트 작동 시작")
        wciitextnow = wciitext() #기본 문구
        lognow = datetime.datetime.now()
        updatetext()
        wcii_wallpaper()

        try:
            with open(wc.applog + "wakeup.log", "a") as f:
                f.write("%s년 %s월 %s일 %s시 %s분 %s초에 지금몇시계 라이트가 일어났어요!\n" % (
                    lognow.year, lognow.month, lognow.day, lognow.hour, lognow.minute, lognow.second))
        except FileNotFoundError:
            with open(wc.applog + "wakeup.log", "w") as f:
                f.write("%s년 %s월 %s일 %s시 %s분 %s초에 지금몇시계 라이트가 일어났어요!\n" % (
                    lognow.year, lognow.month, lognow.day, lognow.hour, lognow.minute, lognow.second))

        with open(wc.appcorelive, "w") as f:
            f.write("live")

        while True:  # 반복
            try:
                # 메인 코드 시작
                with open(wc.appdata, "r") as f:
                    killdata = f.readline()

                with open(wc.appcorelive, "w") as f:
                    f.write("already")

                now = datetime.datetime.now()
                if killdata == "kill":
                    stop_wallpaper()
                    with open(wc.appdata, "w") as f:
                        f.write("dead")
                    try:
                        with open(wc.applog + "wakeup.log", "a") as f:
                            f.write("%s년 %s월 %s일 %s시 %s분 %s초에 지금몇시계 라이트가 자러갔어요!\n" % (
                                lognow.year, lognow.month, lognow.day, lognow.hour, lognow.minute, lognow.second))
                    except FileNotFoundError:
                        with open(wc.applog + "wakeup.log", "w") as f:
                            f.write("%s년 %s월 %s일 %s시 %s분 %s초에 지금몇시계 라이트가 자려갔어요!\n" % (
                                lognow.year, lognow.month, lognow.day, lognow.hour, lognow.minute, lognow.second))
                    break
                else:
                    nowmin = now.strftime('%M')  # 30분마다 문구 불러오기
                    if nowmin == '59':
                        updatetext()
                    elif nowmin == '29':
                        updatetext()

                    if now.strftime('%S') == "00":  # 실행
                        wcii_wallpaper()
                        sleep(0.65)
                sleep(0.4)

            # 메인 코드 끝
            
            #오류 제어 1단 : 실행 가능
            except Exception as e:
                lognow = datetime.datetime.now()
                if e == last_e:
                    errorcount = errorcount + 1
                else:
                    last_e = e
                if errorcount <= 10:
                    writelog("core_error", e, "가벼운 오류")
                    errorcount = errorcount + 1
                    if errorcount == 5:
                        appdata_check()
                    pass

                else: #오류 제어 2단 : 1단이 10회 이상 반복
                    try:
                        error_wallpaper(e)
                        writelog("core_error", e, "심각한 오류")
                    except Exception as e:
                        errorwindow(e)
                        writelog("core_error", e, "심각한 오류 error_wallpaper 사용불가")
                        pass
                    break

    #오류 제어 3단 : 더 큰 범위에서 에러 발생
    except Exception as e:
        print("매우 심각한 오류 : " + str(e))
        try:
            writelog("core_error", e, "매우매우 심각한 오류")
            error_wallpaper(e)
        except:
            writelog("core_error", e, "매우매우 심각한 오류 (월페이퍼 사용불가)")
            errorwindow(e)

#오류 제어 4단 : 1,2,3단에서 제어하지 못한 에러
except Exception as e:
    try:
        writelog("core_error", e, "매우매우매우 심각한 오류")
        error_wallpaper(e)
    except:
        writelog("core_error", e, "매우매우매우 심각한 오류 (월페이퍼 사용불가)")
        errorwindow(e)
