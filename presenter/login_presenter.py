from dao.admin_dao_impl import AdminDAOImpl

class LoginPresenter:
    def __init__(self, view, page, main_presenter):
        self.view = view
        self.page = page
        self.main_presenter = main_presenter
        self.admin_dao = AdminDAOImpl()

    def login(self, username, password):
        if self.admin_dao.verify_admin(username, password):
            from view.admin_view import AdminView
            from presenter.admin_presenter import AdminPresenter

            admin_view = AdminView(None)
            admin_presenter = AdminPresenter(admin_view, self.main_presenter)
            admin_view.presenter = admin_presenter

            self.page.controls.clear()
            self.page.add(admin_view.build(self.page))
            self.page.update()
        else:
            self.view.show_message("Wrong username or password!")

    def go_back(self):
        self.main_presenter.go_back_to_main()
