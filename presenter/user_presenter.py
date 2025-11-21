from dao.notebook_dao_impl import NotebookDAOImpl

class UserNotebookPresenter:
    def __init__(self, view, main_presenter):
        self.view = view
        self.main_presenter = main_presenter
        self.dao = NotebookDAOImpl()

    def load_notebooks(self):
        try:
            notebooks = self.dao.get_all()
            self.view.display_notebooks(notebooks)
        except Exception as e:
            self.view.show_message(f"Error loading notebooks: {e}")

    def go_back(self):
        self.main_presenter.go_back_to_main()
