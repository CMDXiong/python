# python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程


# async def downloader(url):
#     return "panxiong"

import types
@types.coroutine
def downloader(url):
    yield "panxiong"

async def download_url(url):
    # dosomethings
    # 委托给子协程完成
    html = await downloader(url)

    return html

if __name__ == "__main__":
    coro = download_url("www.baidu.com")
    coro.send(None)

    