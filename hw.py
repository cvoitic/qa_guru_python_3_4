
def open_browser(browser_name):
    print(f"{open_browser.__name__} {browser_name}".replace("_", " ").capitalize())


def go_to_companyname_homepage(page_url):
    print(f"{go_to_companyname_homepage.__name__} {page_url}".replace("_", " ").capitalize())


def find_registration_button_on_login_page(page_url, button_text):
    print(f"{find_registration_button_on_login_page.__name__} {page_url} {button_text}".replace("_", " ").capitalize())


open_browser(browser_name="Chrome")
go_to_companyname_homepage("pythontutor.com")
find_registration_button_on_login_page("booking.com", "'Зарегистрироваться'")
