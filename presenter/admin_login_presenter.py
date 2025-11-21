from view.login_view import LoginView
from view.register_view import RegisterView
from presenter.login_presenter import LoginPresenter
from presenter.register_presenter import RegisterPresenter

class AdminLoginPresenter:
    def __init__(self, view, page, main_presenter):
        self.view = view
        self.page = page
        self.main_presenter = main_presenter

    def open_login(self):
        login_view = LoginView()
        login_presenter = LoginPresenter(login_view, self.page, self.main_presenter)
        login_view.presenter = login_presenter

        self.page.controls.clear()
        self.page.add(login_view.build(self.page))
        self.page.update()

    def open_register(self):
        register_view = RegisterView()
        register_presenter = RegisterPresenter(register_view, self.page, self.main_presenter)
        register_view.presenter = register_presenter

        self.page.controls.clear()
        self.page.add(register_view.build(self.page))
        self.page.update()

    def go_back_main(self):
        self.main_presenter.go_back_to_main()
