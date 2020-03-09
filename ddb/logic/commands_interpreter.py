import re


class CommandsInterpreter:
    def __init__(self):
        self.VALID_REGEX = {
            'create': {
                'regex': '\s*CREATE\s+DOCUMENT\s+(\w*)\s+\(([\w\s,]*)\)',
                # zamiast .* dla wyrażeń w nawiasie zastosować można regex pozwalający na wydobycie jedynie wyrazów \w
                # białych znaków \s i przecinka
                'order': ['document', 'columns']
                # już w tym miejscu 'nauczymy' nasz program, jaka jest kolejność występowania elementów w regeksie
            },
            'add': {
                'regex': '\s*ADD\s+\(([\w\s,])\)\s+TO\s+(\w*)',
                'order': ['values', 'document']
            },
            'select': {
                'regex': '\s*SELECT\s+\(([\w\s,])\)\s+FROM\s+(\w*)',
                'order': ['columns', 'document']
            }
        }

        self.FIELDS_TO_SPLIT = ['columns', 'values']
        # obie te stałe powinny zostać przeniesione do pliku constants.py

    def interpret(self, command):
        # to co tu było nie będzie już nam potrzebne. Jeżeli nic nie zwrócimy z fora, to rzucimy wyjątek

        # PĘTLA A
        for command_name, info in self.VALID_REGEX.items():
            found_data = re.findall(info['regex'], command, re.I)
            # zmieniłem nazwy zmiennych, żeby lepiej oddawały to, co przechowują
            if len(found_data):
                found_data = found_data[0]      # pozbywamy się zewnętrznej tablicy. found_data jest teraz tuplą

                ###################################
                # PRZYKLAD 1 - użycie zmiennych   #
                ###################################

                document_name = found_data[info['order'].index('document')] if 'document' in info['order'] else None
                # Jeżeli na liście 'order' jest słowo 'document', sprawdź pod jakim indeksem. Pod tym samym indeksem
                # będzie nazwa dokumentu w tupli document_name. Skąd to wiemy? Sami sworzyliśmy listę 'order' w taki
                # sposób, żeby tak było ;)
                columns = found_data[info['order'].index('columns')] if 'columns' in info['order'] else None
                values = found_data[info['order'].index('values')] if 'values' in info['order'] else None

                if columns is not None:
                    columns = re.sub('\s+', '', columns).split(',')
                    # usunięcie wszystkich białych znaków i podzielenie po przecinku dla kolumn i wartości
                if values is not None:
                    values = re.sub('\s+', '', values).split(',')

                ###################################
                # PRZYKLAD 2 - użycie słownika    #
                ###################################

                query = {'command': command_name}
                # PĘTLA B
                for i, elem in enumerate(info['order']):
                    query[elem] = found_data[i]
                # Najlepiej wytłumaczyć tę pętlę na przykładzie. Więc, w 2 obiegu pętli A rozważamy wartość\
                # info['order'] jako ['values', 'document']. Krotka found_data mogłaby wyglądać tak:
                # ('1, jadzia', 'uzytkownicy'). W pętli B iterujemy po info['order']. W pierwszym obiegu zmienna i = 0
                # elem = 'values'. Do słownika pod kluczem 'values' wpiszemy zatem wartość z zerowego elementu krotki.
                for key in self.FIELDS_TO_SPLIT:
                    if key in query:
                        query[key] = re.sub('\s+', '', query[key]).split(',')
                # w tym podejściu możemy w miarę uniwersalnie zdefiniować które pola podlegają podziałowi

                return command_name, document_name, columns, values                   # dla przykładu 1
                # return query.get('command', None), query.get('document', None), \
                #        query.get('columns', None), query.get('values', None)            # dla przykładu 2
        raise Exception("Interpretation failed")
        # Proszę napisać własną klase wyjątku ;)
