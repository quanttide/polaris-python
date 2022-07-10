"""
API Client 基本类
"""
import requests


class BasePolarisAPIClient(object):
    def __init__(self, host):
        self.host = host

    def request_api(self, api_path, api_params):
        # i.e. http://101.226.94.246:8090/v1/Discover
        url = f"http://{self.host}:8090/{api_path}"
        r = requests.get(url=url, json=api_params)
        return r.json()

    def parse_params(self):
    def discover(self, name, namespace):
        # i.e.
        # {
        #     "type":3,
        #     "service":{
        #         "name":"qtclass",
        #         "namespace":"qtclass"
        #      }
        # }
        data = {
            "type": 1,
            "service": {
                "name": name,
                "namespace":namespace,
            }
                }
        api_path = "v1/Discover"
        return self.request_api(api_path=api_path, api_params=data)

    def get_services(self, **kwargs):
        data = {
  	        "type": 6,
  	        "service": {
    	        "name": None,
    	        "namespace": None,
		        "business": None,
                "metadata":None
  	        }
        }
        data.update(**kwargs)
        api_path = "v1/Discover"
        return self.request_api(api_path=api_path, api_params=data)

    def get_namespaces(self,namespace, **kwargs):
        ## 这里想使用kwarg设置可选参数并添加，但是不太会使用kwarg
        api_path = f"naming/v1/namespaces?name={namespace}"
        url = f"http://{self.host}:8090/{api_path}"

        r = requests.get(url=url)
        return r.json()


