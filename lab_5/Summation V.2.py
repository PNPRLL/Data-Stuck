def summation(n):
    # สูตรปกติ: (n * (n + 1)) / 2
    # แปลงสูตรหลบคำห้ามใช้: (n^2 + n) >> 1
    
    # หาค่า n ยกกำลัง 2 แล้วบวก n
    top_value = pow(n, 2) + n
    
    # หาร 2 ด้วยการเลื่อนบิต (Shift Right)
    result = top_value >> 1
    
    return result

def main():
    n = int(input())
    print(summation(n))

main()
