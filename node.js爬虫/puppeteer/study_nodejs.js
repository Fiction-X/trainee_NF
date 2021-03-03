const fs = require('fs');
const puppeteer = require('puppeteer');
// 设置延时函数， 确保网页图片加载完毕
const sleep = time => new Promise(reslove => {
  setTimeout(reslove, time);
});
// const readtxt = pathname => new Promise(abc => {
//   fs.readFile(pathname, (err, data) => {
//     if (err){
//       console.log(err);
//       return("读取文件出错"+"err:"+err);
//     }
//     else{
//       const a = data.toString()
//       // 将文件中的url按行存入数组
//       urls = a.split("\r\n");
//       console.log(urls);
//     }
//   });
// });
function readtxt(pathname){

  fs.readFile(pathname, (err, data) => {
    if (err){
      console.log(err);
      return("读取文件出错"+"err:"+err);
    }
    else{
      const a = data.toString();
      // 将文件中的url按行存入数组
      let urls = a.split("\r\n");
      console.log(urls);
      module.exports.urls = urls;
      return urls;
    }
  });
}
(async () => {
  imgpath = 'img/';
  srcpath = 'src/';
  const browser = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    // headless:true,
    headless:false,
    defaultViewport: null, args: ['--start-maximized'],
    ignoreDefaultArgs: ['--enable-automation']
  });
  readtxt('input.txt');
  const page = await browser.newPage();
  await page.setViewport({
    width: 1920,
    height: 1080
  });
  
  for(let n = 0; n <this.urls.length; n++)
  {
    console.log(`共${this.urls.length}个网址待检测，现在在检测第${n+1}个网址，网址为${this.urls[n]}`);
    // try{
      await page.goto(this.urls[n], {waitUntil:"networkidle2"});
      const html = await page.content();
      await page.waitForSelector('title');

      await page.screenshot({path:`${imgpath}scr${n}_0.png`});
      console.log('Screenshot over');
      fs.writeFile(`${srcpath}page${n}_0.html`, html, () => console.log('HTML saved'));
      // await sleep(10000);
      // page.once('load', async() => {
      //   console.log('√ Page is loaded');
      await sleep(15000)
      await page.screenshot({path:`${imgpath}scr${n}_1.png`});  
      console.log('Screenshot1 over');
      const html1 = await page.content();
      fs.writeFile(`${srcpath}page${n}_1.html`, html1 ,() => {console.log(`HTML saved`);});  
      await sleep(5000);
      // });
    // }
    // catch(err){
      // console.log("error:" + err);
    // }  
  }
  browser.close();
  console.log('browser has been closed');

})();