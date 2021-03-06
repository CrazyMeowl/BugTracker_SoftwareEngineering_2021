try:
	import sys
	import time
	from PyQt5 import QtGui
	from PyQt5.uic import loadUi
	from PyQt5 import QtWidgets
	from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QMainWindow,QMessageBox
	from PyQt5.QtCore import QDate
	from os import environ
	import requests
	import signin_ui
	import signup_ui
	import main_menu_admin_ui
	import main_menu_customer_ui
	import main_menu_staff_ui
	import report_ui
	import popup_ui
	import welcome_ui
	import webbrowser

	#mandatory
	def suppress_qt_warnings():
		environ["QT_DEVICE_PIXEL_RATIO"] = "0"
		environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
		environ["QT_SCREEN_SCALE_FACTORS"] = "1"
		environ["QT_SCALE_FACTOR"] = "1"
	'''
	class MainMenuAdmin(QDialog):
		def __init__(self):
			QDialog.__init__(self)
			loadUi("main_menu_admin.ui",self)
	'''

	class User():
		def __init__(self):
			self.id = 0
			self.requestAt = 0
			self.expiresIn = 0
			self.accessToken = 0
			self.roles = 0
		def updateData(self,infolist):
			self.id = infolist['id']
			self.requestAt = infolist['requestAt']
			self.expiresIn = infolist['expiresIn']
			self.accessToken = infolist['accessToken']
			self.roles = infolist['roles']
		def signout(self):
			self.id = 0
			self.requestAt = 0
			self.expiresIn = 0
			self.accessToken = 0
			self.roles = 0

	class App():
		def __init__(self,infolist):
			self.name = infolist['name']
			self.logoURL = infolist['logoURL']
			self.companyId = infolist['companyId']
			self.id = infolist['id']

	class Report():
		def __init__(self,infolist):
			self.title = infolist['title']
			self.description = infolist['description']
			self.appId = infolist['appId']
			self.id = infolist['id']

	class Bug():
		def __init__(self,infolist):
			self.title = infolist['title']
			self.serverity = infolist["serverity"]
			self.status = infolist["status"]
			self.description = infolist['description']
			self.appId = infolist['appId']
			self.id = infolist['id']
			self.serverities_list = ["Small","Normal","Bad","Extreme","EMERGENCY"]
			self.status_list = ["Working","Fixed","Revised","Approved"]
	class WelcomeScreen(QDialog):
		def __init__(self):
			super(WelcomeScreen, self).__init__()
			self.ui = welcome_ui.Ui_Dialog()
			self.ui.setupUi(self)
			self.ui.signin_button.clicked.connect(self.gotosignin)
			self.ui.signup_button.clicked.connect(self.gotosignup)

		def gotosignin(self):
			widget.setCurrentIndex(signin_index)

		def gotosignup(self):
			widget.setCurrentIndex(signup_index)

	user = User()
	class SignInScreen(QDialog):
		def __init__(self):
			super(SignInScreen, self).__init__()
			self.ui = signin_ui.Ui_Dialog()
			self.ui.setupUi(self)
			self.ui.password_box.setEchoMode(QtWidgets.QLineEdit.Password)
			self.ui.signin_button.clicked.connect(self.signinfunction)
			self.ui.back_button.clicked.connect(self.back)

		def back(self):
			widget.setCurrentIndex(welcomescreen_index)

		def signinfunction(self):
			username = self.ui.username_box.text()
			password = self.ui.password_box.text()
			#print(username,password)
			
			if len(username)==0 or len(password)==0:
				self.ui.error.setText("Please input all fields.")
			
			else:
				self.ui.error.setText("")
				r = requests.post('https://bugtracker-api.azurewebsites.net/api/Auth', json={
				"userName": username,
				"password": password
				})
				''' DEBUG Only
				print(f"Status Code: {r.status_code}, Response: {r.json()}")
				for i in r.json():
					print(i,":",r.json()[i],type(r.json()[i]))
				'''
				if r.status_code == 400:
					self.ui.error.setText("Invalid username or password")
				elif r.status_code == 200:
					a = r.json()
					print(r.json())
					user.updateData(a)
					if "staff" in user.roles:
						#print("ADMIN")
						print("hello")
						widget.setCurrentIndex(menu_staff_index)
						mainmenustaffscreen.load_app_list()
					if "admin" in user.roles:
						#print("ADMIN")
						widget.setCurrentIndex(menu_admin_index)
					if "customer" in user.roles:
						#print("Customer")
						widget.setCurrentIndex(menu_customer_index)
					self.ui.username_box.clear()
					self.ui.password_box.clear()
					#self.ui.error.setText("")

	class PopupScreen(QDialog):
		def __init__(self):
			super(PopupScreen, self).__init__()
			self.ui = popup_ui.Ui_Dialog()
			self.ui.setupUi(self)
			self.ui.email_button.clicked.connect(self.open_email)
			self.setWindowTitle("Create Company Ui")
			self.setWindowIcon(QtGui.QIcon('logo.png'))

		def open_email(self):
			recipient = 'ITITIU19185@student.hcmiu.edu.vn'
			subject = 'Create Company Request'
			body = 'Hello im ... Owner of ... . I would like to create a company on your BugTracker app'
			body = body.replace(' ', '%20')
			webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)

	class SignUpScreen(QDialog):
		def __init__(self):
			super(SignUpScreen, self).__init__()
			self.ui = signup_ui.Ui_Dialog()
			self.ui.setupUi(self)
			self.ui.password_box.setEchoMode(QtWidgets.QLineEdit.Password)
			self.ui.confirm_password_box.setEchoMode(QtWidgets.QLineEdit.Password)
			self.ui.signup_button.clicked.connect(self.signupfunction)
			self.ui.back_button.clicked.connect(self.back)
			self.ui.create_company_button.clicked.connect(self.popupemail)
			self.date = QDate.currentDate()
			self.ui.birthdate_box.setDate(self.date)

		def popupemail(self):
			self.popupscreen = PopupScreen()
			#self.popupscreen.setFixedHeight(800)
			#self.popupscreen.setFixedWidth(1200)
			self.popupscreen.raise_()
			self.popupscreen.show()

		def back(self):
			widget.setCurrentIndex(0)

		def signupfunction(self):
			username = self.ui.username_box.text()
			password = self.ui.password_box.text()
			confirmpassword = self.ui.confirm_password_box.text()
			fullname = self.ui.fullname_box.text()
			email = self.ui.email_box.text()
			birthdate_year = self.ui.birthdate_box.date().year()
			birthdate_month = self.ui.birthdate_box.date().month()
			birthdate_date = self.ui.birthdate_box.date().day()
			birthdate = f"{birthdate_date}/{birthdate_month}/{birthdate_year}"
			print(birthdate)
			if len(username)==0 or len(password)==0 or len(confirmpassword)==0:
				self.ui.error.setText("Please fill in all inputs.")

			elif password!=confirmpassword:
				self.ui.error.setText("Passwords do not match.")
			elif "@" not in email:
				self.ui.error.setText("Please enter a valid email.")
			elif ' ' in username:
				self.ui.error.setText("Please remove space from your username.")
			else:
				self.ui.error.setText("")
				r = requests.post('https://bugtracker-api.azurewebsites.net/api/Customer/Create', json={
				"userName": username,
				"password": password,
				"fullName": fullname,
				"email": email,
				"birthdate": birthdate
				})
				print(r)
				print(f"Status Code: {r.status_code}, Response: {r.json()}")
				for i in r.json():
					print(i,":",r.json()[i],type(r.json()[i]))
				if r.status_code == 400:
					self.ui.error.setText("Username was taken.")
				else:
					self.ui.error.setText("You shouldn't see this line, or should you?")
					widget.setCurrentIndex(menu_customer_index)
					self.ui.username_box.clear()
					self.ui.password_box.clear()
					self.ui.confirm_password_box.clear()
					self.ui.fullname_box.clear()
					self.ui.email_box.clear()
					self.ui.birthdate_box.setDate(self.date)
	class MainMenuAdminScreen(QDialog):
		def __init__(self):
			super(MainMenuAdminScreen, self).__init__()
			self.side_menu_state = False
			self.itemSelectionDetected = False
			self.ui = main_menu_admin_ui.Ui_Dialog()
			self.ui.setupUi(self)

			self.ui.slide_menu_container.setMaximumWidth(0)
			self.ui.exit_button.clicked.connect(sys.exit)
			self.ui.menu_button.clicked.connect(self.trigger_side_menu)
			self.ui.refresh_button.clicked.connect(self.reload_app_list)
			self.ui.search_button.clicked.connect(self.search_for_app)
			self.ui.report_button.clicked.connect(self.report_app)
			self.ui.website_button.clicked.connect(self.open_link)
			self.ui.email_button.clicked.connect(self.open_email)
			self.ui.app_list.itemSelectionChanged.connect(self.on_change_app)
			self.ui.signout_button.clicked.connect(self.signout)
			self.app_list = []
			self.load_app_list()
		def signout(self):
			user.signout()
			widget.setCurrentIndex(welcomescreen_index)
		def on_change_app(self):
			self.itemSelectionDetected = True
				
		def open_email(self):
			recipient = 'ITITIU19185@student.hcmiu.edu.vn'
			subject = 'Need support'
			body = 'Hello im ... i need a support to help me with ... . I have '
			body = body.replace(' ', '%20')
			webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)

		def open_link(self):
			webbrowser.open("https://bugtracker-api.azurewebsites.net/swagger/index.html")

		def report_app(self):
			if self.itemSelectionDetected == True:
				app_id = self.app_list[self.ui.app_list.currentRow()].id
				reportscreen = ReportScreen(user.id,app_id)
				widget.addWidget(reportscreen)
				report_index = 6
				widget.setCurrentIndex(report_index)
			#print(clicked,type(clicked)) Debug 
			#print(self.app_list[clicked].name)

		def clear_app_list(self):
			self.app_list = []
			self.ui.app_list.clear()

		def search_for_app(self):
			
			keyword = self.ui.search_box.text()
			if keyword == '':
				self.reload_app_list()
			else:
				self.clear_app_list()
				link = 'https://bugtracker-api.azurewebsites.net/api/App/SearchByName/'
				r = requests.get(link+keyword)
				for i in r.json():
					self.app_list.append(App(i))
				for a in self.app_list:
					self.ui.app_list.addItem(a.name)
			
		def reload_app_list(self):
			self.clear_app_list()
			self.load_app_list()
			self.itemSelectionDetected = False
			
		def load_app_list(self):
			self.app_list = []
			r = requests.get('https://bugtracker-api.azurewebsites.net/api/App/GetAll')
			for i in r.json():
				self.app_list.append(App(i))
			for a in self.app_list:
				self.ui.app_list.addItem(a.name)
			'''
			i = 0
			while i < 100:
				self.ui.app_list.addItem(str(i))
				i = i + 1
			'''
			#print(user.id)
		def trigger_side_menu(self):
			
			if self.side_menu_state == False:
				self.ui.slide_menu_container.setMaximumWidth(250)
			else:
				self.ui.slide_menu_container.setMaximumWidth(0)
			self.side_menu_state = not self.side_menu_state
			

	#staff
	class MainMenuStaffScreen(QDialog):
		def __init__(self):
			super(MainMenuStaffScreen, self).__init__()
			self.side_menu_state = False
			self.itemSelectionDetected = False
			self.ui = main_menu_staff_ui.Ui_Dialog()
			self.ui.setupUi(self)

			self.ui.slide_menu_container.setMaximumWidth(0)
			self.ui.exit_button.clicked.connect(sys.exit)
			self.ui.menu_button.clicked.connect(self.trigger_side_menu)
			self.ui.refresh_button.clicked.connect(self.reload_app_list)
			self.ui.search_button.clicked.connect(self.search_for_app)
			#self.ui.report_button.clicked.connect(self.report_app)
			self.ui.app_list.itemDoubleClicked.connect(self.load_report_bug)

			self.ui.app_list.itemClicked.connect(self.show_app_page)

			self.ui.report_list.itemClicked.connect(self.show_report_page)
			self.ui.report_list.itemDoubleClicked.connect(self.load_report_info)

			self.ui.bug_list.itemClicked.connect(self.show_bug_page)
			self.ui.bug_list.itemDoubleClicked.connect(self.load_bug_info)

			self.ui.website_button.clicked.connect(self.open_link)
			self.ui.email_button.clicked.connect(self.open_email)

			self.ui.app_list.itemSelectionChanged.connect(self.on_change_app)

			self.ui.signout_button.clicked.connect(self.signout)
			self.app_list = []
			self.report_list = []
			self.bug_list = []
			self.add_id = None
			#self.load_app_list()
		def show_app_page(self):
			self.ui.pager.setCurrentIndex(0)

		def show_report_page(self):
			self.ui.pager.setCurrentIndex(1)

		def show_bug_page(self):
			self.ui.pager.setCurrentIndex(2)

		def load_report_info(self):
			leReport = self.report_list[self.ui.report_list.currentRow()]
			self.ui.report_title_box.setPlainText(leReport.title)
			self.ui.report_description_box.setPlainText(leReport.description)

		def load_bug_info(self):
			leBug = self.bug_list[self.ui.bug_list.currentRow()]
			self.ui.bug_title_box.setPlainText(leBug.title)
			self.ui.bug_description_box.setPlainText(leBug.description)
			self.ui.bug_status_box.setPlainText(leBug.status_list[leBug.status])
			self.ui.bug_serverity_box.setPlainText(leBug.serverities_list[leBug.serverity])
			startStylesheet = """QPlainTextEdit {
							border:3px solid rgb(17, 60, 71);
							border-radius:20px;
							font: 500 italic 20pt "Ubuntu";
							color: """

			endStylesheet = """;
							;}"""
			if leBug.status == 0:
				#print("Debug here")
				#self.ui.bug_status_box.setStyleSheet()
				pass
		def load_report_bug(self):
			self.app_id = self.app_list[self.ui.app_list.currentRow()].id
			print(self.app_id)
			self.ui.side_box.setCurrentIndex(1)
			self.report_list = []
			self.ui.report_list.clear()

			r = requests.get('https://bugtracker-api.azurewebsites.net/api/Report/GetByAppId/'+str(self.app_id))
			for i in r.json():
				self.report_list.append(Report(i))
			for a in self.report_list:
				self.ui.report_list.addItem(a.title)

			self.bug_list = []
			self.ui.bug_list.clear()

			r = requests.get('https://bugtracker-api.azurewebsites.net/api/Bug/GetByStaffId/'+user.id)
			for i in r.json():
				self.bug_list.append(Bug(i))
			for a in self.bug_list:
				self.ui.bug_list.addItem(a.title)

		def signout(self):
			user.signout()
			self.clear_all_list()
			widget.setCurrentIndex(welcomescreen_index)
		def on_change_app(self):
			self.show_app_page(	)
			self.itemSelectionDetected = True
			#print("nice")
			
		def open_email(self):
			recipient = 'ITITIU19185@student.hcmiu.edu.vn'
			subject = 'Need support'
			body = 'Hello im ... i need a support to help me with ... . I have '
			body = body.replace(' ', '%20')
			webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)

		def open_link(self):
			webbrowser.open("https://bugtracker-api.azurewebsites.net/swagger/index.html")

		def clear_app_list(self):
			self.app_list = []
			self.ui.app_list.clear()
		def clear_all_list(self):
			self.app_list = []
			self.ui.app_list.clear()
			self.report_list = []
			self.ui.report_list.clear()
			self.bug_list = []
			self.ui.bug_list.clear()
		def search_for_app(self):
			
			keyword = self.ui.search_box.text()
			if keyword == '':
				self.reload_app_list()
			else:
				self.clear_app_list()
				link = 'https://bugtracker-api.azurewebsites.net/api/App/SearchByName/'
				r = requests.get(link+keyword)
				for i in r.json():
					self.app_list.append(App(i))
				for a in self.app_list:
					self.ui.app_list.addItem(a.name)
			
		def reload_app_list(self):
			self.clear_app_list()
			self.load_app_list()
			self.repot_list = []
			self.ui.report_list.clear()
			self.bug_list = []
			self.ui.bug_list.clear()
			self.itemSelectionDetected = False
			
		def load_app_list(self):
			self.app_list = []
			r = requests.get('https://bugtracker-api.azurewebsites.net/api/App/GetByStaffId/'+user.id)
			for i in r.json():
				self.app_list.append(App(i))
				print(i)
			for a in self.app_list:
				self.ui.app_list.addItem(a.name)
			'''
			i = 0
			while i < 100:
				self.ui.app_list.addItem(str(i))
				i = i + 1
			'''
			#print(user.id)
		def trigger_side_menu(self):
			
			if self.side_menu_state == False:
				self.ui.slide_menu_container.setMaximumWidth(250)
			else:
				self.ui.slide_menu_container.setMaximumWidth(0)
			self.side_menu_state = not self.side_menu_state
	#customer
	class MainMenuCustomerScreen(QDialog):
		def __init__(self):
			super(MainMenuCustomerScreen, self).__init__()
			self.side_menu_state = False
			self.itemSelectionDetected = False
			self.ui = main_menu_customer_ui.Ui_Dialog()
			self.ui.setupUi(self)

			self.ui.slide_menu_container.setMaximumWidth(0)
			self.ui.exit_button.clicked.connect(sys.exit)
			self.ui.menu_button.clicked.connect(self.trigger_side_menu)
			self.ui.refresh_button.clicked.connect(self.reload_app_list)
			self.ui.search_button.clicked.connect(self.search_for_app)
			self.ui.report_button.clicked.connect(self.report_app)
			self.ui.website_button.clicked.connect(self.open_link)
			self.ui.email_button.clicked.connect(self.open_email)
			self.ui.app_list.itemSelectionChanged.connect(self.on_change_app_app)
			self.ui.signout_button.clicked.connect(self.signout)
			self.app_list = []
			self.load_app_list()
		def signout(self):
			user.signout()
			widget.setCurrentIndex(welcomescreen_index)
		def on_change_app_app(self):
			self.itemSelectionDetected = True
				
		def open_email(self):
			recipient = 'ITITIU19185@student.hcmiu.edu.vn'
			subject = 'Need support'
			body = 'Hello im ... i need a support to help me with ... . I have '
			body = body.replace(' ', '%20')
			webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)

		def open_link(self):
			webbrowser.open("https://bugtracker-api.azurewebsites.net/swagger/index.html")

		def report_app(self):
			if self.itemSelectionDetected == True:
				app_id = self.app_list[self.ui.app_list.currentRow()].id
				reportscreen = ReportScreen(user.id,app_id)
				widget.addWidget(reportscreen)
				report_index = 6
				widget.setCurrentIndex(report_index)
			#print(clicked,type(clicked)) Debug 
			#print(self.app_list[clicked].name)

		def clear_app_list(self):
			self.app_list = []
			self.ui.app_list.clear()

		def search_for_app(self):
			
			keyword = self.ui.search_box.text()
			if keyword == '':
				self.reload_app_list()
			else:
				self.clear_app_list()
				link = 'https://bugtracker-api.azurewebsites.net/api/App/SearchByName/'
				r = requests.get(link+keyword)
				for i in r.json():
					self.app_list.append(App(i))
				for a in self.app_list:
					self.ui.app_list.addItem(a.name)
			
		def reload_app_list(self):
			self.clear_app_list()
			self.load_app_list()
			self.itemSelectionDetected = False
			
		def load_app_list(self):
			self.app_list = []
			r = requests.get('https://bugtracker-api.azurewebsites.net/api/App/GetAll')
			for i in r.json():
				self.app_list.append(App(i))
			for a in self.app_list:
				self.ui.app_list.addItem(a.name)
			'''
			i = 0
			while i < 100:
				self.ui.app_list.addItem(str(i))
				i = i + 1
			'''
			#print(user.id)
		def trigger_side_menu(self):
			
			if self.side_menu_state == False:
				self.ui.slide_menu_container.setMaximumWidth(250)
			else:
				self.ui.slide_menu_container.setMaximumWidth(0)
			self.side_menu_state = not self.side_menu_state
			
	class ReportScreen(QDialog):
		def __init__(self,user_id,app_id):
			super(ReportScreen, self).__init__()
			self.ui = report_ui.Ui_Dialog()
			self.ui.setupUi(self)
			self.ui.cancel_button.clicked.connect(self.cancel)
			self.ui.report_button.clicked.connect(self.report)
			self.user_id = user_id
			self.app_id = app_id
			print(self.user_id,self.app_id)
		#def clear_data(self):
		def cancel(self):
			widget.setCurrentIndex(menu_customer_index)
		def report(self):
			#title = self.ui.title_box.text()
			title = self.ui.select_box.currentText()
			desc = self.ui.description_box.toPlainText()
			
			r = requests.post('https://bugtracker-api.azurewebsites.net/api/Report/Create', json={
			"id": 0,
			"title": title,
			"description": desc,
			"customerId": self.user_id,
			"appId": self.app_id
			})
			#popup report
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)

			msg.setText("Thank you for reporting the bug !")
			#msg.setInformativeText("This is additional information")
			msg.setWindowTitle("Thank you !")
			msg.setWindowIcon(QtGui.QIcon('logo.png'))
			#msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
			msg.setStandardButtons(QMessageBox.Ok)
			retval = msg.exec_()
			print("value of pressed message box button:", retval)
			self.ui.description_box.clear()
			self.cancel()

	# run this if main
	if __name__ == "__main__":
		suppress_qt_warnings()

		app = QApplication(sys.argv)
		widget = QtWidgets.QStackedWidget()

		welcomescreen = WelcomeScreen()
		widget.addWidget(welcomescreen)
		welcomescreen_index = 0

		signinscreen = SignInScreen()
		widget.addWidget(signinscreen)
		signin_index = 1

		signupscreen = SignUpScreen()
		widget.addWidget(signupscreen)
		signup_index = 2

		mainmenuadminscreen = MainMenuAdminScreen()
		widget.addWidget(mainmenuadminscreen)
		menu_admin_index = 3
		#widget.setCurrentIndex(menu_admin_index)

		mainmenucustomerscreen = MainMenuCustomerScreen()
		widget.addWidget(mainmenucustomerscreen)
		menu_customer_index = 4
		#widget.setCurrentIndex(menu_customer_index)

		mainmenustaffscreen = MainMenuStaffScreen()
		widget.addWidget(mainmenustaffscreen)
		menu_staff_index = 5

		widget.setWindowIcon(QtGui.QIcon('logo.png'))
		widget.setWindowTitle("BugTracker v1")
		widget.setFixedHeight(800)
		widget.setFixedWidth(1200)
		widget.show()
		#loginscreen.show()
		try:
			sys.exit(app.exec())
		except Exception as bug:
			print(bug)
except Exception as bug:
	print(bug)
	input("Enter to close this cmd window!!!")