class Luggage:

    # 初始化行李屬性
    def __init__(self, luggage_id, weight, departure_airport, destination, passenger_name):
        self.luggage_id = luggage_id
        self.weight = weight
        self.departure_airport = departure_airport
        self.destination = destination
        self.passenger_name = passenger_name
    # 顯示行李資訊
    def display_info(self):
        print("行李資訊：")
        print(f"行李 ID：{self.luggage_id}")
        print(f"重量：{self.weight} 公斤")
        print(f"出發機場：{self.departure_airport}")
        print(f"目的地：{self.destination}")
        print(f"旅客姓名：{self.passenger_name}")

 

class BoardingPass:
    def __init__(self, passenger_name, registration_id, boarding_time, gate_number, seat, luggage_count, luggage_ids):
        self.passenger_name = passenger_name
        self.registration_id = registration_id
        self.boarding_time = boarding_time
        self.gate_number = gate_number
        self.seat = seat
        self.luggage_count = luggage_count
        self.luggage_ids = luggage_ids
# 顯示登機證資訊
    def display_info(self):
        print("\n登機證資訊：")
        print(f"旅客姓名：{self.passenger_name}")
        print(f"登記證 ID：{self.registration_id}")
        print(f"登機時間：{self.boarding_time}")
        print(f"登機門編號：{self.gate_number}")
        print(f"座位：{self.seat}")
        print(f"行李數：{self.luggage_count}")
        print(f"行李 ID：{', '.join(self.luggage_ids)}")

    def print_boarding_time(self):
        print(f"預計登機時間為 {self.boarding_time}")

# 創建行李和登機證實例並顯示資訊及呼叫副函式
luggage = Luggage("12345", 25, "Airport A", "Airport B", "Alice")
boarding_pass = BoardingPass("Alice", "ABCDE12345", "2024-01-05 08:00", "Gate 10", "24A", 2, ["12345", "67890"])

# 顯示行李資訊
luggage.display_info()
# 顯示登機證資訊
boarding_pass.display_info()
 # 印出預計登機時間
boarding_pass.print_boarding_time()
