import sys
from PyQt5 import QtWidgets,QtGui,uic
from PyQt5.QtWidgets import QMessageBox

import requests
from bs4 import BeautifulSoup


class home(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(home,self).__init__(parent)
        uic.loadUi("../venv/Lib/site-packages/QtDesigner/homepage.ui", self)
        self.show()
        self.start.clicked.connect(self.getstarted)

    def getstarted(self):
        self.hide()
        window = DashBoard(self)

class DashBoard(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(DashBoard,self).__init__(parent)
        uic.loadUi("../venv/Lib/site-packages/QtDesigner/movies.ui", self)
        self.show()
        self.cominsoon.clicked.connect(self.futureMovie)
        self.intheater.clicked.connect(self.currentMovie)

    def futureMovie(self):
        window = ComingSoon(self)

    def currentMovie(self):
        window = InTheaters(self)

class ComingSoon(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ComingSoon, self).__init__(parent)
        uic.loadUi("../venv/Lib/site-packages/QtDesigner/displaymovie.ui", self)
        self.show()
        website = requests.get('https://www.imdb.com/movies-coming-soon/2021-04/')
        soup = BeautifulSoup(website.content, 'html.parser')
        tags = soup.find_all('h4')
        count = 0
        for soups in tags:
            count += 1
            self.numbers.addItem(str(count))
            self.displaymovie.addItem(str(soups.string))

class InTheaters(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(InTheaters, self).__init__(parent)
        uic.loadUi("../venv/Lib/site-packages/QtDesigner/theaters.ui", self)
        self.show()

        website = requests.get('https://www.imdb.com/movies-in-theaters/?ref_=cs_inth')
        soup = BeautifulSoup(website.content, 'html.parser')
        tags = soup.find_all('h4')
        count = 0
        for soups in tags:
            count += 1
            self.numbers.addItem(str(count))
            self.displaymovie.addItem(str(soups.string))




app = QtWidgets.QApplication(sys.argv)
window = home()
app.setQuitOnLastWindowClosed(True)
app.exec_()