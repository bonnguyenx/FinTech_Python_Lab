# bai2_credit_scoring.py
print("=== HỆ THỐNG XẾP HẠNG TÍN DỤNG TỰ ĐỘNG (CIC) ===")
# 1. Nhập điểm tín dụng
score = int(input("Nhập điểm tín dụng của khách hàng (0 - 1000): "))
# 2. Phân loại theo cấu trúc rẽ nhánh đa luồng if-elif-else
if score < 0 or score > 1000:
print("LỖI DỮ LIỆU: Điểm tín dụng không hợp lệ! Vui lòng nhập trong khoảng 0 - 1000.")
elif score >= 800:
 risk_level = "RẤT THẤP (Very Low Risk)"
action = "Tự động duyệt hạn mức tín dụng tối đa (100,000,000 VNĐ)."
elif score >= 650:
 risk_level = "THẤP (Low Risk)"
action = "Duyệt hạn mức tín dụng tiêu chuẩn (50,000,000 VNĐ)."
elif score >= 500:
 risk_level = "TRUNG BÌNH (Medium Risk)"
action = "Chuyển hồ sơ sang bộ phận thẩm định tài sản thế chấp."
else:
 risk_level = "CAO (High Risk)"
action = "TỪ CHỐI CẤP TÍN DỤNG (Có nguy cơ nợ xấu)."
# 3. In báo cáo thẩm định
if 0 <= score <= 1000:
print("\n--------------- KẾT QUẢ THẨM ĐỊNH --------------")
print(f"Điểm đánh giá : {score} / 1000")
print(f"Mức độ rủi ro : {risk_level}")
print(f"Quyết định : {action}")
print("-----------------------------------------------")
