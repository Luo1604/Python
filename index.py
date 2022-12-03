from pyodide.http import pyfetch
import asyncio
from bs4 import BeautifulSoup

async def get_testdata(path) :
    path = "https://www.andreasjakl.com/raycast-anchor-placing-ar-foundation-holograms-part-3/"
    res = await pyfetch(url=path, method="GET")
    obj = BeautifulSoup(await res.string(), 'html.parser')
    list_title = []
    for i in range(1, 7):
        h = obj.find_all('h' + str(i))
        if (h == []):
            break
        list_title.append(h) 
    content = ""
    for item in list_title:
        for i in item:
            title_text = i.get_text()
            content += title_text
    list_text = obj.find_all('p')
    for item in list_text:
        text = item.get_text()
        if (len(text) > 50):
            content += text
    return content
