from polaris_python.api.provider import *
import sys


class PolarisProvider(object):
    namespace_default = "default"

    def __init__(self):
        self.providerAPI = ProviderAPI

    def register(self, namesapce: str, service: str, host:str, port: int):
        registerRequest = InstanceRegisterRequest
        registerRequest.service = service
        registerRequest.namespace = namesapce
        registerRequest.host = host
        registerRequest.port = port
        registerRequest.serviceY = None
        response = self.providerAPI.Register(registerRequest)

    def deregister(self,namesapce: str, service: str, host:str, port: int):
        deregisterRequest = InstanceDeregisterRequest
        deregisterRequest.Service = service