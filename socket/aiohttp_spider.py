# asyncio爬虫、去重、入库
import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

stopping = False
start_url = "http://www.jobbole.com/"
waitting_urls = ["http://www.baidu.com"]
seen_urls = set()

# 并发3
sem = asyncio.Semaphore(3)


# 定义一个协程
async def fetch(url, session):
    async with sem:
        await asyncio.sleep(1)
        async with session.get(url) as resp:
            try:
                print("url status: {}".format(resp.status))
                if resp.status in [200, 201]:
                    data = await resp.text()
                    return data
            except Exception as e:
                print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    print("urls:", urls)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):
    # 获取文章详情并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    print("title: ", title)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = "insert into article_test(title) values('{}')".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print("start get url: {}".format(url))
            # if re.match('http://.*?jobbole.com/\d+/', url):
            if re.match('http://.*?baidu.com', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
                    await asyncio.sleep(0.5)
            # else:
                # if url not in seen_urls:
                #     asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    # 等待mysql连接建立好
    # 如果不设置charset，插入关于中文字符的时候，不会报错，但是数据库里就是没有东西
    # autocommit不设置为True，也不会报错，但是数据库里也没有东西，这两点是个坑
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='panxiong',
                                      db='aiomysql_test', loop=loop, charset="utf8", autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        print(html)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()


# 整体的逻辑
# 1.通过main中start_url解析出很多的url
# 2.consumer不停向waitting_urls中取数据，然后向asyncio中扔协程

