import bcrypt
from dao.admin_dao_impl import AdminDAOImpl

class RegisterPresenter:
    def __init__(self, view, page, main_presenter):
        self.view = view
        self.page = page
        self.main_presenter = main_presenter
        self.admin_dao = AdminDAOImpl()

    def register(self, username, password, confirm_password):
        if not username or not password:
            self._show_message("Username and password cannot be empty!")
            return

        if password != confirm_password:
            self._show_message("Passwords do not match!")
            return

        if self.admin_dao.get_admin(username):
            self._show_message("Username already exists!")
            return

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.admin_dao.add_admin(username, hashed.decode())

        self._show_message("You have successfully registered! Click Back to login.")

    def _show_message(self, message):
        self.view.message_text.value = message
        self.page.update()

    def go_back(self):
        self.main_presenter.go_back_to_main()
