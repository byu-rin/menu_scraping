const path = require("path");
const express = require("express");
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

// search page
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'search.html'));
});

// input page
app.get("/menu_input", (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'menu_input.html'));
});

// result page
app.get("/menu_result", (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'menu_result.html'));
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});