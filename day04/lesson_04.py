# 1) 函数基础：定义 + 参数 + 返回值
def add(a,b):
    return a+b

result = add(3,5)
print(result)

# 解释：def add（a,b）为定义函数，a,b为入参
# return 把结果返回调用方
# add(3,5) 是传参调用

# 2）实战函数：校验响应码状态
resp = {"code":200,"msg":"success","data":{"id":1}}

# 封装函数

def check_status_code(response,expected_code=200):
    """
    校验响应中的 code 是否等于 expected_code
    :param response:接口响应（dict）
    :param status_code:期望状态码，默认200
    :return:True/False
    """
    actual_code = response.get("code")
    if actual_code == expected_code:
        return True
    return False
resp_ok = {"code":200,"msg":"success","data":{"id":1}}
resp_fail = {"code":404,"msg":"not found","data":None}

print(check_status_code(resp_ok))                       #True
print(check_status_code(resp_fail))                     #False
print(check_status_code(resp_fail,404))     #True


# 升级版：返回更清晰的信息（测试里更实用）
def check_status_code_v2(response,expected_code=200):
    actual_code = response.get("code")
    if actual_code == expected_code:
        return True,f"PASS:code={actual_code}"
    else:
        return False,f"FAIL:code={actual_code},expected_code={expected_code}"


print(check_status_code_v2(resp_ok))                       #True
print(check_status_code_v2(resp_fail))                     #False
print(check_status_code_v2(resp_fail,404))     #True

# 5)课后练习-1

