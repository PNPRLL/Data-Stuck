import json

class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    # Getter methods
    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.gpa

    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        # จัดรูปแบบ GPA ให้เป็นทศนิยม 2 ตำแหน่งเสมอ (เช่น 3.0 -> 3.00)
        print(f"GPA: {self.gpa:.2f}")

class ProbHash:
    def __init__(self, size):
        # สร้างลิสต์ว่างขนาด size โดยกำหนดค่าเริ่มต้นเป็น None
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key):
        # Hash Function แบบ Modulo-division
        return key % self.size

    def rehash(self, hkey):
        # Rehash แบบ Linear Probing ขยับไปช่องถัดไปทีละ 1
        return (hkey + 1) % self.size

    def insert_data(self, student):
        key = student.get_std_id()
        idx = self.hash(key)
        
        # เก็บตำแหน่งเริ่มต้นไว้เช็คกรณีวนครบรอบ
        original_idx = idx
        
        while self.hash_table[idx] is not None:
            # ถ้าช่องไม่ว่าง ให้ Rehash ไปช่องถัดไป
            idx = self.rehash(idx)
            
            # ถ้าวนกลับมาที่เดิมแสดงว่าเต็มทุกช่องแล้ว
            if idx == original_idx:
                print(f"The list is full. {key} could not be inserted.")
                return

        # เมื่อเจอช่องว่าง (None) ก็ใส่ข้อมูลลงไป
        self.hash_table[idx] = student
        print(f"Insert {key} at index {idx}")

    def search_data(self, std_id):
        idx = self.hash(std_id)
        original_idx = idx
        
        while self.hash_table[idx] is not None:
            # ถ้าเจอ ID ที่ตรงกัน
            if self.hash_table[idx].get_std_id() == std_id:
                print(f"Found {std_id} at index {idx}")
                return self.hash_table[idx]
            
            # ถ้ายังไม่เจอ ให้ขยับไปดูช่องถัดไป (Linear Probing)
            idx = self.rehash(idx)
            
            # ถ้าวนกลับมาที่เดิมแล้วยังไม่เจอ แปลว่าไม่มีข้อมูลนี้
            if idx == original_idx:
                break
        
        # กรณีออกจากลูป (เจอช่องว่าง หรือวนครบแล้วไม่เจอ)
        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")

main()
