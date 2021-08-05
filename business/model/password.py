from dataclasses import dataclass


@dataclass
class Password:
    uid: str
    name: str
    pass_phrase: str
