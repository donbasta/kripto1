var express = require('express');
var path = require('path');

const app = express();

// static config
app.use(express.static(__dirname + '/static'));

// EJS dependencies
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

// Routes for each cipher
app.get('/', (req, res) => {
    res.render('index.html', {message:'Hello!'});
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

app.get('/affine', (req, res) => {
    res.send('Affine :)');
});

app.get('/hill', (req, res) => {
    res.send('Hill :)');
});

app.get('/enigma', (req, res) => {
    res.send('Enigma :)');
});


// Listening on 8080
const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log('Server start');
});