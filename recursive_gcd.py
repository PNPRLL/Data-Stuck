"""GCD"""
def gcd(a, b):
    """Start"""
    # Base Case: ถ้าตัวหาร (b) เป็น 0 คำตอบคือ a
    if b == 0:
        return a
    # Recursive Case: เรียกฟังก์ชันตัวเอง โดยสลับเอา b มาเป็นตัวตั้ง และเอาเศษ (a % b) เป็นตัวหาร
    return gcd(b, a % b)

num1 = int(input())
num2 = int(input())
print(gcd(num1, num2))
