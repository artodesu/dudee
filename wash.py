import time

# กำหนดค่าคงที่
COIN_VALUE = 10
PROGRAM_TIME = 60
ALERT_TIME = 10

# คลาสเครื่องซักผ้า
class WashingMachine:
    def __init__(self, model_number, brand, model):
        self.model_number = model_number
        self.brand = brand
        self.model = model
        self.status = "idle"
        self.time_left = 0

    def start(self):
        self.status = "washing"
        self.time_left = PROGRAM_TIME

    def tick(self):
        self.time_left -= 1
        if self.time_left == ALERT_TIME:
            print(f"เครื่อง {self.model_number} ({self.brand} {self.model}) ใกล้เสร็จสิ้นการซักผ้า!")
        elif self.time_left <= 1:
            self.status = "finished"

    def show_status(self):
        print("Model number:", self.model_number)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Status:", self.status)
        print("Time left:", self.time_left)

# ฟังก์ชันรับเหรียญ
def get_coins():
    coins = int(input("ใส่เหรียญ (20) ไม่มีการทอนเงิน: "))
    if coins > 100:
        print("จำนวนเหรียญเกินจำนวนสูงสุด")
        return 0
    else:
        return coins

# ฟังก์ชันแจ้งเตือน
def notify(message):
    print(message)

# ฟังก์ชันหลัก
def main():
    # สร้างเครื่องซักผ้าหลายเครื่อง
    washing_machines = [
        WashingMachine(model_number="WM-1", brand="Brand1", model="ModelA"),
        WashingMachine(model_number="WM-2", brand="Brand2", model="ModelB"),
        WashingMachine(model_number="WM-3", brand="Brand3", model="ModelC")
    ]

    # แสดงเครื่องซักผ้าทั้งหมดที่ให้ผู้ใช้เลือก
    print("เลือกเครื่องซักผ้า:")
    for i, machine in enumerate(washing_machines, start=1):
        print(f"{i}. {machine.model_number} ({machine.brand} {machine.model})")

    # ให้ผู้ใช้เลือกเครื่องซักผ้า
    selected_machine_index = int(input("เลือกเครื่องซักผ้า (1-3): ")) - 1

    # รับเหรียญจากลูกค้า
    coins = get_coins()

    # ตรวจสอบจำนวนเหรียญ
    if coins >= COIN_VALUE:
        # เริ่มต้นการซักผ้าสำหรับเครื่องที่ถูกเลือก
        selected_machine = washing_machines[selected_machine_index]
        selected_machine.start()

        # ทำงานวนไปเรื่อยๆ จนกว่าการซักผ้าที่ถูกเลือกจะเสร็จสิ้น
        while selected_machine.status != "finished":
            time.sleep(1)
            selected_machine.tick()
            selected_machine.show_status()

        # แจ้งเตือนเมื่อการซักผ้าเสร็จสิ้น
        notify(f"การซักผ้าเสร็จสิ้น สำหรับเครื่อง {selected_machine.model_number} ({selected_machine.brand} {selected_machine.model})")
    else:
        print("จำนวนเหรียญไม่เพียงพอ")

# เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()
