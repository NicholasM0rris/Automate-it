from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import sys
import random
import pyqtgraph as pg


from selenium.webdriver.common.keys import Keys

username = "44373388"
password = "Morris"
module = 3
question = 2
delay = 2
increment = 5
start_value = 0


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        # ui = GUI(display)
        self.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle("Early development user interface A204 V2.31")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.begin_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.begin_pushButton.setGeometry(QtCore.QRect(564, 460, 205, 81))
        self.begin_pushButton.clicked.connect(self.start_button_function)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.begin_pushButton.setFont(font)
        self.begin_pushButton.setObjectName("begin_pushButton")
        self.increment_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.increment_doubleSpinBox.setGeometry(QtCore.QRect(222, 390, 145, 67))
        self.increment_doubleSpinBox.setSingleStep(0.01)
        self.increment_doubleSpinBox.setObjectName("increment_doubleSpinBox")
        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(136, 32, 321, 61))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(136, 110, 321, 61))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.question_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.question_spinbox.setGeometry(QtCore.QRect(220, 310, 147, 67))
        self.question_spinbox.setObjectName("question_spinbox")
        self.module_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.module_spinbox.setGeometry(QtCore.QRect(220, 228, 147, 67))
        self.module_spinbox.setObjectName("module_spinbox")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(10, 42, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(12, 124, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.module_label = QtWidgets.QLabel(self.centralwidget)
        self.module_label.setGeometry(QtCore.QRect(46, 244, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.module_label.setFont(font)
        self.module_label.setObjectName("module_label")
        self.question_label = QtWidgets.QLabel(self.centralwidget)
        self.question_label.setGeometry(QtCore.QRect(44, 328, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.question_label.setFont(font)
        self.question_label.setObjectName("question_label")
        self.increment_label = QtWidgets.QLabel(self.centralwidget)
        self.increment_label.setGeometry(QtCore.QRect(46, 406, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.increment_label.setFont(font)
        self.increment_label.setObjectName("increment_label")
        self.increment_doubleSpinBox.setSingleStep(0.0001)
        self.increment_doubleSpinBox.setMinimum(0.00001)
        self.delay_label = QtWidgets.QLabel(self.centralwidget)
        self.delay_label.setGeometry(QtCore.QRect(50, 492, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delay_label.setFont(font)
        self.delay_label.setObjectName("delay_label")
        self.delay_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.delay_doubleSpinBox.setGeometry(QtCore.QRect(222, 474, 145, 67))
        self.delay_doubleSpinBox.setSingleStep(0.01)
        self.delay_doubleSpinBox.setObjectName("delay_doubleSpinBox")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(606, 378, 169, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.current_value_label = QtWidgets.QLabel(self.centralwidget)
        self.current_value_label.setGeometry(QtCore.QRect(458, 394, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_value_label.setFont(font)
        self.current_value_label.setObjectName("current_value_label")
        self.starting_value_label = QtWidgets.QLabel(self.centralwidget)
        self.starting_value_label.setGeometry(QtCore.QRect(454, 306, 137, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.starting_value_label.setFont(font)
        self.starting_value_label.setObjectName("starting_value_label")
        self.startingvalue_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.startingvalue_doubleSpinBox.setGeometry(QtCore.QRect(608, 280, 167, 77))
        self.startingvalue_doubleSpinBox.setSingleStep(0.0001)
        self.startingvalue_doubleSpinBox.setMaximum(100000)
        self.startingvalue_doubleSpinBox.setMinimum(0.00001)
        self.startingvalue_doubleSpinBox.setObjectName("startingvalue_doubleSpinBox")
        self.movie_label = QtWidgets.QLabel(self.centralwidget)
        self.movie = QMovie("typing_away.gif")
        self.movie_label.setMovie(self.movie)
        self.movie.start()
        self.movie_label.setGeometry(QtCore.QRect(472, 30, 303, 205))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(394, 460, 159, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.stop_pushButton.setFont(font)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.stop_pushButton.clicked.connect(self.stop_button_function)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.begin_pushButton.setText(_translate("MainWindow", "Begin!"))
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.username_lineEdit.setText(_translate("MainWindow", "44373388"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.password_lineEdit.setText(_translate("MainWindow", "Morris"))
        self.module_label.setText(_translate("MainWindow", "Module:"))
        self.question_label.setText(_translate("MainWindow", "Question:"))
        self.increment_label.setText(_translate("MainWindow", "Increment:"))
        self.delay_label.setText(_translate("MainWindow", "Delay:"))
        self.current_value_label.setText(_translate("MainWindow", "Current value:"))
        self.starting_value_label.setText(_translate("MainWindow", "Starting value:"))
        self.stop_pushButton.setText(_translate("MainWindow", "STOP"))

    def stop_button_function(self):
        save_answer(self.lcdNumber.value(), module, question, False)
        pg.exit()

    def start_button_function(self):
        global username
        global password
        global module
        global question
        global delay
        global increment
        global start_value
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        module = self.module_spinbox.value()
        question = self.question_spinbox.value()
        delay = self.delay_doubleSpinBox.value()
        increment = self.increment_doubleSpinBox.value()
        start_value = self.startingvalue_doubleSpinBox.value()
        self.worker = Worker(self)
        self.worker.start()
        print("Start success")


def login(driver):
    try:
        id_field = driver.find_element_by_name("id")
        id_field.send_keys(username)
        pass_field = driver.find_element_by_name('pwd')
        pass_field.send_keys(password)
        submit = driver.find_element_by_css_selector("input[type='submit']")
        submit.click()
        print(submit)
    except NoSuchElementException:
        print("login error")
        sys.exit()


def select_module(d, module):
    try:
        module = d.find_element_by_css_selector("input[type='radio'][value='{}']".format(module))
        module.click()
        submit = d.find_element_by_css_selector("input[type='submit']")
        submit.click()
    except NoSuchElementException:
        print("Module select error")
        sys.exit()


def select_question(d, q):
    try:
        q = d.find_element_by_css_selector("input[type='radio'][value='{}']".format(q))
        q.click()
        submit = d.find_element_by_css_selector("input[type='submit']")
        submit.click()
    except NoSuchElementException:
        print("Question select error")
        sys.exit()


def answer_question(d, gui):
    passed = False
    value = start_value
    while not passed:
        time.sleep(random.uniform(0, delay))
        try:

            fields = d.find_elements_by_name("answer[]")
            fields[0].send_keys(str(value))
            submit = d.find_element_by_css_selector("input[type='submit']")
            submit.click()

            result = d.find_elements_by_tag_name("p")
            words = []
            for t in result:
                words.append(t.text)

            words = " ".join(words).split()
            # print(words)

            if 'CORRECT!' in words:
                passed = True
                print("ANSWER: {}".format(value))
                save_answer(value, module, question, True)
                pg.exit()
            elif 'INCORRECT!' in words:
                print("{} was INCORRECT!".format(value))
                time.sleep(random.uniform(0, delay))
                reload_question(d)

            elif 'CLOSE' in words:
                print("{} was CLOSE!".format(value))
                time.sleep(random.uniform(0, delay))
                reload_question(d)

            else:
                passed = False
                time.sleep(random.uniform(0, delay))
                reload_question(d)

            value += increment
            gui.lcdNumber.display(value)


        except NoSuchElementException:
            print("Answering error")
            print("value", value)
            sys.exit()
        except IndexError:
            print("moved forward")
            d.forward()


def reload_question(d):
    d.back()
    time.sleep(random.uniform(0, delay))
    d.refresh()


def save_answer(answer, m, q, answered):
    filename = str("answers/M{}Q{}.txt".format(m, q))
    with open(filename, 'w+') as f:
        if answered:
            f.write('Answer: ' + str(answer))
        else:
            f.write('current value: ' + str(answer))
        f.close()


class Worker2(QThread):
    def __init__(self, gui, parent=None):
        QThread.__init__(self, parent)
        self.gui = gui
        print("s1")

    def run(self):
        print("s2")


class Worker(QThread):
    """
       Worker thread
       """

    def __init__(self, gui, parent=None):
        QThread.__init__(self, parent)
        self.gui = gui

    def run(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1024x768")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('log-level=3')
        driver = webdriver.Chrome(
            'C:\\Users\\nicho\\PycharmProjects\\automate_it\\chromedriver\\chromedriver.exe',
            options=chrome_options)

        # query = "Testing this stuff"
        # query = query.replace(' ', '+')
        # driver.get('http://www.google.com/search?q=' + query)
        # user_input = input("Ready?")
        website = "http://huygens.zones.eait.uq.edu.au/courses/mech3250/OnlineTutorials/yat_door.php"
        driver.get(website)

        login(driver)
        time.sleep(random.uniform(0, 1))
        select_module(driver, module)
        time.sleep(random.uniform(0, 1))
        select_question(driver, question)
        time.sleep(random.uniform(0, 1))
        answer_question(driver, gui=self.gui)

        # answer = driver.execute_script("return document.elementFromPoint(350, 230);").text
        time.sleep(5)
        driver.close()
        self.quit()


def main(arglist):
    app = QApplication([])
    app.aboutToQuit.connect(app.deleteLater)
    # gui = interface.GUI(display)
    gui = GUI()
    app.exec_()
    save_answer(gui.lcdNumber.value(), module, question, True)
    pg.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
