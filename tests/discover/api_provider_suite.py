import unittest
from polaris_python.api.provider import *
providerNamespace = "Polaris"
providerService = "polaris.monitor"
providerIPAddress = "101.226.94.24"
providerPort = 8090
providerInstanceIP = "101.226.94.24"
providerInstancePort = 8090


class ProviderTestCase(unittest.TestCase):
    def __init__(self):
        self.mockServer = None
        self.serviceToken = None
        self.provider = ProviderAPI

    def get_name(self):
        return "Provider"

    def testProvider(self):
        registerReq = InstanceRegisterRequest()
        registerReq.namespace = providerNamespace
        registerReq.service = providerService
        registerReq.host = providerInstanceIP
        registerReq.port = providerInstancePort
        regResp = self.provider.Register(registerReq)


if __name__ == '__main__':
    unittest.main()
