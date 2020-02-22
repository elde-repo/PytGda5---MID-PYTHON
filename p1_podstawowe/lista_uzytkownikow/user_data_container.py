from dataclasses import dataclass


@dataclass(frozen=True)
class UserDataContainer:
    first_name: str
    last_name: str
    nick: str
    phone: str
    active: bool
