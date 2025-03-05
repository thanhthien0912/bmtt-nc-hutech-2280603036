def tinh_tong_so_chan(lst):
    tong = 0
    for n in lst:
        if n % 2 == 0:
            tong += n
    return tong

input_list = input("Nhập danh sách các số ngăn cách bởi dấu phẩy: ")
input_list = list(map(int, input_list.split(",")))

kq = tinh_tong_so_chan(input_list)
print("Tổng các số chẵn trong list là:", kq)
