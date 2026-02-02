# 네이버맵 메뉴 크롤러

## 설명
네이버 지도에서 음식점의 메뉴 정보를 수집하는 커맨드라인 기반 크롤링 도구입니다.
음식점 이름을 입력하면 메뉴명과 가격을 정리된 형식으로 출력합니다.

## 기술 스택
- **Python 3.13**
- **Selenium** - 동적 콘텐츠를 위한 브라우저 자동화
- **webdriver-manager** - ChromeDriver 자동 버전 관리
- **Chrome (Headless)** - 백그라운드 브라우저 실행

## 주요 기능
- 네이버 지도에서 음식점 이름으로 검색
- 메뉴명, 설명, 가격 정보 추출
- 대표 메뉴(⭐) 자동 식별
- 서버 및 CI 환경을 위한 Headless 모드 지원
- Chrome 버전에 맞는 ChromeDriver 자동 매칭

>[!TIP]
>음식점 이름은 네이버 지도에 등록된 정식 명칭을 입력하면 검색 정확도가 높아집니다.

<br>

## 실행 화면
**터미널 출력 예시**
```markdown
음식점명을 입력하세요: 후라토식당 잠실직영점

'후라토식당 잠실직영점' 검색 중...

==================================================
 후라토식당 잠실직영점 메뉴
==================================================

  규카츠 ⭐ 대표
    19,000원

  반숙 오므라이스 ⭐ 대표
    14,000원

  스테키 정식 ⭐ 대표
    19,000원
  ...
==================================================
```

## 설치

```bash
# 저장소 클론
git clone https://github.com/byu-rin/menu_scraping.git
cd naver-menu-crawler

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

>[!IMPORTANT]
>Chrome 브라우저가 반드시 설치되어 있어야 합니다.
>Chrome이 설치되어 있지 않으면 Selenium 실행이 실패합니다.

<br>

## 실행 방법

```bash
python crawler/scraper.py
```

>[!NOTE]
>본 프로그램은 커맨드라인(CLI) 기반으로 동작하며, 실행 후 음식점 이름을 입력받습니다.

<br>

## 설계 결정 및 기술적 고민

### 1. ChromeDriver 자동 관리

ChromeDriver는 설치된 Chrome 브라우저 버전과 정확히 일치해야 하며,
Chrome이 자동 업데이트될 경우 수동 관리 방식은 쉽게 깨집니다.

webdriver-manager를 사용하여 실행 시점에 알맞은 ChromeDriver를 자동으로 다운로드 및 캐싱하도록 구성했습니다.

```python
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
```

>[!IMPORTANT]
>이 방식으로 개발 환경 차이로 인한 실행 오류를 최소화할 수 있습니다.

<br>

### 2. Headless 브라우저 크롤링

GUI 브라우저 실행은 자동화나 서버 환경에서 비효율적입니다.

JavaScript 실행은 유지하면서, 화면 출력 없이 동작하는 Headless 모드로 Chrome을 설정했습니다.

```python
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
```

>[!TIP]
>Headless 모드는 CI/CD 환경이나 원격 서버에서 특히 유용합니다.

<br>

### 3. 중첩 iframe 처리

네이버 지도는 음식점 상세 정보를 entryIframe 내부에 로드하여
일반적인 DOM 접근이 불가능합니다.

명시적 대기(Explicit Wait)와 iframe 전환을 통해 내부 콘텐츠에 접근하도록 구현했습니다.

```python
driver.switch_to.frame("entryIframe")
```

>[!NOTE]
>iframe 구조를 파악하지 않으면 메뉴 영역이 비어 있는 상태로 크롤링될 수 있습니다.

<br>

### 4. 동적 콘텐츠 로딩 처리

메뉴 정보는 페이지 로드 시점이 아닌,
메뉴 탭 클릭 이후 비동기적으로 로딩됩니다.

요소가 렌더링될 때까지 대기하는 로직을 추가하여 안정적으로 데이터를 수집하도록 했습니다.

>[!WARNING]
>고정된 sleep 시간에 의존할 경우,
>네트워크 상태에 따라 크롤링 실패 가능성이 높아집니다.

-----------

# Naver Map Menu Crawler

## Description
A command-line based crawling tool that collects restaurant menu information from Naver Map.
Enter a restaurant name to receive a neatly formatted list of menu items and prices.

## Tech Stack
- Python 3.13
- Selenium – Browser automation for handling dynamic content
- webdriver-manager – Automatic ChromeDriver version management
- Chrome (Headless) – Background browser execution

## Key Features
- Search restaurants by name on Naver Map
- Extract menu names, descriptions, and prices
- Automatically identify signature dishes
- Support headless mode for server and CI environments
- Automatically match ChromeDriver with the installed Chrome version

>[!TIP]
>Using the restaurant’s official name registered on Naver Map improves search accuracy.

<br>

## Screenshots
**Terminal Output Example**
```markdown
음식점명을 입력하세요: 후라토식당 잠실직영점

'후라토식당 잠실직영점' 검색 중...

==================================================
 후라토식당 잠실직영점 메뉴
==================================================

  규카츠 ⭐ 대표
    19,000원

  반숙 오므라이스 ⭐ 대표
    14,000원

  스테키 정식 ⭐ 대표
    19,000원
  ...
==================================================
```

## 설치

```Installation
# Clone the repository
git clone https://github.com/byu-rin/menu_scraping.git
cd naver-menu-crawler

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

>[!IMPORTANT]
>Google Chrome must be installed.
>Selenium will fail to run if Chrome is not available.

<br>

## Usage

```bash
python crawler/scraper.py
```

>[!NOTE]
>This program runs as a command-line interface (CLI) and prompts the user to enter a restaurant name after execution.

<br>

## Design Decisions & Technical Challenges

### 1. Automatic ChromeDriver Management

ChromeDriver must exactly match the installed Chrome browser version,
and manual management easily breaks when Chrome updates automatically.

To solve this, webdriver-manager is used to automatically download and cache the appropriate ChromeDriver version at runtime.

```python
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
```

>[!IMPORTANT]
>This approach minimizes execution errors caused by differences between development environments.

<br>

### 2. Headless Browser Crawling

Running a visible GUI browser is inefficient in automation and server environments.

Chrome is configured to run in headless mode while fully preserving JavaScript execution.

```python
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
```

>[!TIP]
>Headless mode is especially useful in CI/CD pipelines and remote servers.

<br>

### 3. Nested iframe Handling

Naver Map loads restaurant detail pages inside an iframe named entryIframe,
making direct DOM access impossible.

Explicit waits and iframe context switching were implemented to access the nested content.

```python
driver.switch_to.frame("entryIframe")
```

>[!NOTE]
>Without understanding the iframe structure, the menu section may be scraped as empty.

<br>

### 4. Dynamic Content Loading

Menu information is not loaded on initial page render,
but asynchronously after clicking the menu tab.

Additional waiting logic was implemented to ensure elements are fully rendered before extraction.

>[!WARNING]
>Relying on fixed sleep delays can lead to crawling failures depending on network conditions.

<br>

## License
MIT



   
