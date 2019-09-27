from wcii_wallpaper import *
from time import sleep
import wcii_var
from WTFerror import *
import subprocess
from wcii_time_lite import *

wc = wcii_var.wcii()

print("< 테스트 시작 >")
wcii_wallpaper("테스트 시작")
sleep(1.5)

print("< 배경화면 설정 테스트 >")
wcii_wallpaper() #월페이퍼 테스트
sleep(1.5)

print("< 스탑 배경화면 설정 테스트 >")
stop_wallpaper() #스탑 월페이퍼 테스트
sleep(1.5)

print("< 에러 배경화면 설정 테스트 >")
error_wallpaper("에러 테스트") #에러 월페이퍼 테스트
sleep(1.5)

print("< 문구 테스트 >")
updatetext() #문구 업데이트, 로드 테스트
print("업데이트 : " + updatetext()) #문구 업데이트
print("로드 : " + loadtext()) #문구 로드
sleep(1.5)

print("< appdata_check 테스트 >")
appdata_check() #appdata 체크
print(appdata_check())
sleep(1.5)

print("< writelog 테스트 >")
with open(wc.applog + "test.log", "w") as f: #로그 내용 초기화
    f.write("")
writelog("test", "test", "testlog") #로그 기능 테스트
with open(wc.applog + "test.log", "r") as f: #로그 내용 불러오기
    print(f.read())
sleep(1.5)

#print("< wcii_gui_lite.py 테스트>")
#try:
#    subprocess.run(['wcii_gui_lite.py'], shell=True)
#except:
#    pass
#sleep(1.5)

#print("< wcii_core_lite.py 테스트 (실행시간 10초) >")
#try:
#    subprocess.run(['wcii_core_lite.py'], shell=True, timeout=10)
#except:
#    pass
#sleep(1.5)

print("< 코어 라이트 테스트 >")
print(corelive())
sleep(1.5)

print("< wcii_time_lite.py 테스트 >")
print("wciitime() : " + wciitime())
print("wciitext() : " + wciitext())
sleep(1.5)

#print("< errorwindow 테스트 >")
#errorwindow("테스트")


