var express = require('express');
var path = require('path');

const app = express();

app.use(express.static(__dirname + '/static'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/vignere', (req, res) => {
    res.send('Vignere :)');
});

app.get('/vignere-full', (req, res) => {
    res.send('Full Vignere :)');
});

app.get('/vignere-rk', (req, res) => {
    res.send('Running Key Vignere :)');
});

app.get('/vignere-ext', (req, res) => {
    res.send('Extended Vignere :)');
});

app.get('/playfair', (req, res) => {
    res.send('Playfair :)');
});

app.get('/vignere', (req, res) => {
    res.send('Vignere :)');
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log('Server start');
});