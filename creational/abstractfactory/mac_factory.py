from creational.abstractfactory.abstract_class import GUIFactory, Button, CheckBox, TextField


class MacFactory(GUIFactory):
    @staticmethod
    def create_button():
        return MacOSButton()

    @staticmethod
    def create_text_filed():
        return MacOSTextFiled()

    @staticmethod
    def crete_check_box():
        return MacOSCheckBox()


class MacOSButton(Button):
    @staticmethod
    def render():
        print('Rendering mac OS button...')

    @staticmethod
    def on_click():
        print('Click on mac os button...')


class MacOSCheckBox(CheckBox):
    @staticmethod
    def render():
        print('Rendering mac OS checkbox button...')

    @staticmethod
    def on_check():
        print('Check on mac OS checkbox button...')


class MacOSTextFiled(TextField):
    @staticmethod
    def render():
        print('Rendering mac OS text filed button...')

    @staticmethod
    def on_input():
        print('Input on mac OS text filed button...')