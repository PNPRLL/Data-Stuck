class DataNode:
    def __init__(self, data=None):
        self.data = data
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

    def insert_before(self, node, data):
        # ถ้าลิสต์ว่างเปล่า จะไม่มีโหนดให้แทรกข้างหน้าได้เลย
        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return

        # ถ้าโหนดเป้าหมายคือหัวขบวน ให้ใช้การแทรกข้างหน้า
        if self.head.data == node:
            self.insert_front(data)
            return

        # เริ่มเดินหาโหนดเป้าหมาย
        curr = self.head
        while curr.next:
            # ถ้าโหนดถัดไปคือตัวที่เราตามหา
            if curr.next.data == node:
                p_new = DataNode(data)
                # ให้โหนดใหม่จับมือกับโหนดเป้าหมาย
                p_new.next = curr.next
                # ให้โหนดปัจจุบันเปลี่ยนมาจับมือกับโหนดใหม่
                curr.next = p_new
                self.count += 1
                return
            curr = curr.next

        # ถ้าเดินจนจบขบวนแล้วยังไม่เจอเป้าหมาย
        print("Cannot insert, " + node + " does not exist.")

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    else:
        print("Invalid Condition!")
  mylist.traverse()

main()
