const puppeteer = require('puppeteer');
const path = require('path');
const os = require('os');
const EventEmitter =  require('events');
const { time } = require('console');
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
    // 自定义延时函数
    const sleep = time => new Promise(reslove => {
        setTimeout(reslove, time);
      });
    const browser = await puppeteer.connect({ browserWSEndpoint: 'ws://10.65.70.150:3000?blockAds=true' });
    const page = await browser.newPage();
    await page.setViewport({
        width: 1920,
        height: 1080
    });	
    await page.goto(abc, {waitUntil:"networkidle2"});
    
    content = await html(page);
    imgs = await img(page);
    var htmlcode = {
        "img"  : imgs.toString('base64'),
        "content" : content
    };
    browser.disconnect();
    return htmlcode;
}

// exports.abcd('http://www.baidu.com');


