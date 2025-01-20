import express from 'express';
import cors from 'cors';
import fetch from 'node-fetch';
import path from 'path';
import { fileURLToPath } from 'url';
import config from '/Users/byurin/scraper/byurin.mjs';

const app = express();
const PORT = 3000;
const { CLIENT_ID, CLIENT_SECRET } = config;

// __dirname 설정 (ES 모듈에서 __dirname 직접 사용 불가)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// 미들웨어 설정
app.use(cors({
  origin: '*',
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// CSP 설정
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self' https://fonts.googleapis.com; https://fonts.gstatic.com;"
  );
  next();
});

// 정적 파일 서비스
app.use(express.static(path.join(__dirname, 'public')));

// 라우팅 설정
const sendFile = (filename) => (req, res) => res.sendFile(path.join(__dirname, 'public', filename));

app.get("/", sendFile('search.html'));
app.get("/menu_input", sendFile('menu_input.html'));
app.get("/menu_result", sendFile('menu_result.html'));

// Naver API 호출 라우트
app.get("/api/search", async (req, res) => {
  const { query } = req.query;
  if (!query) return res.status(400).json({ error: "Query parameter is required" });

  const url = `https://openapi.naver.com/v1/search/local.json?query=${encodeURIComponent(query)}&display=5&start=1&sort=random`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
      },
    });

    if (!response.ok) throw new Error(`Naver API responded with status ${response.status}`);

    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error("API 호출 오류:", error);
    res.status(500).send("Internal Server Error");
  }
});

// 서버 실행
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
