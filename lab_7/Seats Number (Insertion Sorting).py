def insertionSort(data, last):
    comparison_times = 0
    current = 1
    while current <= last:
        hold = data[current]
        walker = current - 1
        
        # ลูปเพื่อหาตำแหน่งแทรก
        while walker >= 0:
            comparison_times += 1  # นับจำนวนครั้งที่เปรียบเทียบ
            
            # เปรียบเทียบค่า String ตามลำดับตัวอักษรและรหัส ASCII
            if hold < data[walker]:
                # ถ้าตัวที่ถืออยู่ น้อยกว่าตัวหน้า ให้ขยับตัวหน้าไปทางขวา
                data[walker + 1] = data[walker]
                walker -= 1
            else:
                # ถ้าไม่น้อยกว่า แสดงว่าเจอตำแหน่งที่ถูกต้องแล้ว ให้หยุด
                break
        
        # วางข้อมูลลงในตำแหน่งที่ถูกต้อง
        data[walker + 1] = hold
        # แสดงผลลัพธ์ของลิสต์ในรอบนั้น
        print(data)
        current += 1
    print(f"Comparison times: {comparison_times}")

def main():
    line = input() 
    # ลบวงเล็บ [ ] ออก และตัดคำด้วยลูกน้ำ
    clean_line = line.replace('[', '').replace(']', '')
    # ตรวจสอบว่ามีข้อมูลหรือไม่ ป้องกัน Error กรณีลิสต์ว่าง
    data_list = []
    if clean_line.strip() == "":
        # แยกข้อมูลด้วยลูกน้ำ (,)
        for item in clean_line.split(','):
            item = item.strip() # ลบช่องว่างหัวท้าย
            # เช็คว่าเป็น String หรือ Number ถ้ามีเครื่องหมายคำพูด ' หรือ " ถือเป็น String
            if item.startswith("'") or item.startswith('"'):
                data_list.append(item.replace("'", "").replace('"', ''))
            else:
                # ถ้าไม่มีเครื่องหมายคำพูด ให้แปลงเป็น int
                data_list.append(int(item))
    last_index = int(input())   
    insertionSort(data_list, last_index)

main()