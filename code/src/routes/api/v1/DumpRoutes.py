import azure.functions as func
from src.app.Controllers.DumpController import index, find, store, update, delete
from src.app.Services.DumpService import DumpService

service = DumpService()

def route_index(req: func.HttpRequest):
    return index(service, req)

def route_find(req: func.HttpRequest):
    return find(service, req)

def route_insert(req: func.HttpRequest):
    return store(service, req)

def route_update(req: func.HttpRequest):
    return update(service, req)

def route_delete(req: func.HttpRequest):
    return delete(service, req)

