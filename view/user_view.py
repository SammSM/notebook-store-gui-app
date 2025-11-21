import flet
from flet import Page, Text, ElevatedButton, Column, DataTable, DataColumn, DataRow, DataCell
from presenter.user_presenter import UserNotebookPresenter

class UserNotebookView:
    def __init__(self, main_presenter):
        self.main_presenter = main_presenter
        self.presenter = UserNotebookPresenter(self, main_presenter)
        self.table = DataTable(
            columns=[
                DataColumn(Text("Brand")),
                DataColumn(Text("Model")),
                DataColumn(Text("Country")),
                DataColumn(Text("OS")),
                DataColumn(Text("Type")),
                DataColumn(Text("RAM")),
                DataColumn(Text("SSD")),
                DataColumn(Text("Price (USD)")),
                DataColumn(Text("Available")),
            ],
            rows=[]
        )
        self.message_text = Text("", size=16)

    def build(self, page: Page):
        self.page = page
        exit_btn = ElevatedButton("Exit", on_click=lambda e: self.presenter.go_back())

        ui = Column([
            exit_btn,
            Text("Available Notebooks", size=20, weight="bold"),
            self.table,
            self.message_text
        ])

        self.presenter.load_notebooks()

        return ui

    def display_notebooks(self, notebooks):
        self.table.rows.clear()
        for nb in notebooks:
            self.table.rows.append(
                DataRow(cells=[
                    DataCell(Text(nb["brand"])),
                    DataCell(Text(nb["model"])),
                    DataCell(Text(nb["country"])),
                    DataCell(Text(nb["os"])),
                    DataCell(Text(nb["type"])),
                    DataCell(Text(nb["ram"])),
                    DataCell(Text(nb["ssd"])),
                    DataCell(Text(str(nb["price"]))),
                    DataCell(Text(str(nb["quantity"]))),
                ])
            )
        self.page.update()

    def show_message(self, msg: str):
        self.message_text.value = msg
        self.message_text.update()
