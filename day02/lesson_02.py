test_cases = [
    {"id": 1, "name": "登录-正确账号密码", "result": "PASS"},
    {"id": 2, "name": "登录-错误密码", "result": "FAIL"},
    {"id": 3, "name": "查询订单", "result": "SKIP"},
]


pass_count = 0
fail_count = 0
skip_count = 0

for case in test_cases:
    if case["result"] == "PASS":
        print(f"[INFO] 用例{case['id']} {case['name']} 执行通过")
        pass_count += 1
    elif case["result"] == "FAIL":
        print(f"[ERROR] 用例{case['id']} {case['name']} 执行失败")
        fail_count += 1
    else:
        print(f"[WARN] 用例{case['id']} {case['name']} 被跳过")
        skip_count += 1

print("---- 执行汇总 ----")
print(f"PASS={pass_count}, FAIL={fail_count}, SKIP={skip_count}")

# while 循环
max_retry = 3
retry = 0
success = False
while retry < max_retry and not success:
    retry += 1
    # 这里模拟第3次才成功
    if retry == 3:
        success = True
        print("[info] 请求成功")
    else:
        print(f"[error] 第{retry}次请求失败")

# 第2天练习任务参考答案
# 任务：
# 1) 新增 BLOCKED 分支
# 2) 收集失败用例名称
# 3) while 控制“回归轮次”最多2轮（当失败数>0继续）

test_cases = [
    {"id": 1, "name": "登录-正确账号密码", "result": "PASS"},
    {"id": 2, "name": "登录-错误密码", "result": "FAIL"},
    {"id": 3, "name": "查询订单", "result": "SKIP"},
    {"id": 4, "name": "支付-风控拦截", "result": "BLOCKED"},
    {"id": 5, "name": "退款申请", "result": "PASS"},
]

max_rounds = 2
round_no = 1

# 用于演示：把失败用例名收集起来（每轮都收集）
all_failed_names_by_round = {}

while round_no <= max_rounds:
    print(f"\n===== 第{round_no}轮回归开始 =====")

    pass_count = 0
    fail_count = 0
    skip_count = 0
    blocked_count = 0
    failed_names = []

    for case in test_cases:
        result = case["result"]

        if result == "PASS":
            print(f"[INFO] 用例{case['id']} {case['name']} 执行通过")
            pass_count += 1
        elif result == "FAIL":
            print(f"[ERROR] 用例{case['id']} {case['name']} 执行失败")
            fail_count += 1
            failed_names.append(case["name"])
        elif result == "SKIP":
            print(f"[WARN] 用例{case['id']} {case['name']} 被跳过")
            skip_count += 1
        elif result == "BLOCKED":
            print(f"[WARN] 用例{case['id']} {case['name']} 被阻塞（BLOCKED）")
            blocked_count += 1
        else:
            print(f"[WARN] 用例{case['id']} {case['name']} 结果未知: {result}")

    all_failed_names_by_round[f"第{round_no}轮"] = failed_names

    print("---- 本轮汇总 ----")
    print(
        f"PASS={pass_count}, FAIL={fail_count}, "
        f"SKIP={skip_count}, BLOCKED={blocked_count}"
    )
    print(f"失败用例名称: {failed_names if failed_names else '无'}")

    # 任务3：如果失败数 > 0 且未超过最大轮次，就继续下一轮
    if fail_count > 0 and round_no < max_rounds:
        print("[INFO] 仍有失败用例，继续下一轮回归...")
        round_no += 1
    else:
        if fail_count == 0:
            print("[INFO] 无失败用例，回归结束。")
        else:
            print("[ERROR] 已达到最大回归轮次，仍存在失败。")
        break

print("\n===== 所有轮次失败用例汇总 =====")
for k, v in all_failed_names_by_round.items():
    print(f"{k}: {v if v else '无'}")