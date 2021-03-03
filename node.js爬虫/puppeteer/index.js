const puppeteer = require('puppeteer');
const path = require('path');
const os = require('os');
const fs = require('fs');
(async() => {
    // 常量定义 
    imgpath = 'img/';
    srcpath = 'src/';
    // 自定义延时函数
    const sleep = time => new Promise(reslove => {
        setTimeout(reslove, time);
      });
    // 文本中获得URL
    function readtxt(pathname){
	    fs.readFile(pathname, (err,data) => {
	    if (err){
		    console.log(err);
	    }
	    else {
		   const a = data.toString();
			let urls = a.split("\r\n");
		    console.log(urls);
		    module.exports.urls = urls;
		    return urls;
	    }
	    })
    }

	function pathexist(pathname){
			fs.exists(pathname,function(exists){
					if(exists){}
					if(!exists){
							fs.mkdirSync(pathname);
					}
			});
	}

    readtxt('url.txt');
	pathexist(imgpath);
	pathexist(srcpath);
    const getOSType = () => {
    var platform = os.platform();
    console.log('当前系统为:'+platform);
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
        // headless:true,
        headless:false,
        defaultViewport: null, args: ['--start-maximized'],
        ignoreDefaultArgs: ['--enable-automation']
    });
    const page = await browser.newPage();
    await page.setViewport ({
	    width: 1920,
	    height: 1080
    });
    for(let n = 0; n < this.urls.length-1; n++)
    {
      console.log(`共${this.urls.length-1}个网址待检测，现在在检测第${n+1}个网址，网址为${this.urls[n]}`);
      await page.goto(this.urls[n], {waitUntil:"networkidle2"});
      // 获得当前页面源码
	  const html = await page.content();
      await page.screenshot({path:`${imgpath}img${n+1}_1.png`});
      console.log('Screenshot over');
      fs.writeFile(`${srcpath}src${n+1}_1.html`, html, () => console.log('HTML saved'));
      await sleep(15000)
      await page.screenshot({path:`${imgpath}img${n+1}_2.png`});
      console.log('Screenshot1 over');
      const html1 = await page.content();
      fs.writeFile(`${srcpath}src${n+1}_2.html`, html1 ,() => {console.log(`HTML saved`);});
      await sleep(5000);
    }
    browser.close();
})();
