def credit_score(income, credit_history_years, has_bad_debt=False):
    # 1. Nếu có nợ xấu -> Từ chối lập tức
    if has_bad_debt == True:
        return "Reject"
    
    # 2. Nếu thu nhập dưới 10 triệu hoặc lịch sử tín dụng dưới 1 năm -> Rủi ro cao
    if income < 10000000 or credit_history_years < 1:
        return "High Risk"
    
    # 3. Nếu thu nhập từ 20 triệu trở lên và lịch sử tín dụng từ 3 năm trở lên -> VIP
    if income >= 20000000 and credit_history_years >= 3:
        return "VIP"
    
    # 4. Các trường hợp còn lại -> Standard
    return "Standard"

# --- Test thử một vài trường hợp ---
print(credit_score(15000000, 2, has_bad_debt=False))  # Kết quả: Standard
print(credit_score(25000000, 4, has_bad_debt=False))  # Kết quả: VIP
print(credit_score(8000000, 0, has_bad_debt=False))   # Kết quả: High Risk
print(credit_score(30000000, 5, has_bad_debt=True))   # Kết quả: Reject
