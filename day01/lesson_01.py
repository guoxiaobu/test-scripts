# 变量与数据类型 int, float, str, bool；类型转换从配置文件读取字符串并转为数字
# test01_json文件
# Pathlib:它提供了面向对象、跨平台的文件系统路径操作方法，彻底取代了传统的 os.path字符串拼接方式。
import json
from pathlib import Path
data = json.loads(Path("config.json").read_text(encoding="utf-8"))
port = int(data['port'])
timeout = float(data['timeout'])
max_retries = int(data['max_retries'])
print(data,type(data))
print(port,type(port))
print(timeout,type(timeout))
print(max_retries,type(max_retries))

# test02_ini配置
# ConfigParser：Python 配置文件解析库，用以读写 .ini 格式配置文件的模块。
# 它让程序能够轻松管理配置参数，而无需硬编码在代码中。
import configparser
cfg = configparser.ConfigParser()
cfg.read("app.ini", encoding = "utf-8")
port = cfg.getint("server", "port")
timeout = cfg.getfloat( 'server', 'timeout')
print(port,type(port))
print(timeout,type(timeout))

# test03_环境变量
# dotenv实现配置与代码分离，避免敏感信息（如密码、API 密钥）硬编码在源代码中。
from dotenv import dotenv_values
env = dotenv_values(".env")
port = int(env["PORT"])
timeout = float(env["TIMEOUT"])

print(port,type(port))
print(timeout,type(timeout))