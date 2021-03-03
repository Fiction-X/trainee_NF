import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 要请求的网络地址
url = 'https://www.naotan020.com/'
arr_url = []
# 请求网络地址得到html网页代码
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url=url)
time.sleep(15)
# 找出所有的 a 标签， 因为所有的链接都在 a 标签内
urls = driver.find_elements_by_xpath("//a")
for url in urls:
    arr_url.append(str(url.get_attribute("href")))
    print(url.text, url.get_attribute("href"))

# 打开文件对象做持久化操作
file = open(r'E:\xiangrisheng\xrs\py\外链审阅\sensitive_url.txt', 'a+', encoding='utf-8')

# 遍历所有的 a 标签， 获取它们的 href 属性的值和它们的 text
for item in arr_url:
    if str(item) not in ['javascript', 'selenium.webdriver', '']:
        if 'http' not in item:
            file.write(str.__add__(str(url)+str(item), '\n'))
        else:
            print(item)
        # file.write(str.__add__(itemg, ' '))
            file.write(str.__add__(item, '\n'))

file.close()
