# bai1_withdraw_check.py
print("==== HỆ THỐNG KIỂM DUYỆT RÚT TIỀN ATM ===")
#1. Khởi tạo dữ liệu tài khoản 
balance = 50000000.    # Số dư hiện tại: 5,000,000
MIN_BALANCE = 50000.   # SỐ dư duy trì tối thiểu: 50,000


#2. Nhập số tiền muốn rút từ bàn phím 
withdraw_amount = float(input(" Nhập số tiền Quý khách muốn rút (VNĐ) :"))

#3. Rẽ nhánh kiểm tra điều kiện 
if withdraw_amount <= 0:
    print(" GIAO DỊCH TỪ CHỐI: Số tiền rút phải lớn hơn 0 VNĐ. ")
elif (balance - withdraw_amount) >= MIN_BALANCE:
    # Thoả mãn điều kiện: Trừ số dư và thông báo 
    balance -= withdraw_amount
    print("----------------------------------------")
    print(f"GIAO DỊCH THÀNH CÔNG !")
    print(f" Số tiền đã rút : {withdraw_amount:,.0f} VNĐ")
    print(f" Số dư còn lại : {balance:,.0f} VNĐ")
else:
    # trường hợp số dư không duy trì
    max_drawable = balance - MIN_BALANCE
    print("------------------------------------")
    print("GIAO DỊCH TỪ CHỐI: Số dư không đủ!")
    print(f" Số tiền tối đa Quý khách có thể rút là: {max_drawable:,.0f}VNĐ")
