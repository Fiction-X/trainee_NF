import chardet
from bs4 import BeautifulSoup


filename = '新建文本文档.html'
if filename.endswith('html'):
    with open(filename, 'rb') as f:
        html = f.read()

        result = chardet.detect(html)
        encoding = result.get('encoding') if result.get(
            'confidence') > 0.8 else 'utf-8'
        html = html.decode(encoding, 'strict')
        bs = BeautifulSoup(html, features="lxml")
        text = bs.get_text(strip=True)
        print(text)
        if text == '':
            print(filename+"过滤后为空文本")
        else:
            with open((filename + '.txt'), 'w', encoding='utf-8') as f:
                f.write(text)
