from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first 11item</a></li>
'''
# html = etree.parse(text, etree.HTMLParser())
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item" ]/a/text()')
# result1 = html.xpath('//li[@class="item-0"]//text()')
print(result)
# print(result1)


# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))