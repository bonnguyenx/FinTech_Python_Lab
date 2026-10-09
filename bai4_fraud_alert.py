# bai4_fraud_alert.py

# 1. Khai báo các biến đầu vào (mô phỏng một giao dịch)
amount = 35000000
is_new_device = True
failed_pin = 1
hour = 2
is_foreign_ip = True

# 2. Kiểm tra các nhóm điều kiện cảnh báo rủi ro
# Nhóm điều kiện 1: Giá trị giao dịch trên 30,000,000 VNĐ VÀ thực hiện từ thiết bị mới
risk_group_1 = (amount > 30000000) and is_new_device

# Nhóm điều kiện 2: Nhập sai PIN từ 3 lần trở lên HOẶC (giao dịch lúc 0h-4h sáng VÀ từ IP nước ngoài)
risk_group_2 = (failed_pin >= 3) or ((0 <= hour <= 4) and is_foreign_ip)

# 3. Quyết định cảnh báo
if risk_group_1 or risk_group_2:
    print("ALERT: Giao dịch có dấu hiệu gian lận! Hệ thống tạm thời KHÓA THẺ.")
else:
    print("SUCCESS: Giao dịch an toàn. Đang xử lý lệnh thanh toán...")
