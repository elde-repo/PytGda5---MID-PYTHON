from collections import namedtuple

Krolestwo = namedtuple('Krolestwo', "krol krolowa ksiezniczka ksiaze")

kingdom = Krolestwo('Karol I', 'Katarzyna', 'Marianna', 'Wieslaw')
print(kingdom)
print(type(kingdom))
