const puppeteer = require('puppeteer');
const path = require('path');
var os = require('os');


(async() => {
    // 自定义延时函数
    const sleep = time => new Promise(reslove => {
        setTimeout(reslove, time);
      });
    const getOSType = () => {
    var platform = os.platform();
    console.log(platform);
    return platform;
    }
    const getpath = () => {
    const chrome_path = {
        Linux_x64: '',
        Mac: '',
        win32: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    }[getOSType()];
    return path.join(chrome_path);
    }
    const browser = await puppeteer.launch({
        executablePath: getpath(),
        // headless:true,
        headless:false,
        defaultViewport: null, args: ['--start-maximized'],
        ignoreDefaultArgs: ['--enable-automation']
    });
    const page = await browser.newPage();
    await page.goto('http://www.huobi.be/zh-cn/exchange/eth_usdt/');
    sleep(15000)
    while (true){
            sleep(500)
            const text = await page.$eval(`#chart > div > p:nth-child(7)`,el => el.textContent);
            console.log(text);
        }


})();