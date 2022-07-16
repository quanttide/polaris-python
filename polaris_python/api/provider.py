from polaris_python.model import service
import requests

class InstanceRegisterRequest(service.InstanceRegisterRequest):
    def __init__(self):
        return


class InstanceDeregisterRequest(service.InstanceDeregisterRequest):
    def __init__(self):
        return


class ProviderAPI(object):
    def __init__(
            self
    ):
        return

    def Register(self, instance: InstanceRegisterRequest):
        response = requests.post(instance)
        print(response)
