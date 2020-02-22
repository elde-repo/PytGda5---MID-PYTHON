from user_data_container import UserDataContainer


class UsersData:
    def __init__(self):
        self.users = []

    def add_user(self, first_name: str, last_name: str, nick: str = None, phone: str = None, active: bool = True) -> None:
        if nick is None:
            nick = (first_name[:3] + last_name[:3]).lower()

        new_user = UserDataContainer(first_name, last_name, nick, phone, active)
        self.users.append(new_user)

    def remove_user(self, i: int) -> None:
        if len(self.users) > i:
            self.users.pop(i)

    def __repr__(self) -> str:
        r = ""
        for user in self.users:
            r += f"first name:  {user.first_name}\n"
            r += f"last name:   {user.last_name}\n"
            r += f"nick:        {user.nick}\n"
            r += f"phone:       {user.phone}\n"
            r += f"active:      {user.active}\n\n"
        return r
