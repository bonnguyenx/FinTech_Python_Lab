# 1. Khởi tạo các thông số ban đầu theo đề bài
v_goc = 20_000_000_000  # Giá trị danh mục gốc: 20 tỷ VNĐ

# Danh sách các kịch bản biến động Tỷ giá USD/VND 
delta_ex_list = [-0.03, 0.0, 0.03]

# Danh sách các kịch bản biến động Tỷ lệ Lãi suất 
delta_ir_list = [-0.02, -0.01, 0.01, 0.02]  # Tương ứng: -2%, -1%, +1%, +2%

# 2. In tiêu đề của bảng Ma trận độ nhạy 
print(f"{'Δex \\ Δir':<12} | " + " | ".join([f"{ir*100:>7.1f}%" for ir in delta_ir_list]))
print("=" * 95)
