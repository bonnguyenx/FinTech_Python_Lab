def calculate_emi(principal, annual_rate, months):
    # Tính lãi suất theo tháng
    r = annual_rate / 12
    
    # Tính tiền trả góp hàng tháng (EMI)
    emi = principal * (r * (1 + r) ** months) / ((1 + r) ** months - 1)
    
    # Tính tổng tiền lãi trong toàn bộ chu kỳ
    total_interest = (emi * months) - principal
    
    # Trả về tuple chứa 2 giá trị
    return emi, total_interest

# --- Test case theo yêu cầu ---
P = 1000000000
rate = 0.12
n = 12

# Sử dụng Unpacking để nhận 2 giá trị trả về từ hàm
monthly_emi, total_interest = calculate_emi(P, rate, n)

# In kết quả định dạng số tiền
print(f"Trẻ mỗi tháng: {monthly_emi:,.0f} VNĐ | Tổng lãi phải trả: {total_interest:,.0f} VNĐ")
