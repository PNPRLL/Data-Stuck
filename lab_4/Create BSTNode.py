class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

def main():
    # รับค่าจำนวนเต็มจาก Input
    input_data = int(input())
    
    # สร้าง Object จากคลาส BSTNode
    p_new = BSTNode(input_data)
    
    # แสดงผลตาม Output Specification
    print(p_new.data)
    print(p_new.left)
    print(p_new.right)

main()
