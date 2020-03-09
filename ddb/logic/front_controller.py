from logic.query_logic import QueryLogic
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
            except Exception:           # łapać nowy, specjalnie zdefiniowany wyjątek ;)
                self.ui.print_error()
                continue

            ql: QueryLogic

            # zadania domowe:
            # 1. zastanowić się, czy na pewno FRONT controller to dobre miejsce na podejmowanie takich decyzji?
            # 2. Jak można to zaimplementować bez brzydkiej ifologii?
            if command_name == 'create':
                ql = CreateLogic()
            # elif command_name == 'select':
            #     ql = SelectLogic()    # odkomentować po zaimplementowaniu klasy 'SelectLogic'
            # else:
            #     ql = AddLogic()    # odkomentować po zaimplementowaniu klasy 'AddLogic'

            ql.control(document_name, cols, vals)
            # dzięki temu, że wszystkie klasy dziedziczą po QueryLogic nie musimy wywoływać metody w każdym ifie!
            # To się nazywa polimorfizm! ;)
