# 1. Khởi tạo các thông số đầu vào của trái phiếu theo đề bài

F = 1_000_000       # Mệnh giá trái phiếu (VNĐ)
c = 0.09            # Lãi suất coupon: 9%/năm
N = 10              # Thời hạn trái phiếu: 10 năm
y = 0.085           # Tỷ lệ lợi suất kỳ vọng của thị trường (YTM): 8.5%/năm

# 2. Tính số tiền lãi coupon trả hàng năm: C = F * c

C = F * c

# In tiêu đề bảng chi tiết giá trị hiện tại (PV) từng năm

print(f"{'Năm (t)':<8} | {'Tiền Coupon (VNĐ)':<20} | {'Giá trị hiện tại PV (VNĐ)'}")
print("-" * 55)

# 3. Tạo biến tổng PV của các khoản lãi coupon và dùng vòng lặp for để chiết khấu từng năm

tong_pv_coupon = 0.0

for t in range(1, N + 1):
    # Tính giá trị hiện tại (PV) của khoản tiền lãi coupon ở năm thứ t
    pv_c = C / ((1 + y) ** t)
    
    # Cộng dồn giá trị PV của coupon vào tổng
    tong_pv_coupon += pv_c
    
    # In ra giá trị chiết khấu từng năm
    print(f"Năm {t:<4} | {C:<20,.2f} | {pv_c:<20,.2f}")

print("-" * 55)

# 4. Tính giá trị hiện tại (PV) của khoản nợ gốc nhận lại vào năm thứ 10

pv_f = F / ((1 + y) ** N)

# 5. Tính tổng giá lý thuyết chuẩn của trái phiếu (P0) = Tổng PV coupon + PV mệnh giá gốc

gia_trai_phieu = tong_pv_coupon + pv_f

# 6. Đánh giá trạng thái giá trái phiếu so với mệnh giá

if gia_trai_phieu > F:
    trang_thai = "Cao hơn mệnh giá (Premium - Trái phiếu có lãi)"
elif gia_trai_phieu < F:
    trang_thai = "Thấp hơn mệnh giá (Discount - Trái phiếu có hại)"
else:
    trang_thai = "Đúng mệnh giá (Par)"

# 7. In kết quả tổng kết cuối cùng

print(f"\n--- KẾT QUẢ ĐỊNH GIÁ TRÁI PHIẾU ---")
print(f"- Tổng giá trị hiện tại của các khoản coupon: {tong_pv_coupon:,.2f} VNĐ")
print(f"- Giá trị hiện tại của mệnh giá gốc (sau 10 năm): {pv_f:,.2f} VNĐ")
print(f"- Giá lý thuyết chuẩn của trái phiếu (P0): {gia_trai_phieu:,.2f} VNĐ")
print(f"- Đánh giá: Trái phiếu đang được bán **{trang_thai}**")
