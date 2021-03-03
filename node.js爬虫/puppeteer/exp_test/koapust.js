const Koa = require('koa')
const bodyParser = require('koa-bodyparser')
const puppteer = require('./btc');
const app = new Koa()

app.use(bodyParser())

app.use( async (ctx) => {
    ctx.body =  ctx.request.body
})

app.listen(3002, () => {
    console.log('start ok')
})