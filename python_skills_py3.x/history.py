# -*- encoding: utf-8 -*-
# 如何实现用户的历史记录功能(最多n条)?
# 解决方案
# 使用容量为n的队列存储历史记录

from collections import deque
q = deque([], 5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

# 使用pickle模块将历史记录存储到硬盘, 以便下次启动使用
import pickle
pickle.dump(q, open('save.pkl', 'wb'))
q2 = pickle.load(open('save.pkl', 'rb'))
print(q2)
