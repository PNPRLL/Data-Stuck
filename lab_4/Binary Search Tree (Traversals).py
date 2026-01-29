class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # สร้างโหนดใหม่เตรียมไว้
        p_new = BSTNode(data)
        
        # กรณีต้นไม้ยังว่างอยู่ ให้โหนดใหม่เป็นราก (Root)
        if self.root is None:
            self.root = p_new
        else:
            # กรณีมีข้อมูลอยู่แล้ว ให้ไล่หาตำแหน่งที่เหมาะสม
            curr = self.root
            while True:
                if data < curr.data:
                    # ถ้าน้อยกว่า ไปทางซ้าย
                    if curr.left is None:
                        curr.left = p_new
                        break
                    curr = curr.left
                else:
                    # ถ้ามากกว่าหรือเท่ากับ ไปทางขวา
                    if curr.right is None:
                        curr.right = p_new
                        break
                    curr = curr.right

    def is_empty(self):
        # คืนค่า True ถ้าไม่มีราก (ต้นไม้ว่าง)
        return self.root is None

    def preorder(self):
        # เรียกใช้ฟังก์ชันช่วยสำหรับการท่องแบบ Recursion
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is not None:
            # พิมพ์ข้อมูลตามรูปแบบ -> data
            print("->", node.data, end=" ")
            # ท่องไปทางซ้าย
            self._preorder_recursive(node.left)
            # ท่องไปทางขวา
            self._preorder_recursive(node.right)

    def preorder(self):
        # เริ่มท่องแบบ Preorder จากราก
        self._preorder(self.root)

    def _preorder(self, node):
        # กฎ: ราก -> ซ้าย -> ขวา
        if node is not None:
            print("->", node.data, end=" ") # 1. พิมพ์รากก่อน
            self._preorder(node.left)       # 2. ไปซ้ายให้สุด
            self._preorder(node.right)      # 3. ค่อยไปขวา

    def inorder(self):
        # เริ่มท่องแบบ Inorder จากราก
        self._inorder(self.root)
        
    def _inorder(self, node):
        # กฎ: ซ้าย -> ราก -> ขวา
        if node is not None:
            self._inorder(node.left)        # 1. ไปซ้ายให้สุดก่อน
            print("->", node.data, end=" ") # 2. พิมพ์ราก (ตรงกลาง)
            self._inorder(node.right)       # 3. ค่อยไปขวา

    def postorder(self):
        # เริ่มท่องแบบ Postorder จากราก
        self._postorder(self.root)

    def _postorder(self, node):
        # กฎ: ซ้าย -> ขวา -> ราก
        if node is not None:
            self._postorder(node.left)      # 1. ไปซ้ายให้สุด
            self._postorder(node.right)     # 2. ไปขวาให้สุด
            print("->", node.data, end=" ") # 3. ค่อยพิมพ์รากทีหลังสุด

    def traverse(self):
        # ฟังก์ชันรวมมิตร แสดงผลตามที่โจทย์สั่ง
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            print("Preorder: ", end="")
            self.preorder()
            print() # ขึ้นบรรทัดใหม่
            
            print("Inorder: ", end="")
            self.inorder()
            print() # ขึ้นบรรทัดใหม่
            
            print("Postorder: ", end="")
            self.postorder()
            print() # ขึ้นบรรทัดใหม่

def main():
    my_bst = BST()
    # รับจำนวนรอบ แล้ววนลูปรับค่า insert ทีละตัว
    for i in range(int(input())):
        my_bst.insert(int(input()))
    
    # สั่งแสดงผลทีเดียว
    my_bst.traverse()

main()
