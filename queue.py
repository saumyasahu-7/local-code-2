#testing simultaneous implementation
#with deque
from collections import deque
q = deque()
q.append('3')
q.append('b')
q.append('c')
print(q)
# deque(['a', 'b', 'c'])
print(q.popleft())
#'a'