const http = require('http');

function start(){
    function onrequest(request, response){
        console.log("Request received.");
        response.writeHead(200, {"Content-Type":"text/plain"});
        response.write("Hello world");
        response.end();
    }
    http.createServer(onrequest).listen(8800);
    console.log('Server has started');
}

exports.start = start;