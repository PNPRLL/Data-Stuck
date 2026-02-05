def isIntersect(a, b, c):
    memo = {}
    
    # 1. วนลูปเก็บข้อมูลจาก list a ลงใน dict
    # ให้ค่าเป็น 1 เพื่อระบุว่า "เจอใน a แล้วนะ"
    for x in a:
        memo[x] = 1
        
    # 2. วนลูป list b
    for x in b:
        # ถ้า x เคยเจอใน a (ค่าใน dict เป็น 1)
        # ให้อัปเดตค่าเป็น 2 เพื่อระบุว่า "เจอใน a และ b แล้วนะ"
        if x in memo:
            if memo[x] == 1:
                memo[x] = 2
                
    # 3. วนลูป list c
    for x in c:
        # ถ้า x มีค่าใน dict เป็น 2 แสดงว่าเจอมาแล้วทั้งใน a และ b
        # พอเจอใน c อีกตัว ก็ครบ 3 ลิสต์ -> คืนค่า True ทันที
        if x in memo:
            if memo[x] == 2:
                return True
                
    # ถ้าวนจนจบแล้วไม่เจอตัวซ้ำครบ 3 ลิสต์เลย
    return False

def main():
    # รับค่าและแปลง String เป็น List
    a = eval(input())
    b = eval(input())
    c = eval(input())
    
    print(isIntersect(a, b, c))

main()