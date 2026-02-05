def get_input():
    # 1. รับค่าและลบวงเล็บ [ ] ทิ้งไปเลย ง่ายกว่าการตัดคำ
    text = input().replace('[', '').replace(']', '')
    
    # 2. เช็คว่าถ้าข้อความว่างเปล่า (กรณี []) ให้ส่งเซตว่างกลับไป
    if not text:
        return set()
        
    # 3. หั่นด้วยลูกน้ำ (,) แล้วแปลงเป็น int ลง set ทันที
    return {int(x) for x in text.split(',')}

def isIntersect(a, b, c):
    # ใช้ & หาตัวซ้ำเหมือนเดิม (เร็วที่สุดแล้ว)
    return bool(a & b & c)

def main():
    a = get_input()
    b = get_input()
    c = get_input()
    print(isIntersect(a, b, c))

main()
