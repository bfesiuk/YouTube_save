from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form
from pytube import YouTube


#CREATING APPLICATION
app = QtWidgets.QApplication(sys.argv)

#CRATING INTERFACE
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.setWindowTitle("YTsave")
Form.setWindowIcon(QtGui.QIcon("D:\\Projects\\YouTube_save\\file.png"))
Form.show()

#APLICATION LOGIC
def download():
	link_for_video = ui.edt_link.text()
	try :
		get_yt = YouTube(link_for_video)
		video = get_yt.streams.first()
		print(video.title)
	except :
		print("Something wrong 1")
	try :
		dirName = QtWidgets.QFileDialog.getExistingDirectory()
		print(dirName)
		video.download(dirName)
		print("Success")
	except :
		print("Something wrong 2")

ui.btn_download.clicked.connect(download)

#RUN APLICATION
sys.exit(app.exec_())
