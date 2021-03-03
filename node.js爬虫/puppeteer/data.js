const puppeteer = require('puppeteer');
const http = require('http');
const https = require('https');
const fs = require('fs');
// const { screenshot } = require('./src/config/defulat');
// 设置延时函数， 确保网页图片加载完毕
const sleep = time => new Promise(resolve => {
  setTimeout(resolve, time);
});
(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    // headless:true,
    headless:false,
    defaultViewport: null, args: ['--start-maximized'],
    ignoreDefaultArgs: ['--enable-automation']
  });
  const page = await browser.newPage();
  await page.goto('http://image.baidu.com/',{waitUntil:"networkidle2"});
  console.log('goto http://image.baidu.com/');
  await page.setViewport({
    width: 1920,
    height: 1080
  });
  console.log('reset viewport');
  await page.focus('#kw');
  await page.keyboard.sendCharacter('浙江');
  await page.click('.s_newBtn');
  console.log('go to search list');
  page.on('load',async () => {
  console.log('page loading done');
  await sleep(1000);
  // 控制滚动条，动态加载图片 Q:暂时没办法指定数量
  for(let i = 0; i < 20 ; i++) {
    const img_num = await page.$$eval('img[data-imgurl]',el => el.length);
    // 获得到的img地址大于300时 停止获取
    if (img_num > 300) break; 
    await page.evaluate(() => {
      window.scrollTo(50,document.body.scrollHeight);
    });
    await sleep(1000);
    }
  await sleep(5000);
  const src = await page.$$eval('img[data-imgurl]',
  el => {
    const arr = [];
    for (let i = 0;i < el.length; i++){
      arr.push(el[i].dataset.imgurl)
    }
    return arr;
  });
  let urls = src;
  downloads(urls);
  console.log('download over');
  browser.close()
});
})();

function downloads(urls){
  var pathname = "img";
  console.log("共需要下载"+urls.length+"张");
  for(let i = 0; i<urls.length; i++){
    let url = urls[i];
    // console.log(url);
    download(url,i,pathname);
  }
}
function download(url,i,pathname){
  https.get(url,(res) => {
    var imgdata = '';
    res.setEncoding("binary");
    res.on("data",function(chunk){
      imgdata = imgdata + chunk;
    });
    res.on('end',()=>{
      fs.writeFileSync(`./img/${pathname}${i}.jpg`,imgdata,'binary');
    })
  })
}
