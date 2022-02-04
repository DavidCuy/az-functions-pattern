from ..Core.Services.BaseService import BaseService
from ..Data.Models.Dump import Dump


class DumpService(BaseService):
    def __init__(self) -> None:
        super().__init__(Dump)