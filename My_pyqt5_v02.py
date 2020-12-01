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
import ffmpeg

print(dir(ffmpeg))

class Mainwindow(qtw.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        #my code goes here
        # self.button = qtw.QPushbutton("click me")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.select_btn.clicked.connect(self.show_data)
        self.ui.audio_btn.clicked.connect(self.cut_audio)

        # my ui code ends ere

        self.show()
    def callback(self):
        print("hello there")

    def cut_audio(self):
        video_name = self.ui.label_videoname.text()

        stream2 = probe = ffmpeg.probe(video_name)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        print(video_stream)
        self.ui.textEdit_data.append("Data:" + str(video_stream))

        audio_type = ""
        if self.ui.radioButton_mp3.isChecked():
            audio_type = "mp3"
            print
        elif self.ui.radioButton__wav.isChecked():
            audio_type = "wav"

        print(audio_type)
        stream = ffmpeg.input(video_name)
        a1 = stream.audio
        stream = ffmpeg.output(a1, 'my_test_output.' + audio_type)
        ffmpeg.run(stream)

    def export_section(self):
        pass

    def extract_srt(self):
        pass

    def convert_to_images(self):
        pass

    def generate_screenstots(self):
        pass

    def convert_codec(self):
        pass

    def exact_size(self):
        pass

    def show_data(self):
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
                self.ui.textEdit_data.append( "Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, Format: {t.format}".format(t=track))
                self.ui.textEdit_data.append("Duration (raw value):" +  str(track.duration) + '\n')
                self.ui.textEdit_data.append(str(track.other_duration))
                #self.ui.textEdit_data.setText(self.ui.textEdit_data.text() + str(track ))


            elif track.track_type == "Audio":
                print("Track audio-data:")
                pprint(track.to_data())
                data_dict = track.to_data()
                for key, val in data_dict.items():
                  print(key)
                  self.ui.textEdit_data.append("Track audio-data:" + str(key) + " : " + str(val))


        in_file = ffmpeg.input(videoname_url)
        probe = ffmpeg.probe(videoname_url)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        video_stream2 = next((stream for stream in probe['streams']), None)
        # width = int(video_stream['width'])
        # height = int(video_stream['height'])
        print(type(video_stream2))

        for key, value in video_stream2.items():
            print(key, " : ", value )
            file_data = str(key) +  " : " + str(value)
            
            self.ui.textEdit_data.append(str(file_data))
        
        # for stream_item in enumerate(video_stream2):
        #     print(video_stream2[stream_item])

        for my_data_x in probe['streams']:
            pass
            # print("*******************************************************")
            # print(my_data_x)

            # for my_data_y in probe[my_data_x]:
            #     print(   my_data_y,":", probe[my_data_x][my_data_y])
            



    def show_data_backup(self):
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
                data_dict = track.to_data()
                for key, val in data_dict.items():
                  print(key)
                  self.ui.textEdit_data.append("Track data:" + str(key) + " : " + str(val))

    def loop_video(self):
        pass



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = Mainwindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())


