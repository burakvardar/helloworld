const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Merhaba Dünyaaaa\n');
});

const PORT = process.env.PORT || 8080;

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});

