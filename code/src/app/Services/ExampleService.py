from ..Core.Services.BaseService import BaseService
from ..Data.Models.Example import Example


class ExampleService(BaseService):
    def __init__(self) -> None:
        super().__init__(Example)