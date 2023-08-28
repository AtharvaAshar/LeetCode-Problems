class MyQueue:

    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]        

    def push(self, x: int):
        self.__stack1.append(x)

    def pop(self) -> int:
        for i in range(len(self.__stack1)-1):
            self.__stack2.append(self.__stack1.pop())
        val=self.__stack1.pop()
        for i in range(len(self.__stack2)):
            self.__stack1.append((self.__stack2.pop()))
        return val
    def peek(self) -> int:
        return self.__stack1[0]

    def empty(self) -> bool:
        return len(self.__stack1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()