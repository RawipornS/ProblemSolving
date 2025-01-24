class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # ความจุสูงสุดของคิว
        self.front = 0  # ตำแหน่งเริ่มต้นของคิว
        self.rear = capacity - 1  # ตำแหน่งสุดท้ายของคิว
        self.size = 0  # ขนาดปัจจุบันของคิว
        self.Q = [None] * capacity  # สร้างคิวเปล่าที่มีขนาดตามความจุ

    # ตรวจสอบว่าคิวเต็มหรือไม่
    def isFull(self):
        return self.size == self.capacity

    # ตรวจสอบว่าคิวว่างหรือไม่
    def isEmpty(self):
        return self.size == 0

    # เพิ่มข้อมูลลงในคิว
    def EnQueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity  # คำนวณตำแหน่งใหม่
        self.Q[self.rear] = item  # เพิ่มข้อมูล
        self.size += 1  # เพิ่มขนาด
        print(f"{item} enqueued to queue")

    # ลบข้อมูลจากคิว
    def DeQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print(f"{self.Q[self.front]} dequeued from queue")
        self.front = (self.front + 1) % self.capacity  # คำนวณตำแหน่งเริ่มต้นใหม่
        self.size -= 1  # ลดขนาดคิว

    # แสดงข้อมูลในคิว
    def print_queue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue elements are:", end=" ")
        index = self.front
        for i in range(self.size):
            print(self.Q[index], end=" ")
            index = (index + 1) % self.capacity
        print()

    # แสดงข้อมูลด้านหน้าสุดของคิว
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Front item is", self.Q[self.front])

    # แสดงข้อมูลท้ายสุดของคิว
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Rear item is", self.Q[self.rear])


# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    queue = Queue(5)  # สร้างคิวที่มีขนาดความจุ 5

    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)

    print("\nOriginal queue:")
    queue.print_queue()

    queue.DeQueue()
    print("\nQueue after dequeue:")
    queue.print_queue()

    queue.que_front()  # แสดงข้อมูลด้านหน้าสุด
    queue.que_rear()  # แสดงข้อมูลด้านท้ายสุด
