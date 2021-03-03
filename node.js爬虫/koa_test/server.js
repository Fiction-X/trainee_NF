const express = require('express');
const app = express();
const btc = require('./test');
const EventEmitter =  require('events');
EventEmitter.prototype._maxListeners = 100;
(async () => {
app.get('/',async function (req, res) {
  var url = req.query.url;
  var htmlcont = await btc.abcd('http://' + url);
  // console.log(htmlcont['img']);
  res.send(htmlcont);
  // res.send(htmlcont['img']);

});

var server = app.listen(8081, function () {

  var host = server.address().address;
  var port = server.address().port;
  console.log("应用实例，访问地址为 http://%s:%s", host, port);

});
})();