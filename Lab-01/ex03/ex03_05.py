def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_str = input("Nhập danh sách các phần tử ngăn cách bởi dấu cách: ")
lst = input_str.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(lst)
print("Số lần xuất hiện của mỗi phần tử trong list:", so_lan_xuat_hien)
