from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
with open('Dictionary.txt') as lugat:
    lugat = lugat.read().split('\n')

class ADD(QWidget):
    def __init__(self):
        super().__init__()

        self.hBtnEditLay = QHBoxLayout()
        self.vEditLay = QVBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engEdit = QLineEdit()
        self.engEdit.setPlaceholderText("Eng...")

        self.uzEdit = QLineEdit()
        self.uzEdit.setPlaceholderText("Uzb...")

        self.okBtn = QPushButton("OK")
        self.okBtn.clicked.connect(self.ok)

        self.natijaLbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.vEditLay.addWidget(self.engEdit)
        self.vEditLay.addWidget(self.uzEdit)

        self.hBtnEditLay.addLayout(self.vEditLay)
        self.hBtnEditLay.addWidget(self.okBtn)

        self.vMainLay.addLayout(self.hBtnEditLay)
        self.vMainLay.addWidget(self.natijaLbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def ok(self):
        if self.engEdit.text() == '' or self.uzEdit.text() == '':
            self.natijaLbl.setText('Error')
            self.natijaLbl.adjustSize()
        else:
            count = 0
            for i in lugat:
                i = i.split()
                if self.engEdit.text() == i[0] or self.uzEdit.text() == i[1]:
                    self.natijaLbl.setText("The word is in the dictionary")
                    self.natijaLbl.adjustSize()
                    count = 1
            if count==0:
                lugat.append(f"{self.engEdit.text()}{' '*(20-len(self.engEdit.text()))}{self.uzEdit.text()}")
                self.natijaLbl.setText("Added")
        self.engEdit.clear()
        self.uzEdit.clear()

    def menu(self):
        self.engEdit.clear()
        self.uzEdit.clear()
        self.natijaLbl.setText('')
        self.close()

class SEARCH(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hRadioLay = QHBoxLayout()
        self.hEditBtnLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.EngRadio = QRadioButton("Englsih")
        self.EngRadio.setChecked(True)
        self.UzRadio = QRadioButton('Uzbek')

        self.Edit = QLineEdit()

        self.searchBtn = QPushButton("search")
        self.searchBtn.clicked.connect(self.search)

        self.lbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.hRadioLay.addWidget(self.EngRadio)
        self.hRadioLay.addWidget(self.UzRadio)

        self.hEditBtnLay.addWidget(self.Edit)
        self.hEditBtnLay.addWidget(self.searchBtn)

        self.vMainLay.addLayout(self.hRadioLay)
        self.vMainLay.addLayout(self.hEditBtnLay)
        self.vMainLay.addWidget(self.lbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def search(self):
        global lugat
        booll = True 
        if self.EngRadio.isChecked():
            for i in lugat:
                i = i.split()
                if i[0] == self.Edit.text():
                    self.lbl.setText(i[1])
                    self.lbl.adjustSize()
                    booll = False
        elif self.UzRadio.isChecked():
            for i in lugat:
                i = i.split()
                if i[1] == self.Edit.text():
                    self.lbl.setText(i[0])
                    self.lbl.adjustSize()
                    booll = False
        if booll:
            self.lbl.setText("Error")
            self.lbl.adjustSize()

    def menu(self):
        self.lbl.clear()
        self.Edit.clear()
        self.close()

class LIST(QWidget):
    def __init__(self):
        super().__init__()

        self.hLblLay = QHBoxLayout()
        self.hListWidgLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engLbl = QLabel("English")
        self.uzLbl = QLabel("Uzbek")

        self.engListWdg = QListWidget()
        self.uzListWdg = QListWidget()

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        global lugat

        cpy = lugat.copy()
        for i in range(len(cpy)):
            cpy[i] = cpy[i].split()
            self.engListWdg.addItem(cpy[i][0])
            self.uzListWdg.addItem(cpy[i][1])

        self.hLblLay.addWidget(self.engLbl)
        self.hLblLay.addWidget(self.uzLbl)

        self.hListWidgLay.addWidget(self.engListWdg)
        self.hListWidgLay.addWidget(self.uzListWdg)

        self.vMainLay.addLayout(self.hLblLay)
        self.vMainLay.addLayout(self.hListWidgLay)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def menu(self):
        self.engListWdg.clear()
        self.uzListWdg.clear()
        self.close()

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.addWindow = ADD()
        self.searchWindow = SEARCH()

        self.vBtnLay = QVBoxLayout()
        self.hMainLay = QHBoxLayout()

        self.addBtn = QPushButton("ADD")
        self.addBtn.clicked.connect(lambda: self.addWindow.show())

        self.searchBtn = QPushButton("SEARCH")
        self.searchBtn.clicked.connect(self.searchWindow.show)
        
        self.listBtn = QPushButton("LIST")
        self.listBtn.clicked.connect(self.showww)

        self.exitBtn = QPushButton("EXIT")
        self.exitBtn.clicked.connect(self.exit)

        self.vBtnLay.addWidget(self.addBtn)
        self.vBtnLay.addWidget(self.searchBtn)
        self.vBtnLay.addWidget(self.listBtn)
        self.vBtnLay.addWidget(self.exitBtn)

        self.hMainLay.addStretch()
        self.hMainLay.addLayout(self.vBtnLay)
        self.hMainLay.addStretch()
        self.setLayout(self.hMainLay)

    def showww(self):
        self.listWindow = LIST()
        self.listWindow.show()

    def exit(self):
            global lugat
            
            with open("dictionary.txt","w") as file:
                for i in range(len(lugat)):
                    if i != len(lugat)-1:
                        file.write(f"{lugat[i]}\n")
                    else:
                        file.write(f"{lugat[i]}")
            self.close()

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()