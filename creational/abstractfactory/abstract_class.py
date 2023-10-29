from abc import ABC, abstractmethod


class Button(ABC):
    @staticmethod
    @abstractmethod
    def render(): ...

    @staticmethod
    @abstractmethod
    def on_click(): ...


class CheckBox(ABC):
    @staticmethod
    @abstractmethod
    def render(): ...

    @staticmethod
    @abstractmethod
    def on_check(): ...


class TextField(ABC):
    @staticmethod
    @abstractmethod
    def render(): ...

    @staticmethod
    @abstractmethod
    def on_input(): ...


class GUIFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_button(): ...

    @staticmethod
    @abstractmethod
    def create_text_filed(): ...

    @staticmethod
    @abstractmethod
    def crete_check_box(): ...
