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
        self.ui.sequence_btn.clicked.connect(self.convert_to_images)
        self.ui.screenshots_btn.clicked.connect(self.generate_screenstots)
        self.ui.convert_codec_btn.clicked.connect(self.convert_codec)
        self.ui.convert_codec_btn.clicked.connect(self.convert_codec)
        self.ui.srt_btn.clicked.connect(self.extract_srt)

        # my ui code ends ere

        self.show()
    def callback(self):
        print("test")

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
        #get video file url
        file_url = self.ui.label_videoname.text()
        out_filename = str(file_url) + "image"
        print(file_url)

        split_url= file_url.split("/")
        kale_filename = split_url.pop(-1)
        kale_url = "/".join(split_url)
        print(kale_url)
        image_filename = kale_filename[:-4]
        print(image_filename)

        desired_image_extention = ".srt"

        image_output = str(kale_url) + "/" + str(image_filename) + str(desired_image_extention)
        image_output_file = str(kale_url) + "/" + str(image_filename)
        print(image_output)

        (
            ffmpeg
            .input(file_url)
            # .filter('scale', 1920, -1)
            #.output(image_output, vframes=1)
            .output("{}{}".format(image_output_file,desired_image_extention))
            .run()
        )


    def convert_to_images(self):

        #get video file url
        file_url = self.ui.label_videoname.text()
        out_filename = str(file_url) + "image"
        print(file_url)

        split_url= file_url.split("/")
        kale_filename = split_url.pop(-1)
        kale_url = "/".join(split_url)
        print(kale_url)
        image_filename = kale_filename[:-4]
        print(image_filename)

        desired_image_extention = ".jpg"
        if self.ui.radioButton_jpg.isChecked():
            desired_image_extention = ".jpg"
            print
        elif self.ui.radioButton_png.isChecked():
            desired_image_extention = ".png"

        image_output = str(kale_url) + "/" + str(image_filename) + str(desired_image_extention)
        image_output_file = str(kale_url) + "/" + str(image_filename)
        print(image_output)

        (
            ffmpeg
            .input(file_url)
            # .filter('scale', 1920, -1)
            #.output(image_output, vframes=1)
            .output("{}-%03d{}".format(image_output_file,desired_image_extention))
            .run()
        )


    def generate_screenstots(self):

        #screenshot_frames is inulveld van gewenste frames
        file_url = self.ui.screenshot_frames.text()
        print(file_url)

        screenshot_input_list = file_url.split(",")
        print(screenshot_input_list)

        file_url = self.ui.label_videoname.text()
        out_filename = str(file_url) + "image"
        print(file_url)

        split_url= file_url.split("/")
        kale_filename = split_url.pop(-1)
        kale_url = "/".join(split_url)
        print(kale_url)
        image_filename = kale_filename[:-4]
        print(image_filename)

        desired_image_extention = ".jpg"
        image_output = str(kale_url) + "/" + str(image_filename) + str(desired_image_extention)
        image_output_file = str(kale_url) + "/" + str(image_filename)

        screenshot = "_screenshot"
        image_output_file_sub = image_output_file + screenshot
        for screenshot_index, screenshot in enumerate(screenshot_input_list):
            print(screenshot)

            (
            ffmpeg
            .input(file_url)
            # .filter('scale', 1920, -1)
            .output("{}_{}_{}".format(image_output_file_sub, screenshot_index, desired_image_extention), vframes=1)
            .run()
            )


        pass

    def convert_codec(self):

        file_url = self.ui.label_videoname.text()
        out_filename = str(file_url) + "image"
        print(file_url)

        split_url= file_url.split("/")
        kale_filename = split_url.pop(-1)
        kale_url = "/".join(split_url)
        print(kale_url)
        image_filename = kale_filename[:-4]
        print(image_filename)

        codec_waarde = self.ui.comboBox_codecs.currentText()
        print(codec_waarde)
        if codec_waarde == "avi":
            desired_extention = ".avi"

        image_output = str(kale_url) + "/" + str(image_filename) + str(desired_extention)


        # ffmpeg -i Movie.mkv -map 0:s:0 subs.srt
        # -i: Input file URL/path.
        # -map: Designate one or more input streams as a source for the output file.
        # s:0: Select the subtitle stream.

        (
            ffmpeg
            .input(file_url)
            .filter('map', map=0)
            .filter('s',s=0)
            .output(image_output)
            .run()
        )


    def exact_size(self):
        pass

    def show_data(self):
        print("ok")
        fname = qtw.QFileDialog.getOpenFileName(self, 'Open file',
         'c:\\',"Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
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


