import flet
from flet import Page, Text, TextField, ElevatedButton, Column, Container, MainAxisAlignment, CrossAxisAlignment, ButtonStyle, OutlinedButton, TextStyle

class LoginView:
    def __init__(self):
        self.presenter = None
        self.message_text = Text("", size=16)

    def build(self, page: Page):
        self.username = TextField(label="Username", width=200)
        self.password = TextField(label="Password", width=200, password=True, can_reveal_password=True)

        login_btn = ElevatedButton(
            "Login",
            width=150,
            height=50,
            style=ButtonStyle(text_style=TextStyle(size=18)),
            on_click=lambda e: self.presenter.login(self.username.value, self.password.value)
        )

        back_btn = OutlinedButton(
            "Back",
            width=150,
            height=50,
            style=ButtonStyle(text_style=TextStyle(size=18)),
            on_click=lambda e: self.presenter.go_back()
        )

        ui = Column([ 
            Text("Admin Login", size=35),
            Container(height=5),
            self.message_text,
            Container(height=10),
            self.username,
            Container(height=5),
            self.password,
            Container(height=10),
            login_btn,
            Container(height=5),
            back_btn
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
        )

        return ui

    def show_message(self, msg: str):
        self.message_text.value = msg
        self.message_text.update()
