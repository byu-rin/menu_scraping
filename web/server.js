const path = require("path");
const express = require("express");
const app = express();

// 정적 파일 경로 설정
app.use(express.static(path.join(__dirname, 'web')));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, 'search.html'));
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});