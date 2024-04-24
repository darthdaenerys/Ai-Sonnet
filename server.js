const express = require('express');
const app = express();
const path = require('path');
const port = 3000;
const { spawn } = require('child_process');
const http = require('http');
const socketIO = require('socket.io');
const server = http.createServer(app);
const io = socketIO(server);

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.status(200).sendFile(path.join(__dirname, 'index.html'));
});

app.post('/generate', (req, res) => {
    const { initialSeed, temperature, steps } = req.body;

    const pythonProcess = spawn('python', ['generator.py', initialSeed, temperature, steps]);


// io.on('connection', (socket) => {
//     console.log('User connected');
//     socket.on('disconnect', () => {
//         console.log('User disconnected');
//     })
// });

server.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});