# bai3_user_role_discount.py
print("=== HỆ THỐNG TÍNH PHÍ GIAO DỊCH TỰ ĐỘNG ===")
# 1. Nhập thông tin cấu hình
role = input("Nhập vai trò hệ thống (ADMIN / STAFF / USER):"). strip().upper()
member_type = input("Nhập hạng hội viên (VIP / STANDARD):"). strip().upper()
amount = float(input("Nhập giá trị giao dịch (VNĐ): "))
# 2. Xử lý phân quyền và tính phí
BASE_FEE_RATE = 0.01 # Mức phí gốc 1%
if role == "ADMIN" or role == "STAFF":
   fee = 0
   note = "Được miễn phí giao dịch (Đặc quyền Nội bộ)."
elif role == "USER":
      raw_fee = amount * BASE_FEE_RATE
if member_type == "VIP":
    fee = raw_fee * 0.5 # Giảm 50% cho VIP
    note = "Áp dụng ưu đãi giảm 50% phí cho Khách hàng VIP."

else:
 # Hạng STANDARD: Phí gốc 1%, tối thiểu 10,000 VNĐ
 fee = max(raw_fee, 10000)
 note = "Phí tiêu chuẩn 1% (Tối thiểu 10,000 VNĐ)."

else:
  fee = 0
  note = "LỖI: Vai trò người dùng không hợp lệ trong hệ thống."
# 3. Xuất hóa đơn chi tiết
print("\n---------------- KẾT QUẢ TÍNH PHÍ ----------------")
print(f"Giá trị chuyển tiền : {amount:,.0f} VNĐ")
print(f"Vai trò / Hạng thẻ : {role} / {member_type}")
print(f"Phí giao dịch : {fee:,.0f} VNĐ")
print(f"Ghi chú : {note}")
print("--------------------------------------------------")
