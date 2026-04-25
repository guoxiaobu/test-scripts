def check_status_code(response, expected_code=200):
    actual_code = response.get("code")
    if actual_code == expected_code:
        return True,f"Pass,code = {actual_code}"
    else:
        return False,f"Fail,code = {actual_code},expect_code = {expected_code}"


