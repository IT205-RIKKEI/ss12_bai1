def get_validate_input(prompt:str, input_type:str="str"):
    while True:
        data = input(prompt).strip()
        if data == "":
            print("Dữ liệu không được để trống! Nhập lại.")
            continue
        if input_type == "int":
            if not data.isdigit():
                print("Vui lòng nhập số nguyên!")
                continue
            value = int(data)
            if value <= 0:
                print("Số lượng phải lớn hơn 0! Nhập lại.")
                continue
            return value
        return data

def show_inventory(inventory):
    if len(inventory) == 0:
        print("Kho hàng hiện đang trống!")
        return
    print("DANH SÁCH HÀNG TỒN KHO")
    print(f"{'ID':<10}| {'Tên hàng hóa':<25}| {'Số lượng tồn'}")
    for item in inventory:
        print(
            f"{item['id']:<10}| "
            f"{item['name']:<20}| "
            f"{item['quantity']}"
        )

def add_item(inventory):
    print("NHẬP HÀNG HÓA MỚI")
    item_id = get_validate_input("Nhập mã hàng hóa: ")
    item_name = get_validate_input("Nhập tên hàng hóa: ")
    quantity = get_validate_input("Nhập số lượng tồn kho: ", "int")

    new_item = {"id": item_id,"name": item_name,"quantity": quantity}
    inventory.append(new_item)
    print("Thêm hàng hóa vào kho thành công")

def update_quantity(inventory):
    print("CẬP NHẬT SỐ LƯỢNG TỒN KHO")
    item_id = get_validate_input("Nhập mã hàng hóa cần sửa: ")
    for item in inventory:
        if item["id"] == item_id:
            print(
                f"Tìm thấy hàng hóa: {item['name']} "
                f"(Số lượng hiện tại: {item['quantity']})"
            )
            new_quantity = get_validate_input("Nhập số lượng mới: ","int")
            item["quantity"] = new_quantity
            print("Cập nhật số lượng thành công!")
            return
    print(f"Không tìm thấy hàng hóa có mã [{item_id}]")

def menu():
    print("\n===== QUẢN LÝ KHO HÀNG =====")
    print("1. Xem danh sách hàng tồn kho")
    print("2. Nhập thêm hàng hóa mới")
    print("3. Cập nhật số lượng tồn kho")
    print("4. Thoát chương trình")

inventory = [
    {
        "id": "G01",
        "name": "Gạo tẻ",
        "quantity": 50
    },
    {
        "id": "G02",
        "name": "Mì tôm",
        "quantity": 120
    }
]

while True:
    menu()
    choice = input("Mời bạn chọn chức năng (1-4): ")
    match choice:
        case "1":
            show_inventory(inventory)
        case "2":
            add_item(inventory)
        case "3":
            update_quantity(inventory)
        case "4":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")