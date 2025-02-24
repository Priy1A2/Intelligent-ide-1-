import http from http
import express from express
import { Server : SocketServer } from "socket.io"

const app = express()
const server = http.createServer(app);
const io = new SocketServer({
    cors = '*'
})

io.attach(server);

io.on('connection', (socket) => {
    console.log(`Scoket connected`, socket.id)
})

server.listen(9000, ()=>{
    console.log(`Docker server is running on port 9000`);
})
