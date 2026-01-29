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

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
