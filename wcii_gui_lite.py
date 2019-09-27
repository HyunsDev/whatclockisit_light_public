#-*- coding: utf-8 -*-
import sys
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from WTFerror import *
import wcii_var
from wcii_wallpaper import *

try:
    wc = wcii_var.wcii()
    class wcii_lite(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setWindowTitle('지금몇시계 라이트')
            self.setWindowIcon(QIcon('dsource/wcii_icon.png'))
            self.center()
            self.setFixedSize(300, 400)

            grid = QGridLayout()
            grid.addWidget(self.setwall(), 0, 0)
            grid.addWidget(self.showwall(), 1, 0)
            grid.addWidget(self.killui(), 2 , 0)

            self.setLayout(grid)
            self.show()
        try:
            def setwall(self):
                groupbox = QGroupBox('배경화면 설정하기')

                mainui = QVBoxLayout()
                setwall = QHBoxLayout()
                defwall = QHBoxLayout()

                self.wallpaper_lable = QLabel("배경사진 변경")
                self.wallpaper_button = QPushButton("파일 선택하기")
                self.wallpaper_button.clicked.connect(self.select_wallpaper)

                setwall.addWidget(self.wallpaper_lable)
                setwall.addWidget(self.wallpaper_button)

                self.wallpaper_def_lable = QLabel("배경사진 초기화")
                self.wallpaper_def_button = QPushButton("기본 값으로 설정하기")
                self.wallpaper_def_button.clicked.connect(self.def_wallpaper)

                defwall.addWidget(self.wallpaper_def_lable)
                defwall.addWidget(self.wallpaper_def_button)

                mainui.addLayout(setwall)
                mainui.addLayout(defwall)
                groupbox.setLayout(mainui)
                return groupbox

            def showwall(self):
                groupbox = QGroupBox('배경사진 미리보기')
                showwall = QHBoxLayout()
                self.pixmap = QPixmap(wc.appimage).scaledToWidth(250)
                self.img = QLabel()
                self.img.setPixmap(self.pixmap)

                showwall.addWidget(self.img)
                groupbox.setLayout(showwall)
                return groupbox

            def killui(self):
                groupbox = QGroupBox('무시무시한 버튼')
                redbu = QHBoxLayout()
                self.redbutton = QPushButton('지금몇시계 끄기')
                self.redbutton.clicked.connect(self.killwcii)

                redbu.addWidget(self.redbutton)
                groupbox.setLayout(redbu)
                return groupbox

            def center(self):
                qr = self.frameGeometry()
                cp = QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

            def killwcii(self):
                reply = QMessageBox.question(self, '지금몇시계 라이트를 내쫒으실 건가요...?', "지금몇시계 라이트를 종료하시겠습니까?\n(코어가 실행되지 않았더라도 이 창은 뜨니 오해말아주세요!)",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    with open(wc.appdata, "w") as f:
                        f.write("kill")
                    QMessageBox.information(self, "지금몇시계 라이트를 종료했습니다", "시계를 켜실려면 다시 코어를 실행해주세요!")
                    stop_wallpaper()
                    sys.exit(app.exec_())

            def select_wallpaper(self):
                title = "배경사진을 골라주세요"
                filter = "사진 파일(*.png)"
                wp_link = QFileDialog.getOpenFileName(self, title, None, filter)
                if wp_link[0] != "":
                    shutil.copyfile(wp_link[0], wc.appimage)
                    self.pixmap = QPixmap(wc.appimage).scaledToWidth(250)
                    self.img.setPixmap(self.pixmap)
                    QApplication.processEvents()
                    QMessageBox.information(self, "바탕화면 변경 완료!", "바탕화면 변경 완료!")
                    if corelive() == True:
                        wcii_wallpaper()
                    else:
                        stop_wallpaper()


            def def_wallpaper(self):
                shutil.copyfile(wc.dimage, wc.appimage)
                self.pixmap = QPixmap(wc.appimage).scaledToWidth(250)
                self.img.setPixmap(self.pixmap)
                QApplication.processEvents()
                QMessageBox.information(self, "바탕화면 초기화 완료!", "바탕화면 초기화 완료!")
                if corelive() == True:
                    wcii_wallpaper()
                else:
                    stop_wallpaper()



        #오류 제어 1단 : GUI 에러
        except Exception as e:
            errorwindow(e)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = wcii_lite()
        sys.exit(app.exec_())

#오류 제어 2단 : 모든 부분에서의 에러 처리
except Exception as e:
    errorwindow(e)