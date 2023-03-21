# install pyqt5
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import*
class WebClass(QMainWindow):
    def __int__(self):
        super(QMainWindow, self).__int__()
        self.showMaximized()

        self.browser=QWebEngineView()
        self.setCentralWidget(self.browser)

        self.browser.setUrl(QUrl('http://google.com'))

        #===menus==
        self.menu=QToolBar()
        self.addToolBar(self.menu)

        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        self.menu.addAction(back_btn)

        next_btn = QAction('Next', self)
        next_btn.triggered.connect(self.browser.forward)
        self.menu.addAction(next_btn)

        reload_btn = QAction('Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        self.menu.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.browser.home_url)
        self.menu.addAction(home_btn)

        self.url_txt=QLineEdit()
        self.url_txt.returnPressed.connect(self.navigate_url)
        self.menu.addWidget(self.url_txt)

        self.browser.urlChanged.connect(self.update_url)

#================================================================

    def home_url(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_url(self):
        self.browser.setUrl(QUrl(self.url_txt))

    def update_url(self,u):
        self.url_txt.setText(u.tostring())


WebApp=QApplication(sys.argv)
QApplication.setApplicationName("Web browser - Developed by Sujan")
obj=WebClass()
WebApp.exec()


