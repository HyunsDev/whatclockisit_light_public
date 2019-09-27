#-*- coding: utf-8 -*-
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import wcii_var
from WTFerror import *

wc = wcii_var.wcii()

def wciitime(time=None):
    if time == None:
        now = datetime.datetime.now()
        nowtime = now.strftime('%H%M')
        nowtime = str(nowtime)
    else:
        nowtime = str(time)

    if nowtime == '0000':
        showtime = "지금은 자정이야"
        return showtime
    elif nowtime == '1200':
        showtime = "지금은 정오야"
        return showtime
    else:
        hour = int(nowtime[0:2])
        if hour == 00:
            hour = 24
        minu = int(nowtime[2:4])
        time_map_hour = {0: "", 1: "한", 2: "두", 3: "세", 4: "네", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉"}
        time_map_minu = {0: "", 1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

        # 시간
        if hour >= 21: showhour = "밤 "
        elif hour >= 17: showhour = "저녁 "
        elif hour >= 15: showhour = "오후 "
        elif hour >= 11: showhour = "점심 "
        elif hour >= 7: showhour = "아침 "
        elif hour >= 5: showhour = "이른 아침 "
        elif hour >= 3: showhour = "새벽 "
        elif hour >= 1: showhour = "늦은 밤 "
        elif hour >= 0: showhour = "밤 "

        if hour > 12: hour = hour - 12

        if hour >= 10:
            hour = hour - 10
            showhour = showhour + "열" + time_map_hour[hour] + " 시 "
        else:
            showhour = showhour + time_map_hour[hour] + " 시 "

        # 분 구문
        showminu = ""
        if minu >= 10:
            if minu > 20:
                minu_ten = int(str(minu)[0])
                showminu = time_map_minu[minu_ten] + "십"
            else:
                showminu = "십"
            minu_one = int(str(minu)[1])
            showminu = showminu + time_map_minu[minu_one] + " 분"
        elif minu > 0:
            minu_one = int(str(minu)[0])
            showminu = showminu + time_map_minu[minu_one] + " 분"
        else:
            showminu = showminu + "정각"

        # 최종 출력 구문
        showtime = showhour + showminu + "이야."
        return showtime

def wciitext(hour=None):
    if hour == None:
        now = datetime.datetime.now()
        nowdate = now.strftime('%H')
        time_now = int(nowdate) // 2 + 1
    else:
        #이후에 24시간 기반 api가 구축되면 수정
        now = datetime.datetime.now()
        nowdate = now.strftime('%H')
        time_now = int(nowdate) // 2 + 1
    try:
        #24시간 기반 api 추가
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        url = urlopen(f'http://hyuns.space/api/hanguel/{time_now}/index.php', timeout=5)
        #url = urlopen(f'http://localhost:8080/api/{time_now}/index.php', timeout=3)
        soup = BeautifulSoup(url, "lxml")
        soup = str(soup.body)
        soup = soup.replace("<body>", "")
        soup = soup.replace("</body>", "")
        soup = soup.strip()
        showtext = soup
        return showtext

    except Exception as e:
        print(f"서버연결 오류발생 : {e}")
        writelog("neterror", e)

        time_now = int(nowdate)
        if time_now == 0:
            showtext = "좋은 꿈 꿔"
        elif time_now == 1:
            showtext = "헉?! 아직도 안 잤어?"
        elif time_now == 2:
            showtext = "아직 안 자고 뭐해?"
        elif time_now == 3:
            showtext = "음.. 졸리지 않니?"
        elif time_now == 4:
            showtext = "하아암.. 졸립당"
        elif time_now == 5:
            showtext = "지금 쯤이면 해가 뜰려나..?"
        elif time_now == 6:
            showtext = "벌써 새벽이네"
        elif time_now == 7:
            showtext = "상쾌한 아침"
        elif time_now == 8:
            showtext = "오늘은 뭐해?"
        elif time_now == 9:
            showtext = "힘쌔고 강한 아침!"
        elif time_now == 10:
            showtext = "지금은 뭐하시나..?"
        elif time_now == 11:
            showtext = "(대충 할 말이 없다는 말)"
        elif time_now == 12:
            showtext = "쩝..배고프당"
        elif time_now == 13:
            showtext = "밥 맛있게 먹었어?"
        elif time_now == 14:
            showtext = "더 열심히!"
        elif time_now == 15:
            showtext = "나른하당..ㅎ"
        elif time_now == 16:
            showtext = "헉 벌써"
        elif time_now == 17:
            showtext = "지금 뭐해?"
        elif time_now == 18:
            showtext = "슬슬 배고파진다 ㅎㅎ"
        elif time_now == 19:
            showtext = "해가 슬슬 지고 있겠네.." #계절마다 달라져야 함
        elif time_now == 20:
            showtext = "저녁 맛있게 먹었어?"
        elif time_now == 21:
            showtext = "벌써"
        elif time_now == 22:
            showtext = "오늘은 별이 보일려나?"
        elif time_now == 23:
            showtext = "슬슬 졸립지 않아?"
        elif time_now == 24:
            showtext = "좋은 꿈 꿔"

    return showtext

if __name__ == '__main__':
    print(wciitime())
    print(wciitext())