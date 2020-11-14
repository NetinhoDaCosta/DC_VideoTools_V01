import sys
from interface import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import qtmodern.styles
import qtmodern.windows


class Mainwindow(qtw.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        #my code goes here
        # self.button = qtw.QPushbutton("click me")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.select_btn.clicked.connect(self.loop_video)





        # my ui code ends ere

        self.show()
    def callback(self):
        print("hello there")

    def loop_video(self):
        print("ok")
        fname = qtw.QFileDialog.getOpenFileName(self, 'Open file',
         'c:\\',"Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
        videoname_url = str(fname[0])
        self.ui.label_videoname.setText(videoname_url)




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    w = Mainwindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())


