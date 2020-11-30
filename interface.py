# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert_v01.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 1041)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 60))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../System_crawl_sequence_size_v01/System_crawl_sequence_size/red_logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setObjectName("select_btn")
        self.verticalLayout.addWidget(self.select_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_videoname = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_videoname.sizePolicy().hasHeightForWidth())
        self.label_videoname.setSizePolicy(sizePolicy)
        self.label_videoname.setObjectName("label_videoname")
        self.horizontalLayout_2.addWidget(self.label_videoname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.groupBox_create_new_sequence = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_create_new_sequence.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_create_new_sequence.sizePolicy().hasHeightForWidth())
        self.groupBox_create_new_sequence.setSizePolicy(sizePolicy)
        self.groupBox_create_new_sequence.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_create_new_sequence.setObjectName("groupBox_create_new_sequence")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_create_new_sequence)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sequence_btn = QtWidgets.QPushButton(self.groupBox_create_new_sequence)
        self.sequence_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.sequence_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.sequence_btn.setStyleSheet("")
        self.sequence_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/gallery.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sequence_btn.setIcon(icon)
        self.sequence_btn.setIconSize(QtCore.QSize(30, 30))
        self.sequence_btn.setObjectName("sequence_btn")
        self.horizontalLayout.addWidget(self.sequence_btn)
        self.radioButton_jpg = QtWidgets.QRadioButton(self.groupBox_create_new_sequence)
        self.radioButton_jpg.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton_jpg.setObjectName("radioButton_jpg")
        self.horizontalLayout.addWidget(self.radioButton_jpg)
        self.radioButton_png = QtWidgets.QRadioButton(self.groupBox_create_new_sequence)
        self.radioButton_png.setObjectName("radioButton_png")
        self.horizontalLayout.addWidget(self.radioButton_png)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox_create_new_sequence)
        self.groupBox_generate_screenshots = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_generate_screenshots.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_generate_screenshots.setObjectName("groupBox_generate_screenshots")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_generate_screenshots)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.screenshots_btn = QtWidgets.QPushButton(self.groupBox_generate_screenshots)
        self.screenshots_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.screenshots_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.screenshots_btn.setStyleSheet("")
        self.screenshots_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/scissors.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshots_btn.setIcon(icon1)
        self.screenshots_btn.setIconSize(QtCore.QSize(30, 30))
        self.screenshots_btn.setObjectName("screenshots_btn")
        self.horizontalLayout_8.addWidget(self.screenshots_btn)
        self.label_7 = QtWidgets.QLabel(self.groupBox_generate_screenshots)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.screenshot_frames = QtWidgets.QLineEdit(self.groupBox_generate_screenshots)
        self.screenshot_frames.setText("")
        self.screenshot_frames.setObjectName("screenshot_frames")
        self.horizontalLayout_8.addWidget(self.screenshot_frames)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_19)
        self.verticalLayout.addWidget(self.groupBox_generate_screenshots)
        self.groupBox_extract_audio = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_extract_audio.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_extract_audio.setObjectName("groupBox_extract_audio")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_extract_audio)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.audio_btn = QtWidgets.QPushButton(self.groupBox_extract_audio)
        self.audio_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.audio_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.audio_btn.setStyleSheet("")
        self.audio_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio_btn.setIcon(icon2)
        self.audio_btn.setIconSize(QtCore.QSize(30, 30))
        self.audio_btn.setObjectName("audio_btn")
        self.horizontalLayout_9.addWidget(self.audio_btn)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.radioButton_mp3 = QtWidgets.QRadioButton(self.groupBox_extract_audio)
        self.radioButton_mp3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton_mp3.setChecked(True)
        self.radioButton_mp3.setObjectName("radioButton_mp3")
        self.horizontalLayout_11.addWidget(self.radioButton_mp3)
        self.radioButton_wav = QtWidgets.QRadioButton(self.groupBox_extract_audio)
        self.radioButton_wav.setObjectName("radioButton_wav")
        self.horizontalLayout_11.addWidget(self.radioButton_wav)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.groupBox_extract_audio)
        self.groupBox_extract_srt = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_extract_srt.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_extract_srt.setObjectName("groupBox_extract_srt")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_extract_srt)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.srt_btn = QtWidgets.QPushButton(self.groupBox_extract_srt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srt_btn.sizePolicy().hasHeightForWidth())
        self.srt_btn.setSizePolicy(sizePolicy)
        self.srt_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.srt_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.srt_btn.setStyleSheet("")
        self.srt_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/video-conference.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.srt_btn.setIcon(icon3)
        self.srt_btn.setIconSize(QtCore.QSize(30, 30))
        self.srt_btn.setObjectName("srt_btn")
        self.horizontalLayout_12.addWidget(self.srt_btn)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.groupBox_extract_srt)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_16)
        self.verticalLayout.addWidget(self.groupBox_extract_srt)
        self.groupBox_convert_codec = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_convert_codec.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_convert_codec.setObjectName("groupBox_convert_codec")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_convert_codec)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.convert_codec_btn = QtWidgets.QPushButton(self.groupBox_convert_codec)
        self.convert_codec_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.convert_codec_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.convert_codec_btn.setStyleSheet("")
        self.convert_codec_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.convert_codec_btn.setIcon(icon4)
        self.convert_codec_btn.setIconSize(QtCore.QSize(30, 30))
        self.convert_codec_btn.setObjectName("convert_codec_btn")
        self.horizontalLayout_13.addWidget(self.convert_codec_btn)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_convert_codec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(160, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_codecs = QtWidgets.QComboBox(self.groupBox_convert_codec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_codecs.sizePolicy().hasHeightForWidth())
        self.comboBox_codecs.setSizePolicy(sizePolicy)
        self.comboBox_codecs.setObjectName("comboBox_codecs")
        self.comboBox_codecs.addItem("")
        self.comboBox_codecs.addItem("")
        self.comboBox_codecs.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_codecs)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_convert_codec)
        self.groupBox_extract_snippet = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_extract_snippet.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_extract_snippet.setObjectName("groupBox_extract_snippet")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_extract_snippet)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.snippet_btn = QtWidgets.QPushButton(self.groupBox_extract_snippet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snippet_btn.sizePolicy().hasHeightForWidth())
        self.snippet_btn.setSizePolicy(sizePolicy)
        self.snippet_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.snippet_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.snippet_btn.setStyleSheet("")
        self.snippet_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/video-editing.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snippet_btn.setIcon(icon5)
        self.snippet_btn.setIconSize(QtCore.QSize(30, 30))
        self.snippet_btn.setObjectName("snippet_btn")
        self.horizontalLayout_14.addWidget(self.snippet_btn)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_extract_snippet)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_startframe = QtWidgets.QLineEdit(self.groupBox_extract_snippet)
        self.lineEdit_startframe.setObjectName("lineEdit_startframe")
        self.horizontalLayout_5.addWidget(self.lineEdit_startframe)
        self.label_5 = QtWidgets.QLabel(self.groupBox_extract_snippet)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_duration = QtWidgets.QLineEdit(self.groupBox_extract_snippet)
        self.lineEdit_duration.setObjectName("lineEdit_duration")
        self.horizontalLayout_5.addWidget(self.lineEdit_duration)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox_extract_snippet)
        self.groupBox_loop_video = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_loop_video.sizePolicy().hasHeightForWidth())
        self.groupBox_loop_video.setSizePolicy(sizePolicy)
        self.groupBox_loop_video.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_loop_video.setObjectName("groupBox_loop_video")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_loop_video)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loop_btn = QtWidgets.QPushButton(self.groupBox_loop_video)
        self.loop_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.loop_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.loop_btn.setStyleSheet("")
        self.loop_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/rotation.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loop_btn.setIcon(icon6)
        self.loop_btn.setIconSize(QtCore.QSize(30, 30))
        self.loop_btn.setObjectName("loop_btn")
        self.horizontalLayout_3.addWidget(self.loop_btn)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.groupBox_loop_video)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.lineEdit_loops = QtWidgets.QLineEdit(self.groupBox_loop_video)
        self.lineEdit_loops.setObjectName("lineEdit_loops")
        self.horizontalLayout_15.addWidget(self.lineEdit_loops)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addWidget(self.groupBox_loop_video)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.textEdit_data = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_data.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.textEdit_data.setObjectName("textEdit_data")
        self.verticalLayout.addWidget(self.textEdit_data)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_btn.setText(_translate("MainWindow", "Select a video file to process"))
        self.label_2.setText(_translate("MainWindow", "Selected Video source:"))
        self.label_videoname.setText(_translate("MainWindow", "..."))
        self.groupBox_create_new_sequence.setTitle(_translate("MainWindow", "Convert to an image sequence"))
        self.radioButton_jpg.setText(_translate("MainWindow", "JPG sequence"))
        self.radioButton_png.setText(_translate("MainWindow", "PNG sequence"))
        self.groupBox_generate_screenshots.setTitle(_translate("MainWindow", "Generate screenshots / Extract frames"))
        self.label_7.setText(_translate("MainWindow", "Screenshot frames"))
        self.groupBox_extract_audio.setTitle(_translate("MainWindow", "Extract audio data from your video"))
        self.radioButton_mp3.setText(_translate("MainWindow", "MP3"))
        self.radioButton_wav.setText(_translate("MainWindow", "WAV"))
        self.groupBox_extract_srt.setTitle(_translate("MainWindow", "Extract a SRT (subtitle) file from your video"))
        self.label_9.setText(_translate("MainWindow", "Download embedded SRT data"))
        self.groupBox_convert_codec.setTitle(_translate("MainWindow", "Convert to another codec"))
        self.label_3.setText(_translate("MainWindow", "Select a codec to convert to:"))
        self.comboBox_codecs.setItemText(0, _translate("MainWindow", "mp4"))
        self.comboBox_codecs.setItemText(1, _translate("MainWindow", "mov"))
        self.comboBox_codecs.setItemText(2, _translate("MainWindow", "avi"))
        self.groupBox_extract_snippet.setTitle(_translate("MainWindow", "Extract a snippet/part of your video"))
        self.label_4.setText(_translate("MainWindow", "Start Frame:"))
        self.label_5.setText(_translate("MainWindow", "Duration (in frames):"))
        self.groupBox_loop_video.setTitle(_translate("MainWindow", "Loop your video"))
        self.label_8.setText(_translate("MainWindow", "How many loops?"))
        self.label_6.setText(_translate("MainWindow", "Video Data Analysis:"))
