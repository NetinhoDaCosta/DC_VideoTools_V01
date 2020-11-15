import sys
from interface import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import qtmodern.styles
import qtmodern.windows
from ffprobe import FFProbe
from pprint import pprint
from pymediainfo import MediaInfo


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

        data_list =[]
        media_info = MediaInfo.parse(videoname_url)
        for track in media_info.tracks:

            if track.track_type == "Video":
                print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
                    "Format: {t.format}".format(t=track)
                )
                print("Duration (raw value):", track.duration)
                #print("Duration (other values:")
                pprint(track.other_duration)
                self.ui.textEdit_data.append( "Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
                    "Format: {t.format}".format(t=track))
                self.ui.textEdit_data.append("Duration (raw value):" +  str(track.duration) + '\n')
                self.ui.textEdit_data.append("Duration (other values:")
                #self.ui.textEdit_data.setText(self.ui.textEdit_data.text() + str(track ))


            elif track.track_type == "Audio":
                print("Track data:")
                pprint(track.to_data())
                self.ui.textEdit_data.append("Track data:" + str(track.to_data()))







if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    w = Mainwindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())


