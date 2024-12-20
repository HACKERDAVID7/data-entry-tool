from view_data import ViewDataPage
from login import LoginPage
from registration import RegistrationPage
from data_entry import DataEntryPage
from splash_screen import SplashScreen

class NavigationManager:
    def __init__(self, root):
        self.root = root

    def show_login(self):
        LoginPage(self.root, self)

    def show_register(self):
        RegistrationPage(self.root, self)

    def show_data_entry(self):
        DataEntryPage(self.root, self)

    def show_view_data(self):
        ViewDataPage(self.root, self)
    
    def show_splash_screen(self):
        SplashScreen(self.root, self)
