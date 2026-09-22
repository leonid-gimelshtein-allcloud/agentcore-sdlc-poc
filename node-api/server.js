const express = require('express');

const app = express();
const PORT = 3001;

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.get('/hello/:name', (req, res) => {
  res.json({ message: `Hello, ${req.params.name}!` });
});

app.listen(PORT, () => {
  console.log(`node-api listening on http://localhost:${PORT}`);
});
