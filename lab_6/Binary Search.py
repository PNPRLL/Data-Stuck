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

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    comparisons = 0
    
    found = False
    
    while low <= high:
        # คำนวณตำแหน่งกึ่งกลาง
        mid = (low + high) // 2
        comparisons += 1
        
        # ดึงชื่อจากตำแหน่งกลางมาเทียบ
        mid_name = data[mid].get_name()
        
        if mid_name == name:
            # กรณีเจอข้อมูล
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            found = True
            break
        elif mid_name < name:
            # ถ้าชื่อตรงกลาง น้อยกว่า ชื่อที่หา -> ไปหาฝั่งขวา
            low = mid + 1
        else:
            # ถ้าชื่อตรงกลาง มากกว่า ชื่อที่หา -> ไปหาฝั่งซ้าย
            high = mid - 1
            
    if found:
        print(f"Comparisons times: {comparisons}")
    else:
        # กรณีหาไม่เจอ (สังเกต: โจทย์ใช้คำว่า exists เติม s ในตัวอย่าง Output)
        print(f"{name} does not exists.")
        print(f"Comparisons times: {comparisons}")

def main():
    # รับข้อมูล JSON และชื่อที่ต้องการค้นหา
    input_data = json.loads(input())
    target_name = input()
    
    student_list = []
    
    # แปลงข้อมูลจาก Dictionary เป็น Object Student
    for s in input_data:
        std = Student(s["id"], s["name"], s["gpa"])
        student_list.append(std)
    binary_search(student_list, target_name)
main()
