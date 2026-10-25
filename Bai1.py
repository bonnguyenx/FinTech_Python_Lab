target = 10000000000
age = 25 
year_count = 1
total_assets = 0 
deposit = 60000000

# In tieu de cua bang bao cao tien trinh 
print(f"{'Nam':<6} | {'Tuoi':,6} | {'So tien gui tien gui moi (VND)':<22} | {'Tien lai trong nam (VND)':<24} | {'Tong tai san cuoi nam (VND)'}")
print("-" * 105)
 
# Su dung ham While de lap ham tich luy 
while total_assets < target: 
    # Tinh tien lai trong nam (Tai san hien tai + Tien gui moi trong nam) * 10%
    interest = (total_assets + deposit) * 0.10 

    # Cap nhat tong tai san cuoi nam 
    total_assets = total_assets + deposit + interest 

    # In ra dong bao cao ket qua cua nam hien tai 
    print(f"{year_count:<6} | {age:<6} | {deposit:<22,.0f} | {interest:<24,.0f} | {total_assets:<20,.0f}")

    # Kiem tra neu tong tai san da dat hoac vuot muc tieu thi dung vong lap 
    if total_assets >= target:
        break

    # Tang tuoi len 1 cho nam tiep theo 
    age += 1
    # Tang so nam tich luy len 1 
    year_count += 1
    # So tien gui moi cua nam sau tang them 8% so voi nam truoc 
    deposit = deposit * 1.08 

print ("-" *105)
print(f"==> Ket qua: Nguoi nay dat muc tieu 10 ty VND o tuoi **{age}** sau **{year_count}** nam tich luy  ")
