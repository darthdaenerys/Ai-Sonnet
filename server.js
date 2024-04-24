const express = require('express');
const app = express();
const path = require('path');
const port = 3000;
const http = require('http');
const server = http.createServer(app);

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.status(200).sendFile(path.join(__dirname, 'index.html'));
});


server.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});