from creational.abstractfactory.abstract_class import GUIFactory, Button, TextField, CheckBox


class WindowsFactory(GUIFactory):
    @staticmethod
    def create_button():
        return WindowButton()

    @staticmethod
    def create_text_filed():
        return WindowTextFiled()

    @staticmethod
    def crete_check_box():
        return WindowCheckBox()


class WindowButton(Button):
    @staticmethod
    def render():
        print('Rendering window button...')

    @staticmethod
    def on_click():
        print('Clicking on window button...')


class WindowCheckBox(CheckBox):
    @staticmethod
    def render():
        print('Rendering window check box...')

    @staticmethod
    def on_check():
        print('Check on window check box...')


class WindowTextFiled(TextField):
    @staticmethod
    def render():
        print('Rendering window text filed...')

    @staticmethod
    def on_input():
        print('Input on window text filed...')


