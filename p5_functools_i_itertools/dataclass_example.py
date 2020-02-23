import dataclasses
import typing


@dataclasses.dataclass()
class User:
    first_name: str
    last_name: str
    nick: str
    phone: typing.Optional[str] = None
    active: typing.Optional[bool] = True
    other: typing.Optional[dict] = None
