import flet
from flet import Page, Text, ElevatedButton, Column, Container, MainAxisAlignment, CrossAxisAlignment, ButtonStyle, TextStyle

class MainView:
    def __init__(self):
        self.presenter = None

    def build(self, page: Page):
        admin_btn = ElevatedButton(
            "Login as Admin",
            on_click=lambda e: self.presenter.open_admin_mode(),
            width = 200,
            height = 50,
            style=ButtonStyle(text_style=TextStyle(size=18))
        )

        user_btn = ElevatedButton(
            "Continue as User",
            on_click=lambda e: self.presenter.open_user_mode(),
            width = 200,
            height = 50,
            style=ButtonStyle(text_style=TextStyle(size=18))
        )

        ui = Column(
            [
                Text("Welcome to Notebook Store!", size=35),
                Container(height=10),
                admin_btn,
                Container(height=10),
                user_btn,
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand = True
        )

        return ui
