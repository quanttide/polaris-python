
# ServiceMetadata 服务元数据信息
class ServiceMetadata(object):
    # 获取服务名
    def GetService(self)->str:
        return

    # 获取命名空间
    def GetNamespace(self):
        return

    # 获取元数据信息
    def GetMetadata(self):
        return


# ServiceInstances 服务实例列表
class ServiceInstances():
    # 获取服务实例列表
    def GetInstances(self):
        return

    # 获取全部实例总权重
    def GetTotalWeight(self):
        return


# GetOneInstanceRequest单个服务实例查询请求
class GetOneInstanceRequest():
    def __init__(
            self,
            service: str,  # 服务名
            namespace: str,  # 命名空间

    ):
        self.service = service
        self.namespace = namespace


# InstanceRegisterRequest 注册服务请求
class InstanceRegisterRequest(object):
    def __init__(
            self,
            service: str,  # 必选，服务名
            service_token: str,  # 必选，服务访问Token
            namespace: str,  # 必选，服务访问Token
            host: str,  # 必选，服务访问Token
            port: int,  # 必选，服务访问Token
            protocol: str = None,  # 必选，服务访问Token
            weight: int = 0,  # 必选，服务访问Token
    ):
        self.port = port
        self.host = host
        self.namespace = namespace
        self.service_token = service_token
        self.service = service
        self.weight = weight
        self.protocol = protocol
        url = f"http://{self.host}/{self.port}/naming/v1/services"
        data = {
            "name": self.service,
            "namespace": self.namespace,
        }
        return url, data


class InstanceRegisterResponse(object):
    def __init__(
            self,
            instance_id: str,  # 实例id
            existed: bool,  # 实例是否已存在
    ):
        return


class InstanceDeregisterRequest(object):
    def __init__(
            self,
            service: str,  # 必选，服务名
            service_token: str,  # 必选，服务访问Token
            namespace: str,  # 必选，服务访问Token
            host: str,  # 必选，服务访问Token
            port: int,  # 必选，服务访问Token
            protocol: str = None,  # 必选，服务访问Token
            weight: int = 0,  # 必选，服务访问Token
    ):
        self.port = port
        self.host = host
        self.namespace = namespace
        self.service_token = service_token
        self.service = service
        self.weight = weight
        self.protocol = protocol
