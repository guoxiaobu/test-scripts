res_ok = {"code":200,"msg":"ok","data":{"id",1}}
res_fail = {"code":401,"msg":"Unauthorized","data": {"id":2}}
res_fail1 = {"code":501,"msg":"Not Implemented","data":{"id":3}}
from utils_01 import check_status_code
print(check_status_code(res_ok))
print(check_status_code(res_fail))
print(check_status_code(res_fail1))

