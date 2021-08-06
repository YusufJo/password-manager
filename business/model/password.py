from dataclasses import dataclass


@dataclass
class Password:
    uid: str
    title: str
    pass_phrase: str
