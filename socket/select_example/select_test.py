# encoding: utf-8
# 1.epoll并不代表一定比select好
# 在并发高的情况下，连接活跃不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好
# 连接活跃：建立一次连接后，不会不再管了，或者明确会断掉，如游戏就是连接活跃

# 通过非阻塞io实现http请求