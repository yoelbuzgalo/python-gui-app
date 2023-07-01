from PySide6.QtWidgets import QApplication, QMainWindow
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage
from back_end import Backend, Status
from models.user import User
import winsound
import time
class App(QApplication):
    def __init__(self, program_name, system_information):
        super().__init__(system_information)
        self.setApplicationName(program_name)
        self.current_user = None
        self.main_window = MainWindow(self.applicationName())
        self.start_program()
    def start_program(self):
        # self.play_intro_sound()
        if self.current_user is None:
            self.init_login_page()
    @staticmethod
    def play_intro_sound():
        bloops = (
            (440, 300),
            (523, 500),
            (659, 800)
        )
        # Plays start up sound
        for index, (frequency, duration) in enumerate(bloops):
            winsound.Beep(frequency, duration)
            if index == 1:
                time.sleep(1)

    def init_login_page(self):
        self.current_user = None
        self.login_page = LoginPage()
        self.login_page.login_button.clicked.connect(self.login)
        self.login_page.sign_up_redirect_button.clicked.connect(self.init_sign_up_page)
        self.main_window.setCentralWidget(self.login_page)
        self.main_window.show()

    def init_sign_up_page(self):
        self.current_user = None
        self.sign_up_page = SignUpPage()
        self.sign_up_page.sign_up_button.clicked.connect(self.sign_up)
        self.sign_up_page.login_redirect_button.clicked.connect(self.init_login_page)
        self.main_window.setCentralWidget(self.sign_up_page)
        self.main_window.show()

    def login(self):
        # Gets the current credentials input
        credentials = {
            "username": self.login_page.username_input.text(),
            "password": self.login_page.password_input.text()
        }
        # Send request to backend with the credentials
        login_status, user_instance = Backend.request_login(credentials)
        # Checks the returned status, if its either success or not - on success it will log you in with the returned user instance
        if login_status is not Status.SUCCESS:
            print("No matched user or your password is wrong, please try again!")
        if login_status is Status.SUCCESS:
            self.current_user = user_instance
            self.welcome_screen()

    def sign_up(self):
        # Gets the current credentials input
        credentials = {
            "username": self.sign_up_page.username_input.text(),
            "password": self.sign_up_page.password_input.text()
        }
        # Send request to backend with the credentials
        sign_up_status = Backend.request_sign_up(credentials)
        # Checks the returned status, if its either success or not - on success it will sign you up with the returned user instance
        if sign_up_status == Status.SUCCESS:
            login_status, user_instance = Backend.request_login(credentials)
            if login_status is not Status.SUCCESS:
                print("There was an error trying to log in after successful sign up")
            if login_status is Status.SUCCESS:
                self.current_user = user_instance
                self.welcome_screen()

    def welcome_screen(self):
        print(f"Hello, {self.current_user.get_username()}, welcome to {self.applicationName()}")

    def logout(self) -> Status:
        self.current_user = None
        print('Successfully logged out')
        return Status.SUCCESS
class MainWindow(QMainWindow):
    def __init__(self, window_name):
        super().__init__()
        self.setWindowTitle(window_name)
        self.setFixedSize(300,200)
def create_application(program_name, system_information):
    app = App(program_name, system_information)
    app.exec()