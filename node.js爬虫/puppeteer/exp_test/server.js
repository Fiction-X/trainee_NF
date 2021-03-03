const express = require('express');
const app = express();
const btc = require('./btc');
(async () => {

app.get('/',async function (req, res) {
  var url = req.query.url;
  var htmlcont = await btc.abcd('http://' + url);

  res.send(htmlcont);
  // res.send(htmlcont['img']);

});

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port
  console.log("应用实例，访问地址为 http://%s:%s", host, port)

});
})();