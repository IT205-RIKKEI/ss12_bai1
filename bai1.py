cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("\n====== SHOPEE CART MANAGEMENT SYSTEM ======")
    print("1. Xem chi tiết giỏ hàng và tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            print("\n--- CHI TIẾT GIỎ HÀNG ---")

            print(
                f"{'STT':<5} | "
                f"{'Mã SP':<10} | "
                f"{'Tên sản phẩm':<25} | "
                f"{'SL':<5} | "
                f"{'Đơn giá':<12} | "
                f"{'Thành tiền':<15}"
            )

            total_product = 0
            total_money = 0

            for index, value in enumerate(cart_items, start=1):
                money_product = value.get("number") * value.get("price")

                print(
                    f"{index:<5} | "
                    f"{value.get('id'):<10} | "
                    f"{value.get('name'):<25} | "
                    f"{value.get('number'):<5} | "
                    f"{value.get('price'):<12} | "
                    f"{money_product:<15}"
                )

                total_product += value.get("number")
                total_money += money_product

            print(f"\nTổng số lượng sản phẩm: {total_product}")
            print(f"Tổng tiền thanh toán: {total_money}")

        case "2":
            pro_id = input("Nhập mã sản phẩm: ")
            pro_name = input("Nhập tên sản phẩm: ")

            while True:
                pro_number = input("Nhập số lượng: ")

                if pro_number.isdigit():
                    pro_number = int(pro_number)
                    break

                print("Bạn nhập không hợp lệ!")

            while True:
                pro_price = input("Nhập đơn giá: ")

                if pro_price.isdigit():
                    pro_price = int(pro_price)
                    break

                print("Bạn nhập không phải số!")

            found = False

            for index, value in enumerate(cart_items):
                if pro_id == value.get("id"):
                    cart_items[index]["number"] = value.get("number") + pro_number
                    found = True

                    print("Sản phẩm đã tồn tại, cộng dồn số lượng thành công!")
                    break

            if not found:
                new_product = {
                    "id": pro_id,
                    "name": pro_name,
                    "number": pro_number,
                    "price": pro_price
                }

                cart_items.append(new_product)
                print("Thêm sản phẩm mới thành công!")

        case "3":
            update_pro_id = input("Nhập mã sản phẩm cần cập nhật: ")

            while True:
                update_pro_number = input("Nhập số lượng mới: ")

                if update_pro_number.isdigit():
                    update_pro_number = int(update_pro_number)
                    break

                print("Bạn nhập không hợp lệ!")

            found = False

            for index, value in enumerate(cart_items):
                if update_pro_id == value.get("id"):
                    cart_items[index]["number"] = update_pro_number
                    found = True

                    print("Cập nhật số lượng thành công!")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại!")

        case "4":
            del_pro_id = input("Nhập mã sản phẩm cần xóa: ")

            found = False

            for index, value in enumerate(cart_items):
                if del_pro_id == value.get("id"):
                    del cart_items[index]
                    found = True

                    print("Xóa sản phẩm thành công!")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại!")

        case "5":
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")