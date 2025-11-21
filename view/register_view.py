import flet
from flet import Page, Text, ElevatedButton, Column, Container, MainAxisAlignment, CrossAxisAlignment, ButtonStyle, TextStyle, TextField, OutlinedButton

class RegisterView:
    def __init__(self):
        self.presenter = None
        self.message_text = Text("", size=18)

    def build(self, page: Page):
        self.username = TextField(label="Username", width=200)
        self.password = TextField(label="Password", width=200, password=True, can_reveal_password=True)
        self.confirm_password = TextField(label="Confirm Password", width=200, password=True, can_reveal_password=True)

        register_btn = ElevatedButton(
            "Register",
            width=150,
            height=50,
            style=ButtonStyle(text_style=TextStyle(size=18)),
            on_click=lambda e: self.presenter.register(
                self.username.value,
                self.password.value,
                self.confirm_password.value
            )
        )

        back_btn = OutlinedButton(
            "Back",
            width=150,
            height=50,
            style=ButtonStyle(text_style=TextStyle(size=18)),
            on_click=lambda e: self.presenter.go_back()
        )

        controls = [
            Text("Admin Register", size=35),
            Container(height=10),
            self.username,
            Container(height=5),
            self.password,
            Container(height=5),
            self.confirm_password,
            Container(height=10),
            register_btn,
            Container(height=5),
            back_btn
        ]

        if self.message_text:
            controls.append(Container(height=10))
            controls.append(self.message_text)

        ui = Column(
            controls,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        return ui
