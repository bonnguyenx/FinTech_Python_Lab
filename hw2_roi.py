
# hw2_roi.py

def main():
    # Nhập dữ liệu từ bàn phím
    tong_von_ban_dau = float(input("Nhập tổng vốn ban đầu (Initial Investment): "))
    tong_gia_tri_ban = float(input("Nhập tổng giá trị bán ra (Final Value): "))

    # Tính lợi nhuận ròng (Net Profit)
    loi_nhuan_rong = tong_gia_tri_ban - tong_von_ban_dau

    # Tính tỷ lệ ROI (%) theo công thức: ROI(%) = (lợi_nhuận_ròng / tổng_vốn_ban_đầu) * 100
    roi = (loi_nhuan_rong / tong_von_ban_dau) * 100

    # In kết quả
    print(f"Lợi nhuận ròng (Net Profit): {loi_nhuan_rong:,.2f}")
    print(f"Tỷ lệ ROI: {roi:.2f}%")