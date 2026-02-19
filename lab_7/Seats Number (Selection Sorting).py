def selectionSort(data, last):
    current = 0
    comparison_times = 0
    
    while current < last:
        # สมมติให้ตำแหน่งปัจจุบันเป็นตำแหน่งที่มีค่าน้อยที่สุดไว้ก่อน
        smallest = current
        # ให้ walker เริ่มเดินจากตำแหน่งถัดจาก current
        walker = current + 1
        while walker <= last:
            comparison_times += 1
            # แปลงเป็น Tuple แยกข้อความออกเป็น 2 ส่วน คือ ตัวอักษร, ตัวเลข "B12" -> ('B', 12)
            walker_val = (data[walker][0], int(data[walker][1:]))
            smallest_val = (data[smallest][0], int(data[smallest][1:]))
            
            if walker_val < smallest_val:
                smallest = walker
            walker += 1
        # เมื่อจบวงรอบ walker ให้สลับที่ระหว่างตัวปัจจุบันกับตัวที่น้อยที่สุด
        data[current], data[smallest] = data[smallest], data[current]
        
        print(data)
        current += 1
    print(f"Comparison times: {comparison_times}")

def main():
    line = input()
    # ลบเครื่องหมายที่ไม่ต้องการออกให้หมด
    clean_line = line.replace('[', '').replace(']', '').replace('"', '').replace("'", "")
    # ตรวจสอบและแปลงเป็น List
    if clean_line.strip() == "":
        data_list = []
    else:
        # ตัดด้วยลูกน้ำ (,) และลบช่องว่างหัวท้ายทิ้ง
        data_list = [x.strip() for x in clean_line.split(',')]
    last_index = int(input())
    selectionSort(data_list, last_index)
main()