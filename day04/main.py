# 4)模块与import使用
from utils import check_status_code
resp_Ok = {"code":200,"msg":"success","data":{"id":1}}
resp_fail = {"code":404,"msg":"not found","data":None}
is_ok = check_status_code(resp_Ok)
is_fail = check_status_code(resp_fail)
print("校验结果：",is_ok)
print("校验结果：",is_fail)