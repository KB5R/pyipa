from dataclasses import dataclass


@dataclass
class User:
    username: str
    first_name: str
    last_name: str
    disabled: bool
