def insertionSort(data, last):
    count = 0
    current = 1
    
    while current <= last:
        hold = data[current]
        walker = current - 1
        
        # แปลงค่า hold ให้เป็นคู่ (ตัวอักษร, ตัวเลข) เพื่อให้เทียบง่ายๆ เช่น "K19" -> ('K', 19)
        hold_val = (hold[0], int(hold[1:]))
        
        while walker >= 0:
            count += 1
            # แปลงค่าตัวที่ walker ชี้อยู่ ให้เป็นคู่เหมือนกัน
            walker_val = (data[walker][0], int(data[walker][1:]))
            # เทียบกันตรงๆ ได้เลย Python จะเทียบตัวอักษรก่อน แล้วค่อยเทียบเลข
            if hold_val < walker_val:
                data[walker + 1] = data[walker]
                walker -= 1
            else:
                break
        
        data[walker + 1] = hold
        print(data)
        current += 1
        
    print(f"Comparison times: {count}")

data_list = eval(input())  # รับ List เข้ามาเลยรองรับทั้ง ' และ "
last_index = int(input())
insertionSort(data_list, last_index)