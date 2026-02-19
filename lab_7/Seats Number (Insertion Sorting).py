def insertionSort(data, last):
    comparison_times = 0
    current = 1
    while current <= last:
        # เก็บค่าปัจจุบันไว้ในตัวแปร hold ที่จะนำไปแทรก
        hold = data[current]
        walker = current - 1
        # แยกตัวอักษรและตัวเลขของตัวที่ถืออยู่ (hold) "R94" จะถูกแปลงเป็น ('R', 94)
        hold_val = (hold[0], int(hold[1:]))
        while walker >= 0:
            comparison_times += 1  # นับจำนวนครั้งที่เปรียบเทียบ
            # แยกตัวอักษรและตัวเลขของตัวหน้า
            walker_val = (data[walker][0], int(data[walker][1:]))
            # เปรียบเทียบค่า Tuple (ตัวอักษรจะถูกเทียบก่อน ถ้าเท่ากันถึงจะเทียบตัวเลข)
            if hold_val < walker_val:
                # ถ้าตัวที่ถืออยู่ (hold) น้อยกว่าตัวหน้า (walker) ให้ขยับตัวหน้าไปทางขวา 1 ช่อง
                data[walker + 1] = data[walker]
                walker -= 1 # ถอย walker ไปเช็คตัวถัดไปทางซ้าย
            else:
                break     
        # วางข้อมูลที่ถืออยู่ลงในตำแหน่งที่ถูกต้อง
        data[walker + 1] = hold
        # แสดงผลลัพธ์ของลิสต์ในรอบนั้น
        print(data)
        current += 1 # ขยับไปพิจารณาตัวถัดไป
    # แสดงจำนวนการเปรียบเทียบทั้งหมดเมื่อทำงานเสร็จ
    print(f"Comparison times: {comparison_times}")

def main():
    line = input().strip() 
    # ตัดวงเล็บ [ ] หน้าสุดและหลังสุดออก
    if line.startswith('['): line = line[1:]
    if line.endswith(']'): line = line[:-1]
    # ตรวจสอบว่ามีข้อมูลหรือไม่ ป้องกัน Error กรณีลิสต์ว่าง
    data_list = []
    if line.strip() != "":
        # แยกข้อมูลด้วยลูกน้ำ (,)
        for item in line.split(','):
            item = item.strip() # ลบช่องว่างหัวท้าย
            # เช็คว่าเป็น String หรือ Number 
            if (item.startswith("'") and item.endswith("'")) or \
               (item.startswith('"') and item.endswith('"')):
                # ใช้ [1:-1] ตัดแค่ตัวแรกสุดและหลังสุดออกเท่านั้น ข้อมูลข้างในจะปลอดภัย
                data_list.append(item[1:-1])
            else:
                # ถ้าไม่มีเครื่องหมายคำพูดครอบ ให้แปลงเป็น int
                data_list.append(int(item))
    last_index = int(input())   
    insertionSort(data_list, last_index)

main()
