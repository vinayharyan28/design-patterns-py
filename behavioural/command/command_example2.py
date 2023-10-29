from abc import abstractmethod


class ISwitch:
    @staticmethod
    @abstractmethod
    def execute(): ...


class LightReceiver:
    @staticmethod
    def run_switch_on_command():
        print('light is on')

    @staticmethod
    def run_switch_of_command():
        print('light is of')


class SwitchOnCommand(ISwitch):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.run_switch_on_command()


class SwitchOfCommand(ISwitch):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.run_switch_of_command()


class LightInvoker:
    def __init__(self):
        self.command = dict()
        self.command_history = list()

    def register(self, command_id, command):
        self.command[command_id] = command

    def undo(self, command_id, command):
        self.command[command_id] = command
        return command[command_id-1].execute()

    def execute(self, command_id):
        if command_id in self.command.keys():
            self.command[command_id].execute()
        else:
            print('command id not present in command.')


light_receiver = LightReceiver()
switch_on_command = SwitchOnCommand(light_receiver)
switch_of_command = SwitchOfCommand(light_receiver)
invoker = LightInvoker()
invoker.register(1, switch_on_command)
invoker.register(2, switch_of_command)
invoker.execute(1)
invoker.execute(2)
invoker.execute(2)
invoker.execute(1)
















