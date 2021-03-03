const puppeteer = require('puppeteer');
const path = require('path');
const os = require('os');
const fs = require('fs');

const EventEmitter =  require('events');
EventEmitter.prototype._maxListeners = 100;

exports.abcd = async function abcd(abc)  {
    async function html(page){
        // 当前页面源码
        const html = await page.content();
        return html;
    }

    async function img(page){
        var imgs = await page.screenshot();
        // console.log(imgs.toString('base64'));
        return imgs;
    }
    // 常量定义
    // 自定义延时函数
    const sleep = time => new Promise(reslove => {
        setTimeout(reslove, time);
      });

    const getOSType = () => {
    var platform = os.platform();
    console.log('当前系统为:' + platform);
   return platform;
    }
    const getpath = () => {
    const chrome_path = {
		linux:'/usr/bin/google-chrome-stable',
        Mac: '',
        win32: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    }[getOSType()];
    return path.join(chrome_path);
    }
    const browser = await puppeteer.launch({
        executablePath: getpath(),
        args: ["--no-sandbox" , "--disable-setuid-sandbox"],
        ignoreDefaultArgs: ['--enable-automation'],
        ignoreHTTPSErrors: true,
        headless:true,
        //headless:false,
    });
    const page = await browser.newPage();
    await page.setViewport({
        width: 1920,
        height: 1080
    });	
    await page.goto(abc, {waitUntil:"networkidle2"});
    await sleep(5000)
    content = await html(page);
    fs.writeFile('src.html', content ,() => {console.log(`HTML saved`);});
    imgs = await img(page);
    var htmlcode = {
        "img"  : imgs.toString('base64'),
        "content" : content
    };
    await browser.close();
    // console.log(htmlcode)
    return htmlcode;

}

exports.abcd('http://www.cpijl.com');


