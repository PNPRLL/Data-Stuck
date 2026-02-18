def bubbleSort(data, last):
    current = 0
    comparison_times = 0
    sorted_flag = False  # set sorted to false
    # วนลูปตราบใดที่ยังไม่ถึงตัวสุดท้าย และยังมีการสลับข้อมูลเกิดขึ้นในรอบที่แล้ว
    while current <= last and sorted_flag is False:
        walker = last
        # สมมติว่ารอบนี้เรียงเสร็จแล้วไว้ก่อน
        sorted_flag = True
        # วนลูปจากท้ายสุด ขึ้นมาจนถึงตำแหน่ง current
        while walker > current:
            # นับจำนวนการเปรียบเทียบ
            comparison_times += 1
            # เปรียบเทียบตัวขวา กับตัวซ้าย
            if data[walker] < data[walker - 1]:
                # มีการสลับ แสดงว่ายังไม่เรียงเสร็จ
                sorted_flag = False
                # exchange (walker, walker-1)
                data[walker], data[walker - 1] = data[walker - 1], data[walker]
            # ขยับ walker ไปตำแหน่งถัดไป
            walker -= 1

        # แสดงผลลัพธ์ของลิสต์ในแต่ละรอบ
        print(data)
        current += 1
    # แสดงจำนวนการเปรียบเทียบทั้งหมด
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
    bubbleSort(data_list, last_index)

main()
