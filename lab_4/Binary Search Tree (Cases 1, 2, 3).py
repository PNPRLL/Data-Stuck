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

    def find_min(self):
        # ถ้าต้นไม้ว่าง คืนค่า None ตามโจทย์
        if self.root is None:
            return None
        
        # เริ่มเดินจากราก
        curr = self.root
        # เดินไปทางซ้ายเรื่อยๆ จนกว่าจะสุดทาง (เพราะค่าที่น้อยที่สุดต้องอยู่ซ้ายสุดเสมอ)
        while curr.left is not None:
            curr = curr.left
        
        # คืนค่า data ของโหนดซ้ายสุด
        return curr.data

    def find_max(self):
        # ถ้าต้นไม้ว่าง คืนค่า None ตามโจทย์
        if self.root is None:
            return None
        
        # เริ่มเดินจากราก
        curr = self.root
        # เดินไปทางขวาเรื่อยๆ จนกว่าจะสุดทาง (เพราะค่าที่มากที่สุดต้องอยู่ขวาสุดเสมอ)
        while curr.right is not None:
            curr = curr.right
            
        # คืนค่า data ของโหนดขวาสุด
        return curr.data

    def delete(self, data):
        # รีเซ็ตค่าที่จะส่งคืน
        self.deleted_data = None
        # เรียกฟังก์ชันช่วยแบบ Recursive
        self.root = self._delete_node(self.root, data)
        return self.deleted_data

    def _delete_node(self, node, data):
        # Base Case: ถ้าเดินจนตกขอบแสดงว่าไม่เจอข้อมูล
        if node is None:
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
            return None

        # Recursive Search: หาตำแหน่งโหนดที่จะลบ
        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            # เจอข้อมูลแล้ว! (data == node.data)
            self.deleted_data = node.data # เก็บค่าไว้ส่งคืน

            # Case 1: ไม่มีลูก (Leaf Node) หรือ Case 2: มีลูกข้างเดียว
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: มีลูกสองข้าง (Two Subtrees)
            # หาค่ามากสุดของฝั่งซ้าย (Max of Left Subtree)
            temp = node.left
            while temp.right is not None:
                temp = temp.right
            max_val = temp.data

            # เอาค่านั้นมาแปะทับโหนดที่จะลบ
            node.data = max_val

            # ลบตัวต้นฉบับของค่าที่เอามาแปะทิ้ง (Recursive Delete)
            # หมายเหตุ: ต้องเก็บค่า deleted_data เดิมไว้ก่อน เพราะการเรียกซ้ำจะไปเขียนทับ
            saved_deleted = self.deleted_data
            node.left = self._delete_node(node.left, max_val)
            self.deleted_data = saved_deleted # คืนค่าที่ถูกต้องกลับมา

        return node

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
