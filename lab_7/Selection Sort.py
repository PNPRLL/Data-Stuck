def selectionSort(data, last):
    # กำหนดค่าเริ่มต้นให้กับ current เป็น 0
    current = 0
    comparison_times = 0
    
    # วนลูปจนกว่าข้อมูลจะเรียงเสร็จ
    while current < last:
        # สมมติให้ตำแหน่ง current เป็นตำแหน่งที่มีค่าน้อยที่สุดไว้ก่อน
        smallest = current
        # กำหนดให้ walker เริ่มต้นที่ตำแหน่งถัดจาก current
        walker = current + 1
        while walker <= last:
            # นับจำนวนครั้งที่ทำการเปรียบเทียบข้อมูล
            comparison_times += 1
            # ตรวจสอบว่าค่าที่ walker ชี้อยู่ น้อยกว่า ค่าที่ smallest ชี้อยู่หรือไม่
            if data[walker] < data[smallest]:
                # ถ้าใช่ ให้เปลี่ยนตำแหน่ง smallest เป็นตำแหน่งของ walker แทน
                smallest = walker
            # ขยับ walker ไปตำแหน่งถัดไป
            walker += 1
            
        # สลับค่าข้อมูล (Exchange) ระหว่างตำแหน่ง current และ smallest
        data[current], data[smallest] = data[smallest], data[current]
        print(data)
        current += 1

    # แสดงจำนวนครั้งการเปรียบเทียบทั้งหมดเมื่อจบการทำงาน
    print(f"Comparison times: {comparison_times}")

def main():
    line = input()
    # ลบวงเล็บ [ ] ออก และตัดคำด้วยลูกน้ำ
    clean_line = line.replace('[', '').replace(']', '')
    
    # ตรวจสอบว่ามีข้อมูลหรือไม่ ป้องกัน Error กรณีลิสต์ว่าง
    if clean_line.strip() == "":
        data_list = []
    else:
        # แปลงข้อมูลแต่ละตัวให้เป็น int และเก็บลงใน List
        data_list = [int(x) for x in clean_line.split(',')]
    last_index = int(input())
    selectionSort(data_list, last_index)

main()