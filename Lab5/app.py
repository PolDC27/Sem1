from Ui.ui import ui
from Ui.ui import menu_repo
from Controller.Controller import Controller


def main():
        my_repository = menu_repo()()
        my_controller = Controller(my_repository)
        my_Ui = ui(my_controller)
        my_Ui.menu()

main()
