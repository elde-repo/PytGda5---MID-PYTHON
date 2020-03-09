import re


class CommandsInterpreter:
    def __init__(self):
        self.VALID_REGEX = {
            'create': {
                'regex': '\s*CREATE\s+DOCUMENT\s+(\w*)\s+\((.*)\)'
            },
            'add': {
               'regex': '\s*ADD\s+\((.*)\)\s+TO\s+(\w*)'
            },
            'select': {
               'regex': '\s*SELECT\s+\((.*)\)\s+FROM\s+(\w*)'
            }
        }

    def interpret(self, command):
        document_name = None
        columns = None
        values = None

        for command_name, vr in self.VALID_REGEX.items():
            selected_command = re.findall(vr['regex'], command, re.I)
            if len(selected_command):
                selected_command = selected_command[0]
                if command_name == 'create':
                    document_name = selected_command[0]
                    columns = selected_command[1]
                elif command_name == 'add':
                    values = selected_command[0]
                    document_name = selected_command[1]
                elif command_name == 'select':
                    columns = selected_command[0]
                    document_name = selected_command[1]

                if columns is not None:
                    columns = columns.replace(' ', '').split(',')
                if values is not None:
                    values = values.replace(' ', '').split(',')

                return command_name, document_name, columns, values
        raise Exception("Failed")
