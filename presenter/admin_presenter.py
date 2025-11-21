from model.notebook import Notebook
from dao.notebook_dao_impl import NotebookDAOImpl

class AdminPresenter:
    def __init__(self, view, main_presenter):
        self.view = view
        self.main_presenter = main_presenter
        self.dao = NotebookDAOImpl()

    def load_ram_ssd_dropdowns(self):
        ram = self.dao.get_all_ram()
        ssd = self.dao.get_all_ssd()
        self.view.set_ram_ssd_dropdowns(ram, ssd)

    def load_brand_dropdown(self):
        brands = self.dao.get_all_brands()
        self.view.set_brand_dropdown(brands)

    def load_model_dropdown(self):
        drop_val = self.view.brand_dropdown.value
        if drop_val is None or drop_val == "default":
            self.view.set_model_dropdown([]) 
            return

        models = self.dao.get_all_models(drop_val)
        self.view.set_model_dropdown(models)


    def load_notebooks(self):
        notebooks = self.dao.get_all()
        self.view.set_table_data(notebooks)

    def add_notebook(self, model_id, ram_id, ssd_id, price, quantity):
        if not all([model_id, ram_id, ssd_id, price, quantity]):
            self.view.show_message("All fields are required!")
            return
        notebook = Notebook(
            id=None,
            model_id=int(model_id),
            ram_id=int(ram_id),
            ssd_id=int(ssd_id),
            price=float(price),
            quantity=int(quantity)
        )
        self.dao.add(notebook)
        self.load_notebooks()

    def delete_notebook(self, notebook_id):
        self.dao.delete(notebook_id)
        self.load_notebooks()

    def update_notebook(self, notebook_id, model_id, ram_id, ssd_id, price, quantity):
        notebook = Notebook(
            id=notebook_id,
            model_id=int(model_id),
            ram_id=int(ram_id),
            ssd_id=int(ssd_id),
            price=float(price),
            quantity=int(quantity)
        )
        self.dao.update(notebook)
        self.load_notebooks()

    def go_back(self):
        self.main_presenter.go_back_to_main()
