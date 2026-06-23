class DeliveryOrder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0.0
        self.delivery_status = ""
        self.calculate_total_cost()
        self.classify_delivery_status()

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost >= 600000:
            self.delivery_status = "Đơn hàng Đặc biệt (Ưu tiên cao - Rủi ro cao)"
        elif self.total_delivery_cost >= 300000:
            self.delivery_status = "Đơn hàng Đường dài (Cần giám sát)"
        elif self.total_delivery_cost >= 100000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        else:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"


class OrderManager:
    def __init__(self):
        self.orders: list[DeliveryOrder] = []


    def show_all_orders(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào.")
            return
        print(f"{'Mã Đơn':<12} | {'Tên người nhận':<20} | {'Cước nền':<12} | {'KC (km)':<8} | {'Phụ phí':<12} | {'Tổng chi phí':<14} | {'Trạng thái đơn'}")
        for o in self.orders:
            print(f"{o.order_id:<12} | {o.receiver_name:<20} | {o.base_fee:<12f} | {o.distance:<8} | {o.surcharge:<12f} | {o.total_delivery_cost:<14f} | {o.delivery_status}")

    def add_order(self):
        print("\n--- Nhập thông tin vận đơn mới ---")
        while True:
            order_id = input("Mã vận đơn: ").strip()
            if not order_id:
                print("Không được để trống, nhập lại!")
                continue
            for o in self.orders:
                if o.order_id == order_id:
                    print("Mã vận đơn đã tồn tại, nhập lại!")
                    break
            else:
                break
        while True:
            receiver_name = input("Tên người nhận: ").strip()
            if not receiver_name:
                print("Không được để trống, nhập lại!")
                continue
            break
        while True:
            try:
                base_fee = float(input("Cước phí nền (VNĐ/km): "))
                if base_fee <= 0:
                    print("Không được bé hơn 0, nhập lại!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")
        while True:
            try:
                distance = int(input("Khoảng cách giao hàng (km, 1-5000): "))
                if distance < 1 or distance > 5000:
                    print("Phải nằm trong khoảng từ 1 đến 5000, nhập lại!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")
        while True:
            try:
                surcharge = float(input("Phụ phí (VNĐ): "))
                if surcharge <= 0:
                    print("Không được bé hơn 0, nhập lại!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")
        order = DeliveryOrder(order_id, receiver_name, base_fee, distance, surcharge)
        self.orders.append(order)
        print(f"Đã thêm vận đơn '{order_id}' thành công.")
        print(f"Tổng chi phí: {order.total_delivery_cost:f} VNĐ | Trạng thái: {order.delivery_status}")

    def update_order(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào.")
            return
        order_id = input("Nhập mã vận đơn cần cập nhật: ").strip()
        order = None
        for o in self.orders:
            if o.order_id == order_id:
                order = o
                break
        if order is None:
            print("Không tìm thấy vận đơn.")
            return
        while True:
            try:
                order.base_fee = float(input("Cước phí nền mới (VNĐ/km): "))
                if order.base_fee <= 0:
                    print("Không được bé hơn 0, nhập lại!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")
        while True:
            try:
                order.distance = int(input("Khoảng cách mới (km, 1-5000): "))
                if order.distance < 1 or order.distance > 5000:
                    print("Phải nằm trong khoảng từ 1 đến 5000, nhập lại!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")
        while True:
            try:
                order.surcharge = float(input("Phụ phí mới (VNĐ): "))
                if order.surcharge <= 0:
                    print("Không được bé hơn 0, nhập lại!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")
        order.calculate_total_cost()
        order.classify_delivery_status()
        print(f"Đã cập nhật vận đơn '{order_id}' thành công.")
        print(f"Tổng chi phí mới: {order.total_delivery_cost:f} VNĐ | Trạng thái mới: {order.delivery_status}")

    def delete_order(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào.")
            return
        order_id = input("Nhập mã vận đơn cần xóa: ").strip()
        order = None
        for o in self.orders:
            if o.order_id == order_id:
                order = o
                break
        if order is None:
            print("Không tìm thấy vận đơn.")
            return
        confirm = input("Bạn có chắc muốn xóa vận đơn này khỏi hệ thống không? (Y/N): ").strip()
        if confirm.lower() == "y":
            self.orders.remove(order)
            print(f"Đã xóa vận đơn '{order_id}' khỏi hệ thống.")
        else:
            print("Hủy thao tác xóa.")

    def search_by_receiver(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào.")
            return
        keyword = input("Nhập tên người nhận cần tìm: ").strip().lower()
        results = []
        for o in self.orders:
            if keyword in o.receiver_name.lower():
                results.append(o)
        if not results:
            print("Không tìm thấy vận đơn phù hợp.")
            return
        print(f"{'Mã Đơn':<12} | {'Tên người nhận':<20} | {'Cước nền':<12} | {'KC (km)':<8} | {'Phụ phí':<12} | {'Tổng chi phí':<14} | {'Trạng thái đơn'}")
        for o in results:
            print(f"{o.order_id:<12} | {o.receiver_name:<20} | {o.base_fee:<12f} | {o.distance:<8} | {o.surcharge:<12f} | {o.total_delivery_cost:<14f} | {o.delivery_status}")


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khỏi hệ thống
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
=====================================""")

def main():
    manager = OrderManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1":
                manager.show_all_orders()
            case "2":
                manager.add_order()
            case "3":
                manager.update_order()
            case "4":
                manager.delete_order()
            case "5":
                manager.search_by_receiver()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6.")

if __name__ == "__main__":
    main()