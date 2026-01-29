class DataNode:
    def __init__(self, data=None):
        # เก็บข้อมูล String
        self.data = data
        # เก็บ Address ของตัวถัดไป เริ่มต้นเป็น None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # เริ่มต้นมีโบกี้ 0 ตัว
        self.count = 0
        # เริ่มต้นยังไม่มีหัวขบวน
        self.head = None

    def insert_front(self, data):
        # สร้างโบกี้ใหม่ขึ้นมา
        p_new = DataNode(data)
        # ให้โบกี้ใหม่เอื้อมมือไปจับโบกี้ที่เป็นหัวหน้าเดิมไว้ (แม้หัวหน้าเดิมจะเป็น None ก็ตาม)
        p_new.next = self.head
        # แต่งตั้งโบกี้ใหม่ให้กลายเป็นหัวหน้าขบวนแทน
        self.head = p_new
        # พิ่มจำนวนนับโบกี้ขึ้น 1
        self.count += 1

    def insert_last(self, data):
        p_new = DataNode(data)
        if self.head is None:
            self.head = p_new
        else:
            # เดินหาโหนดสุดท้าย
            curr = self.head
            while curr.next:
                curr = curr.next
            # เอาตัวใหม่ไปต่อท้าย
            curr.next = p_new
        self.count += 1

    def traverse(self):
        # ถ้าไม่มีหัวขบวนเลย
        if self.head is None:
            print("This is an empty list.")
        else:
            # เริ่มเดินจากหัวขบวน
            curr = self.head
            while curr:
                if curr.next:
                    print(curr.data, end=" -> ")
                else:
                    print(curr.data)
                # ขยับไปโบกี้ถัดไป
                curr = curr.next

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        # แยกเงื่อนไข (F = หน้า, L = หลัง)
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()
