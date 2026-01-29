class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # ตัวนับว่าตอนนี้ในลิสต์มีโหนดกี่ตัวแล้ว
        self.count = 0
        # ตัวแปรสำคัญที่ใช้จำว่าใครคือโหนดแรกของขบวน
        self.head = None

    def insert_last(self, data):
        # สร้างโหนดใหม่ขึ้นมาเตรียมไว้
        p_new = DataNode(data)
        # ถ้าลิสต์ยังว่าง (ไม่มีหัวขบวน) ให้โหนดใหม่นี้เป็นหัวขบวนทันที
        if self.head is None:
            self.head = p_new
        else:
            # ถ้ามีโหนดอยู่แล้ว ต้องเดินหาโหนดสุดท้ายให้เจอ
            curr = self.head
            # วนลูปไปเรื่อยๆ จนกว่าจะเจอโหนดที่แขน (next) ยังไม่ได้จับกับใคร
            while curr.next:
                curr = curr.next
            # พอเจอตัวสุดท้ายแล้ว ก็เอาแขนของมันมาจับโหนดใหม่ที่เราสร้างไว้
            curr.next = p_new
        # เพิ่มจำนวนนับโหนดขึ้น 1 ตัว
        self.count += 1

    def traverse(self):
        # ถ้าหัวขบวนเป็นว่าง แสดงว่าไม่มีข้อมูลเลย
        if self.head is None:
            print("This is an empty list.")
        else:
            # เริ่มต้นเดินจากโหนดแรก (Head)
            curr = self.head
            # วนลูปเดินไปจนกว่าจะหมดขบวน (จนกว่า curr จะเป็น None)
            while curr:
                # ถ้ายังมีโหนดถัดไป ให้พิมพ์ข้อมูลแล้วตามด้วยลูกศร
                if curr.next:
                    print(curr.data, end=" -> ")
                # ถ้าถึงโหนดสุดท้ายแล้ว ให้พิมพ์แค่ข้อมูลไม่ต้องมีลูกศร
                else:
                    print(curr.data)
                # สั่งให้ตัวเดินขยับไปที่โหนดถัดไป
                curr = curr.next

def main():
    # สร้างลิสต์ว่างขึ้นมาหนึ่งอัน
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    # สั่งให้แสดงผลข้อมูลทั้งหมดในลิสต์ออกมา
    mylist.traverse()

main()
