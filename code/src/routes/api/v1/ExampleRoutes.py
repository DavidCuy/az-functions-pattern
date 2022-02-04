import azure.functions as func
from src.app.Controllers.ExampleController import index, find
from src.app.Services.ExampleService import ExampleService

service = ExampleService()

def route_index(req: func.HttpRequest):
    return index(service, req)

def route_find(req: func.HttpRequest):
    return find(service, req)
