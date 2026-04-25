def check_status_code(response,expected_code=200):
    actual_code = response.get("code")
    return actual_code == expected_code
