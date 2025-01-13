class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def EnQueue(self, item):
        if self.isFull():
            print("ไม่สามารถเพิ่มผู้ใช้ได้ เนื่องจากคิวเต็ม")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size += 1
        print(f"{item} เข้าคิวแล้ว")

    def DeQueue(self):
        if self.isEmpty():
            print("คิวว่าง ไม่มีผู้ใช้บริการ")
            return
        print(f"{self.Q[self.front]} ออกจากคิว")
        self.front = (self.front + 1) % (self.capacity)
        self.size -= 1

    def queueFront(self):
        if self.isEmpty():
            print("คิวว่าง")
        else:
            print(f"ผู้ใช้บริการปัจจุบันคือ {self.Q[self.front]}")

# ตัวอย่างการทดสอบ
if __name__ == "__main__":
    queue = Queue(5)
    queue.EnQueue("ผู้ใช้ 1")
    queue.EnQueue("ผู้ใช้ 2")
    queue.EnQueue("ผู้ใช้ 3")
    queue.EnQueue("ผู้ใช้ 4")
    queue.queueFront()
    queue.DeQueue()
    queue.queueFront()
    if queue.isEmpty():
        print("คิวว่าง")
    else:
        print("คิวยังมีผู้ใช้")
