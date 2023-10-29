from creational.abstractfactory.mac_factory import MacFactory
from creational.abstractfactory.window_factory import WindowsFactory


def is_windows():
    # Check the current operating system
    # For simplicity, assume its windows here
    return True


if __name__ == '__main__':
    factory = WindowsFactory() if is_windows() else MacFactory()
    button = factory.create_button()
    text_filed = factory.create_text_filed()
    check_box = factory.crete_check_box()

    button.render()
    text_filed.render()
    check_box.render()

    button.on_click()
    text_filed.on_input()
    check_box.on_check()