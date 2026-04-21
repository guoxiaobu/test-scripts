# 1) list：增删改查
import token

cases = ['登录成功','登录失败-密码错误','注册成功']

# 查（Read）
print(cases[-1])     # 注册成功
print(len(cases))    # 列表长度：3

# 增（Create）
cases.append('找回密码成功')
cases.insert(1,'登录失败-用户不存在')
print(cases)
# 改 （Update）
cases[0] = '登录成功-正确的账号和密码'
print(cases)

# 删 （Delete）
cases.remove('注册成功')  #按值删除
deleted = cases.pop()   #删除最后一个并返回
print('删除了：',deleted)

print(cases)

# 2) dict:键值对（模拟json响应）
# 模拟接口 JSON 响应
resp = {
    "code": 200,
    "message": "success",
    "data": {
        "user_id": 1001,
        "token": "abc123"
    }
}

# 查（Look）
print(resp["code"])                  #200
print(resp["data"]["token"])         #abc123

# 增/改
resp['time'] = '40ms'               #新增字段
resp['message'] = 'ok'              #修改message字段值

# 删除
del resp['time']
print(resp)

# 常用操作：
# d["key"] 取值（key 不存在会报错）
# d.get("key", 默认值) 安全取值
# d["key"] = value 新增或修改
# del d["key"] 删除键

# 3) 实战：list 存用例 + dict 模拟响应

# 用 list 存测试用例
test_cases = [
    {"name": "正常登录", "username": "tom", "password": "123456"},
    {"name": "密码错误", "username": "tom", "password": "000000"},
    {"name": "用户不存在", "username": "nobody", "password": "123456"}
]

# 用 dict 模拟登录接口响应
def mock_login(username, password):
    if username == "tom" and password == "123456":
        return {"code":200,"msg":"登录成功","data":{"token":"token_xxx"}}
    elif username == "tom" and password == "00000":
        return {"code":401,"msg":"密码错误","data":None}
    else:
        return {"code":404,"msg":"用户不存在","data":None}
# 遍历用例执行
for case in test_cases:
    rsp = mock_login(case["username"], case["password"])
    print(f"用例：{case['name']} -> 响应：{rsp}")

# 4) 今日练习任务（建议你自己敲一遍）
# 新建一个 list，放 5 条测试用例标题，完成增删改查各 1 次。

list1 = ['注册成功','注册失败-用户名已使用','注册失败-邮箱已使用','注册失败-手机已使用','注册失败-邮箱已失效']
# 增加（Add）
list1.append('注册失败-重复注册')
# 修改（Update）
list1[0] = '注册成功-用户名，邮箱及手机正确'
# 删除（Del）
list1.remove('注册失败-邮箱已使用')
# 查询
print(list1)
# 写一个 dict，模拟“查询用户信息”接口响应（包含 code/msg/data）。
user_infosuccess_rsp = {
    "code": 200,
    "msg":"success",
    "data": {
        "user_id": 1001,
        "name":"Tom",
        "password":"123456"
    }
}
user_infofail_rsp = {
    "code": 404,
    "msg": "user not found",
    "data": None
}
# 在 data 里再放一个嵌套 dict（如 {"id":1,"name":"Tom"}），并取出 name 打印。
print("完整响应：",user_infosuccess_rsp)
user_name = user_infosuccess_rsp["data"]["name"]
print(user_name)
# 用 for 循环遍历你的用例列表并逐条打印。
for cs in list1:
    print(cs,end=' ')
print("_________________")

# 为什么不用 user_info_resp["data"]["name"]？
# 因为这种写法要求两个 key 都必须存在：
# 没有 data -> 直接报错 KeyError
# 有 data 但没有 name -> 也报错
# 而 get() 写法不会报错，会给你默认值。
user_name_safe = (user_infofail_rsp.get("data") or {}).get("name", "未知用户")
print("用户姓名(安全取值)：", user_name_safe)