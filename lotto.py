import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from random import *
os.chdir("home15(lotto)\\Lotoreya")

os.system("cls")
class Ilova(QMainWindow):
    f=open("bilet.txt", "wt+")
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMaximumSize(1500,900)
        self.setMinimumSize(1500,900)
        self.setStyleSheet("""background-color:yellow;""")
        oyna=QWidget()

        #chap tarafi

        #Radiobutton turlari
        self.rdb=QButtonGroup()
        self.rdb1=QRadioButton("Omad (36/5)")
        self.rdb2=QRadioButton("Sharqona (36/6)")
        self.rdb3=QRadioButton("Omad (36/7)")
        self.rdb.addButton(self.rdb1)
        self.rdb.addButton(self.rdb2)
        self.rdb.addButton(self.rdb3)
        self.rdb.buttonClicked.connect(self.lotto_format)
        self.rdb_usul=QHBoxLayout()
        self.rdb_usul.addWidget(self.rdb1)
        self.rdb_usul.addWidget(self.rdb2)
        self.rdb_usul.addWidget(self.rdb3)


        #imkoniyatlarni kiritish
        self.kirit=QLabel()
        self.kirit.setStyleSheet("""
        width:300px;
        height:100px;
        size:300,100;
        background-color:white;
        """)
        self.plus=QPushButton("+")
        self.plus.clicked.connect(self.plus_yoz)
        self.plus.setStyleSheet("""
        background-color:grey;
        width:100px;
        height:100px;
        border:10px solid red;
        """)
        self.kirit_ly=QHBoxLayout()
        self.kirit_ly.addWidget(self.kirit)
        self.kirit_ly.addWidget(self.plus)

        #sonlarni kiritish
        self.buttons=QGridLayout()
        self.ls_son=[]
        sch=0
        self.raqam_gr=QButtonGroup()
        self.raqam_gr.buttonClicked[int].connect(self.raqam_yoz)
        self.raqam_gr.setExclusive(False)
        for x in range(6):
            for y in range(6):
                sch+=1
                btn=QPushButton()
                btn.setText(f"{sch}")
                btn.resize(40,40)
                self.knopka(btn)
                self.ls_son.append(btn)
                self.buttons.addWidget(self.ls_son[sch-1], x+1, y+1)
                self.raqam_gr.addButton(btn,sch)
                # self.raqam_gr.addButton(self.ls_son[sch-1],sch)
        # self.raqam_gr.buttonClicked.connect(lambda y:self.raqam_yoz)
        self.btn_telegram=QPushButton("Telegram")
        self.btn_youtb=QPushButton("You Tube")
        self.net=QHBoxLayout()
        self.net.addWidget(self.btn_telegram)
        self.net.addWidget(self.btn_youtb)
        

        
        #o'ng tarafi
        self.start=QPushButton("Start")
        self.start.setStyleSheet("background-color:red;")
        self.start.clicked.connect(self.start_ishla)
        self.ls_rand=[]
        self.rand_box=QHBoxLayout()
        self.rand_box.addWidget(self.start)
        for x in range(7):
            lbl_rand=QLabel()
            lbl_rand.resize(40,80)
            self.rand_style(lbl_rand)
            self.ls_rand.append(lbl_rand)
            self.rand_box.addWidget(self.ls_rand[x])
        self.chiqarish=QLabel("")
        self.chiqarish.resize(600,600)
        column2=QVBoxLayout()
        column2.addLayout(self.rand_box)   
        column2.addWidget(self.chiqarish) 
        

        #hammasini qo'shish
        column1=QVBoxLayout()
        column1.addLayout(self.rdb_usul)
        column1.addLayout(self.kirit_ly)
        column1.addLayout(self.buttons)
        column1.addLayout(self.net)
        final=QHBoxLayout()
        final.addLayout(column1)
        final.addLayout(column2)
        # final.addStretch()
        oyna.setLayout(final)
        # oyna.setStyleSheet("width: 1500;height:800;")
        self.setCentralWidget(oyna)



        #style berish
    def rdb_style(self, radio:QRadioButton):
        radio.setStyleSheet("""
            width:200px;
            height:100px;
        """)
    def knopka(sel, raqam:QPushButton):
        raqam.setStyleSheet("""
        width:40px;
        height:40px;
        border-radius:20px;
        background-color:pink;
        border:2px solid red;
        """)
    def rand_style(self, lbl):
        lbl.setStyleSheet("""
        border-radius:25px;
        background-color:orange;
        border:2px solid black;
        size:50px,50px;
        """)
    #dastur logikasi
    n_format=0
    def lotto_format(self):
        if self.rdb1.isChecked():
            Ilova.n_format=5
        elif self.rdb2.isChecked():
            Ilova.n_format=6
        else:
            Ilova.n_format=7
        self.rdb1.setEnabled(False)
        self.rdb2.setEnabled(False)
        self.rdb3.setEnabled(False)


    def raqam_yoz(self, id):
        kt=self.kirit.text().split()
        if len(kt)<Ilova.n_format:
            for btn in self.raqam_gr.buttons():
                if btn is self.raqam_gr.button(id):
                    matn=self.kirit.text()+" "+btn.text()
                    self.kirit.setText(matn)
                    # btn.setEnabled(False)
                    btn.setDisabled(True)
    def plus_yoz(self):
        ls=[]
        ls.append(self.kirit.text())
        if len(self.kirit.text().split())==Ilova.n_format:
            Ilova.f.write(self.kirit.text()+"\n")
            self.kirit.setText("")
            for btn in self.raqam_gr.buttons():    
                btn.setDisabled(False)
    def start_ishla(self):
        Ilova.f.close()
        self.random_chiq()
    def random_chiq(self):
        rnum=[]
        while len(rnum)<Ilova.n_format:
            num=randint(1,36)
            if num not in rnum:
                rnum.append(num)
        for x in range(Ilova.n_format):
            self.ls_rand[x].setText(f"{rnum[x]}")
        fayl=open("bilet.txt", "r")
        fayl.read()
        hajm=fayl.tell()
        fayl.seek(0)
        
        pop_count=0
        p=fayl.tell()
        while p!=hajm:
            pop_count+=1
            popitka=fayl.readline().split()
            sch=0
            for x in range(Ilova.n_format):
                if popitka[x]==rnum[x]:
                    sch+=1
            matn=self.chiqarish.text()+f"{pop_count}-biletda {sch} ta to'g'ri\n"
            self.chiqarish.setText(matn)
            self.chiqarish.setStyleSheet("color:blue; font-size:30px;")
            p=fayl.tell()
        Ilova.yangi=self.chiqarish.text()
        self.project=Oyna()
        self.project.show()
        self.hide()
class Oyna(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet("""
        QMainWindow 
        {background-color:yellow;}
        
        QPushButton
        {background-color:black;
        color:rgb(55,205,55);
        border:5px solid rgb(55,205,55);
        border-radius:15px;
        }
        """)
        self.setWindowTitle("")
        self.setMaximumSize(750, 500)
        self.setMinimumSize(750, 500)
        self.btn=QPushButton("goto 1-window", self)
        self.btn.setFont(QFont("Consolas", 20))
        self.btn.setGeometry(300,435,350,50)
        self.btn.clicked.connect(self.main_window)
        self.tedit=QLabel(self)
        self.tedit.setStyleSheet("""
        background-color:white;
        """)
        self.tedit.setGeometry(50,50,250,100)
        self.tedit.setText(Ilova.yangi)
    def main_window(self):
        self.application=Ilova()
        self.application.show()
        self.hide()

app=QApplication(sys.argv)
dastur=Ilova()
dastur.show()
sys.exit(app.exec_())