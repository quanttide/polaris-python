# 快速开始样例

---
## 样例说明

---
本样例演示如何使用 polaris-python 完成被调端以及主调端应用接入polaris，并完成服务调用流程。

## 样例

---
### 如何接入
1. 首先修改requirement.txt文件，引入polaris_python

```text
    polaris_python==0.0.1
```

2.在当前目录下创建配置文件 polaris.yaml，配置文件中配置 Polaris Server 地址。
```yaml
global:
  serverConnector:
    addresses:
    - 127.0.0.1:8090
```

### 运行

