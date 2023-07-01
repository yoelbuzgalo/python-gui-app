from PySide6.QtWidgets import QLabel, QLineEdit,QVBoxLayout, QHBoxLayout, QWidget, QPushButton

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        # Layout for Username Box
        self.username_layout = QHBoxLayout()
        self.username_layout.setObjectName("username_layout")
        self.username_label = QLabel("Username: ")
        self.username_input = QLineEdit()
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)
        # Layout for Password Box
        self.password_layout = QHBoxLayout()
        self.password_layout.setObjectName("password_layout")
        self.password_label = QLabel("Password: ")
        self.password_input = QLineEdit()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)
        # Login Button
        self.login_button = QPushButton("Login")

        # No Account? Redirect to Sign Up
        self.sign_up_redirect_layout = QVBoxLayout()
        self.sign_up_redirect_label = QLabel("Don't have an account? Sign up today!")
        self.sign_up_redirect_button = QPushButton("Sign Up")
        self.sign_up_redirect_layout.addWidget(self.sign_up_redirect_label)
        self.sign_up_redirect_layout.addWidget(self.sign_up_redirect_button)

        # Main layout of the login page
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName("Main_Layout")
        self.main_layout.addLayout(self.username_layout)
        self.main_layout.addLayout(self.password_layout)
        self.main_layout.addWidget(self.login_button)
        self.main_layout.addLayout(self.sign_up_redirect_layout)
        self.setLayout(self.main_layout)