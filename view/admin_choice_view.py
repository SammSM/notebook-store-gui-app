import flet
from flet import Text, ElevatedButton, Column, Container, MainAxisAlignment, CrossAxisAlignment, OutlinedButton, ButtonStyle, TextStyle

class AdminChoiceView:
    def __init__(self):
        self.presenter = None

    def build(self, page):
        back_btn = OutlinedButton(
            "Back",
            on_click=lambda e: self.presenter.go_back_main(),
            width = 150,
            height = 50,
            style=ButtonStyle(text_style=TextStyle(size=18))
        )

        open_login_btn = ElevatedButton(
            "Login",
            on_click=lambda e: self.presenter.open_login(),
            width = 150,
            height = 50,
            style=ButtonStyle(text_style=TextStyle(size=18))
        )

        open_register_btn = ElevatedButton(
            "Register",
            on_click=lambda e: self.presenter.open_register(),
            width = 150,
            height = 50,
            style=ButtonStyle(text_style=TextStyle(size=18))
        )

        ui = Column([ 
            Text("Admin", size=35),
            Container(height=10),
            open_login_btn,
            Container(height=5),
            open_register_btn,
            Container(height=5),
            back_btn
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand = True
        )

        return ui
