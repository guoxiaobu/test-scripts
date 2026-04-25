# question1（基础）:定义一个函数 say_hello(name)，传入姓名后返回："你好，xxx"。
def sayhello(name):
    return f"Hello,{name}"

print(sayhello('Guoxiaobu'))

# question2（参数+返回值）:定义函数 add(a, b)，返回两数之和，并调用一次打印结果。
def add(a,b):
    return a+b
print(add(3,2))

# question3:定义函数 check_status_code(response, expected_code=200)：
# 从 response 中取 code
# 比较是否等于 expected_code
# 返回 True/False

def check_status_code(response,expected_code=200):
    actual_code = response.get('code')
    if actual_code == expected_code:
        return True
    else:
        return False
# question4:准备三个响应字典：
# # {"code": 200, ...}
# {"code": 401, ...}
# {"code": 500, ...}
# 用循环调用 check_status_code，统一校验期望值 200，打印每条结果。
res_ok = {"code":200,"msg":"ok","data":{"id",1}}
res_fail = {"code":401,"msg":"Unauthorized","data": {"id":2}}
res_fail1 = {"code":501,"msg":"Not Implemented","data":{"id":3}}
print(check_status_code(res_ok))
print(check_status_code(res_fail))
print(check_status_code(res_fail1))


