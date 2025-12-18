class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
                    pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def get_stack_top(self):
            if self.data == []:
                print("Underflow: Cannot get stack top from an empty list")
                return None
            return self.data[-1]

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)


Student = ArrayStack()
m = int(input())
n = int(input())

for _ in range(n):
    name = input()
    Student.push(name)

group = [""] * m # สร้าง list ที่เป็นข้อความว่าง "" ขึ้นมารอรับ input เป็นจำนวน m ตัว  ex m = 2 : ["", ""] 
group_index = 0 # ชี้ให้รู้ว่าเริ่มต้น index ที่ 0

while not Student.is_empty():
    st_name = Student.pop()

    if group[group_index] == "": #เช็คว่าถ้าเป็นคนแรกของกลุ่มรึเปล่า
        group[group_index] += st_name
    else: # ถ้ามีชื่อคนอื่นอยู่แล้ว ต้องเติม ", " นำหน้าก่อน แล้วค่อยใส่ชื่อ
        group[group_index] += ", " + st_name

    group_index += 1 # เลื่อนไปกล่มถัดไป

    if group_index >= m: # เช็คว่าใส่ข้อความครบจำนวนกลุ่มในแต่ละรอบรึยัง
        group_index = 0

for i in range(m): #ปริ้นแต่ละกลุ่มออกมา
    print(f"Group {i + 1}: {group[i]}")
