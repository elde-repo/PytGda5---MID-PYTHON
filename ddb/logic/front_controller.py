from user_interface.user_interface import UserInterface
from logic.commands_interpreter import CommandsInterpreter
from logic.create_logic import CreateLogic


class FrontController:
    def __init__(self):
        self.ui = UserInterface()
        self.ci = CommandsInterpreter()

        self.ui.say_hello()

    def run(self):
        while True:
            command = self.ui.user_input()
            try:
                command_name, document_name, cols, vals = self.ci.interpret(command)
            except:
                self.ui.print_error()
                continue

            if command_name == 'create':
                cl = CreateLogic()
                cl.controll(document_name, cols, vals)
