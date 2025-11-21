from view.main_view import MainView
from view.admin_choice_view import AdminChoiceView
from view.user_view import UserNotebookView
from presenter.admin_login_presenter import AdminLoginPresenter

class MainPresenter:
    def __init__(self, view: MainView, page):
        self.view = view
        self.page = page

    def open_admin_mode(self):
        admin_choice_view = AdminChoiceView()
        presenter = AdminLoginPresenter(admin_choice_view, self.page, self)
        admin_choice_view.presenter = presenter

        self.page.controls.clear()
        self.page.add(admin_choice_view.build(self.page))
        self.page.update()

    def open_user_mode(self):
        user_view = UserNotebookView(self)
        self.page.controls.clear()
        self.page.add(user_view.build(self.page))
        self.page.update()

    def go_back_to_main(self):
        self.page.controls.clear()
        self.page.add(self.view.build(self.page))
        self.page.update()
