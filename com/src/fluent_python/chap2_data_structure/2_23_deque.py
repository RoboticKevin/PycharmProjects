# 双向队列
from collections import deque
from queue import Queue, LifoQueue, PriorityQueue
from multiprocessing import Queue, JoinableQueue
from asyncio import Queue, LifoQueue, PriorityQueue

if __name__ == '__main__':
    dq = deque(range(5), maxlen=5)
    print(dq)  # 0 1 2 3 4

    dq.rotate(2)  # 右侧n个数旋转到开头, 3 4 0 1 2
    print(dq)
    dq.rotate(-3)  # 1 2 3 4 0
    print(dq)

    dq.appendleft(5)  # 满员时，会挤下多余的元素 5 1 2 3 4
    print(dq)

    dq.append(0)  # 1 2 3 4 0
    print(dq)

    dq.extend([5, 6, 7])  # 4 0 5 6 7
    print(dq)
