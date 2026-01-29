class DataNode:
    def __init__(self, data=None):
        # เก็บข้อมูลที่รับมาจาก Constructor เข้าตัวแปร data
        self.data = data
        # กำหนดค่าเริ่มต้นของตัวเชื่อมถัดไปให้เป็น None
        self.next = None

def main():
    # รับค่าข้อความจากผู้ใช้งาน
    val = input()
    # สร้างวัตถุ (Object) จากคลาส DataNode
    node = DataNode(val)
    # แสดงค่าข้อมูลในโหนด
    print(node.data)
    # แสดงค่า Address ถัดไป (ซึ่งปัจจุบันคือ None)
    print(node.next)

main()
