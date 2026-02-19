def insertionSort(data, last):
    comparison_times = 0
    current = 1
    while current <= last:
        # เก็บค่าปัจจุบันไว้ในตัวแปร hold ที่จะนำไปแทรก
        hold = data[current]
        # ให้ walker เริ่มเช็คจากตัวที่อยู่ก่อนหน้า current
        walker = current - 1
        while walker >= 0:
            comparison_times += 1  # นับจำนวนครั้งที่เปรียบเทียบ
            # เปรียบเทียบค่า String ตามลำดับตัวอักษรและรหัส ASCII (หรือเปรียบเทียบตัวเลข)
            if hold < data[walker]:
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
    line = input() 
    # ลบวงเล็บ [ ] ออก ให้เหลือแค่ข้อมูลข้างใน
    clean_line = line.replace('[', '').replace(']', '')
    # ตรวจสอบว่ามีข้อมูลหรือไม่ ป้องกัน Error กรณีลิสต์ว่าง
    data_list = []

    if clean_line.strip() != "":
        # แยกข้อมูลแต่ละตัวออกจากกันด้วยลูกน้ำ (,)
        for item in clean_line.split(','):
            item = item.strip() # ลบช่องว่างหัวและท้ายทิ้ง
            # ถ้ามีเครื่องหมายคำพูด ' หรือ " ถือเป็น String
            if item.startswith("'") or item.startswith('"'):
                # ลบเครื่องหมายคำพูดออกแล้วนำไปต่อท้ายใน List
                data_list.append(item.replace("'", "").replace('"', ''))
            else:
                # ถ้าไม่มีเครื่องหมายคำพูด ให้แปลงค่าเป็น int ก่อนเก็บลง List
                data_list.append(int(item))
    last_index = int(input())   
    insertionSort(data_list, last_index)

main()
