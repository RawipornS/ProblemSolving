# Node class
class Node:
    def __init__(self, data):
        self.data = data  # เก็บข้อมูลใน Node
        self.next = None  # ตัวชี้ไปยัง Node ถัดไป (เริ่มต้นเป็น None)

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # หัวของ Linked List (เริ่มต้นเป็น None)

    # เพิ่ม Node ใหม่ที่จุดเริ่มต้นของ Linked List
    def push(self, data):
        new_node = Node(data)  # สร้าง Node ใหม่
        new_node.next = self.head  # ชี้ Node ใหม่ไปยังหัวปัจจุบัน
        self.head = new_node  # ตั้ง Node ใหม่เป็นหัวของลิสต์

    # ลบ Node ที่มีค่าเท่ากับ key
    def deleteNode(self, key):
       # กรณีที่หัวเป็น Node ที่ต้องการลบ
        if self.head and self.head.data == key:
            self.head = self.head.next  # เปลี่ยนหัวไปยัง Node ถัดไป
            return

        # วนลูปเพื่อค้นหา Node ที่ต้องการลบ
        current = self.head  # เริ่มจากหัว
        while current.next:  # วนจนกว่าจะถึง Node สุดท้าย
            if current.next.data == key:  # ถ้าพบ Node ที่ต้องการลบ
                current.next = current.next.next  # ข้าม Node ที่ต้องการลบ
                return
            current = current.next  # เลื่อนไปยัง Node ถัดไป

    # กลับลำดับของ Linked List
    def reverse(self):
        prev, current = None, self.head  # ตั้ง prev เป็น None และ current เป็นหัว
        while current:  # วนลูปจนถึง Node สุดท้าย
            next_node = current.next  # เก็บ Node ถัดไป
            current.next = prev  # สลับการชี้ของ Node ปัจจุบันไปยัง Node ก่อนหน้า
            prev = current  # เลื่อน prev ไปยัง Node ปัจจุบัน
            current = next_node  # เลื่อน current ไปยัง Node ถัดไป
        self.head = prev  # ตั้งหัวใหม่เป็น Node สุดท้าย

    # แสดงข้อมูลใน Linked List
    def printList(self):
        current = self.head  # เริ่มต้นที่หัว
        while current:  # วนจนกว่าจะถึง Node สุดท้าย
            print(current.data, end=" -> ")  # พิมพ์ค่าของ Node
            current = current.next  # เลื่อนไปยัง Node ถัดไป
        print("None")  # สิ้นสุดลิสต์

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    llist = LinkedList()

    # เพิ่มข้อมูลลงใน Linked List
    for data in [7, 1, 3, 2]:
        llist.push(data)  # เพิ่ม Node ทีละตัวจากลำดับ [7, 1, 3, 2]

    print("Created Linked List:")
    llist.printList()  # แสดง Linked List

    llist.deleteNode(1)  # ลบ Node ที่มีค่า 1
    print("Linked List after Deletion of 1:")
    llist.printList()

    llist.reverse()  # กลับลำดับ Linked List
    print("Reversed Linked List:")
    llist.printList()
