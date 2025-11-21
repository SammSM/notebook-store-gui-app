import flet
from flet import Page, Text, TextField, ElevatedButton, Column, DataTable, DataRow, DataCell, Row, IconButton, DataColumn, Dropdown, dropdown

class AdminView:
    def __init__(self, presenter=None):
        self.presenter = presenter
        self.notebook_id = None
        self.brand_dropdown = None
        self.model_dropdown = None
        self.ram_dropdown = None
        self.ssd_dropdown = None
        
        self.price_input = TextField(label="Price (USD)", width = 200)
        self.quantity_input = TextField(label="Available", width = 200)

        self.message_text = Text("", size=16)

        self.table = DataTable(
            columns=[
                DataColumn(Text("Model")),
                DataColumn(Text("RAM")),
                DataColumn(Text("SSD")),
                DataColumn(Text("Price (USD)")),
                DataColumn(Text("Available")),
                DataColumn(Text("")),
                DataColumn(Text("")),
            ],
            rows=[]
        )

    def build(self, page: Page):
        self.page = page

        self.brand_dropdown = Dropdown(label="Brand", options=[], width=200, on_change=self.on_brand_change)
        self.model_dropdown = Dropdown(label="Model", options=[], width=200)
        self.ram_dropdown = Dropdown(label="RAM", options=[], width=150)
        self.ssd_dropdown = Dropdown(label="SSD", options=[], width=150)

        add_btn = ElevatedButton("Add", on_click=self.add_notebook)
        update_btn = ElevatedButton("Update", on_click=self.update_notebook)
        back_btn = ElevatedButton("Logout", on_click=lambda e: self.presenter.go_back())

        ui = Column([
            back_btn,
            Text("Admin Panel", size=35),
            Row([self.brand_dropdown, self.model_dropdown, self.ram_dropdown, self.ssd_dropdown]),
            self.price_input,
            self.quantity_input,
            Row([add_btn, update_btn]),
            self.message_text,
            self.table
        ])

        if self.presenter:
            self.presenter.load_brand_dropdown()
            self.presenter.load_ram_ssd_dropdowns()
            self.presenter.load_notebooks()

        return ui


    def set_ram_ssd_dropdowns(self, ram, ssd):
        self.ram_dropdown.options = [dropdown.Option(text="RAM", key='default', disabled=True)] + [dropdown.Option(str(r["id"]), r["name"]) for r in ram]
        self.ssd_dropdown.options = [dropdown.Option(text="SSD", key='default', disabled=True)] + [dropdown.Option(str(s["id"]), s["name"]) for s in ssd]
        self.page.update()

    def on_brand_change(self, e):
        self.presenter.load_model_dropdown()

    def set_brand_dropdown(self, brands):
        self.brand_dropdown.options = [dropdown.Option(text="Brand", key='default', disabled=True)] + [dropdown.Option(str(b["id"]), b["name"]) for b in brands]
        self.page.update()

    def set_model_dropdown(self, models):
        self.model_dropdown.options = [dropdown.Option(text="Model", key='default', disabled=True)] + [dropdown.Option(str(m["id"]), m["name"]) for m in models]
        self.page.update()

    def set_table_data(self, notebooks):
        self.table.rows.clear()
        for nb in notebooks:
            edit_btn = IconButton(icon="edit", on_click=lambda e, n=nb: self.load_notebook(n))
            delete_btn = IconButton(icon="delete", on_click=lambda e, n=nb: self.presenter.delete_notebook(n["id"]))
            self.table.rows.append(DataRow(cells=[
                DataCell(Text(nb["model"])),
                DataCell(Text(nb["ram"])),
                DataCell(Text(nb["ssd"])),
                DataCell(Text(str(nb["price"]))),
                DataCell(Text(str(nb["quantity"]))),
                DataCell(edit_btn),
                DataCell(delete_btn),
            ]))
        self.page.update()

    def load_notebook(self, nb):
        self.notebook_id = nb["id"]
        self.price_input.value = str(nb["price"])
        self.quantity_input.value = str(nb["quantity"])

        self.brand_dropdown.value = str(nb.get("brand_id", "")) if nb.get("brand_id", None) is not None else None
        self.presenter.load_model_dropdown()
        self.model_dropdown.value = str(nb.get("model_id", "")) if nb.get("model_id", None) is not None else None
        self.ram_dropdown.value = str(nb.get("ram_id", "")) if nb.get("ram_id", None) is not None else None
        self.ssd_dropdown.value = str(nb.get("ssd_id", "")) if nb.get("ssd_id", None) is not None else None

        self.page.update()

    def update_notebook(self, e):
        if self.notebook_id==None:
            return

        modelid = self.model_dropdown.value
        ramid = self.ram_dropdown.value
        ssdid = self.ssd_dropdown.value
        price = self.price_input.value
        quantity = self.quantity_input.value

        if not all([modelid, ramid, ssdid, price, quantity]):
            self.show_message("All fields are required!")
            return

        self.presenter.update_notebook(self.notebook_id, modelid, ramid, ssdid, price, quantity)
        self.notebook_id = None

        self.price_input.value = ""
        self.quantity_input.value = ""
        self.brand_dropdown.value = 'default'
        self.model_dropdown.value = 'default'
        self.ram_dropdown.value = 'default'
        self.ssd_dropdown.value = 'default'

        self.brand_dropdown.update()
        self.model_dropdown.update()
        self.ram_dropdown.update()
        self.ssd_dropdown.update()

        self.presenter.load_notebooks()

    def add_notebook(self, e):
        if self.notebook_id != None:
            return
        
        modelid = self.model_dropdown.value
        ramid = self.ram_dropdown.value
        ssdid = self.ssd_dropdown.value
        price = self.price_input.value
        quantity = self.quantity_input.value

        if not all([modelid, ramid, ssdid, price, quantity]):
            self.show_message("All fields are required!")
            return

        self.presenter.add_notebook(modelid, ramid, ssdid, price, quantity)

        self.price_input.value = ""
        self.quantity_input.value = ""
        self.brand_dropdown.value = 'default'
        self.model_dropdown.value = 'default'
        self.ram_dropdown.value = 'default'
        self.ssd_dropdown.value = 'default'

        self.brand_dropdown.update()
        self.model_dropdown.update()
        self.ram_dropdown.update()
        self.ssd_dropdown.update()

        self.presenter.load_notebooks()

    def show_message(self, msg):
        self.message_text.value = msg
        self.message_text.update()
