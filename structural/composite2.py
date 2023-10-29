from abc import ABC, abstractmethod


class IComponent(ABC):
    """Interface"""

    @abstractmethod
    def get_size(self):
        """returns size of the component in mb"""


class File(IComponent):

    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_size(self):
        return self._size


class Folder(IComponent):

    def __init__(self, name, components):
        self._name = name
        self._components = components

    def get_size(self):
        total_size = 0
        for c in self._components:
            total_size += c.get_size()
        return total_size


budget_file = File('budget_report.csv', 2.5)
photo = File('image.jpg', 7.5)
metallica = File('enter sandaman.mp3', 5)

stuff = Folder('My Stuff', [budget_file, photo, metallica])


print('Budget size: ', budget_file.get_size())
print(photo.get_size())
print(metallica.get_size())
print(stuff.get_size())















