# url, parser, path, api, apikey 전부 str 타입
from dataclasses import dataclass

@dataclass
class Entity:
    
    url: str = ''
    path: str = ''
    api: str = ''
    apikey: str = ''

