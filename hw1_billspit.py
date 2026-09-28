
# hw1_billsplit.py

def main():
    # Nhập dữ liệu từ bàn phím
    x = float(input("Nhập tổng hóa đơn X (đồng): "))
    y = float(input("Nhập phần trăm tiền tip Y (%): "))
    n = int(input("Nhập số người chia N: "))

    # Tính tổng số tiền sau khi cộng tiền tip
    tong_tien = x * (1 + y / 100)

    # Tính số tiền mỗi người phải trả
    tien_moi_nguoi = tong_tien / n

    # Làm tròn đến số nguyên (0 chữ số thập phân)
    ket_qua = round(tien_moi_nguoi)

    print(f"Số tiền thực tế mỗi người phải trả: {ket_qua} đồng")
