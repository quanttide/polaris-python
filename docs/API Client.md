# 北极星APIClient
## 用例
examples/api_client.py
```python
from polaris_python import PolarisAPIClient

polaris_client = PolarisAPIClient(host='101.226.153.96')
result = polaris_client.discover(name='qtclass', namespace='qtclass')
print(result)
result2 = polaris_client.get_namespaces(names = [{"name": "...", "comment": ""}])
```

## 代码
```python
class PolarisAPIClient(object):
    def __init__(self, host):
        self.host = host
        
    def request_api(self, api_path, api_params):
        # i.e. http://101.226.153.96:8090/v1/Discover
        url = f"http://{self.host}:8090/{api_path}"
        r = requests.post(url=url, json=api_params)
        return r.json()
        
    def discover(self, name, namespace):
        # i.e. 
        # {
    #     "type":3,  
#     "service":{
 #         "name":"qtclass", 
#         "namespace":"qtclass"
   #      }
        # }
        data = {'type':3,
                'service':{
                    'name':name,
                    'namespace':namespace
                    }
                }
        return self.request_api(api_path='/v1/Discover', api_params=data)
    
    def get_namespaces(self):
        pass
```

## API格式
https://polarismesh.cn/zh/doc/参考文档/接口文档/服务发现.html#服务发现

request: 
```json
POST http://101.226.153.96:8090/v1/Discover
Content-Type: application/json
{
     "type":3,
     "service":{
       "name":"qtclass", 
       "namespace":"qtclass" 
      }
}
```

response:
```json
{
    "code": 200000,
    "info": "execute success",
    "type": "ROUTING",
    "service": {
        "name": "qtclass",
        "namespace": "qtclass",
        "metadata": {},
        "ports": null,
        "business": null,
        "department": null,
        "cmdb_mod1": null,
        "cmdb_mod2": null,
        "cmdb_mod3": null,
        "comment": null,
        "owners": null,
        "token": null,
        "ctime": null,
        "mtime": null,
        "revision": null,
        "platform_id": null,
        "total_instance_count": null,
        "healthy_instance_count": null,
        "user_ids": [],
        "group_ids": [],
        "remove_user_ids": [],
        "remove_group_ids": [],
        "id": null,
        "editable": null
    },
    "instances": [],
    "routing": null,
    "rateLimit": null,
    "circuitBreaker": null,
    "services": []
}
```



