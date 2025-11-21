# import flet
# from flet import Page, ThemeMode, app
# from view.admin_view import AdminView
# from presenter.admin_presenter import AdminPresenter

# def main(page: Page):
#     page.title = "Computer Store"
#     page.theme_mode = ThemeMode.DARK

#     main_view = AdminView()
#     main_presenter = AdminPresenter(main_view, page)
#     main_view.presenter = main_presenter

#     page.add(main_view.build(page))

# app(target=main)

import flet
from flet import Page, ThemeMode, app
from view.main_view import MainView
from presenter.main_presenter import MainPresenter

def main(page: Page):
    page.title = "Notebook Store"
    page.theme_mode = ThemeMode.DARK

    main_view = MainView()
    main_presenter = MainPresenter(main_view, page)
    main_view.presenter = main_presenter

    page.add(main_view.build(page))

app(target=main)
