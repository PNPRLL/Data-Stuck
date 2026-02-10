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

def main(text_in):
    import json
    std_in = json.loads(text_in)
    # สร้าง object Student จากข้อมูล JSON
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
