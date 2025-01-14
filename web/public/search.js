document.getElementById('searchButton').addEventListener('click', async function () {
    const query = document.getElementById('searchInput').value;
    if (!query) {
        alert('음식점명을 입력해주세요.');
        return;
    }

    try {
        const response = await fetch(`/api/search?query=${encodeURIComponent(query)}`);
        if (!response.ok) {
            throw new Error('서버 오류가 발생했습니다.');
        }

        const data = await response.json(); // api 응답 데이터
        const resultList = document.getElementById('resultList');
        resultList.innerHTML = ''; // 기존 결과 초기화

        
        if (data.items && data.items.length > 0) {
            data.items.forEach(item => {
                const listItem = document.createElement('div');
                listItem.className = 'list-item non-click';

                const cleanTitle = item.title.replace(/<[^>]+>/g, ''); // <b> 태그 제거
                listItem.textContent = `${cleanTitle} (${item.roadAddress})`;

                resultList.appendChild(listItem);
            });
        } else {
            resultList.innerHTML = '<p>검색 결과가 없습니다.</p>';
        }
    } catch (error) {
        console.error('API 호출 오류', error);
        elert('검색 중 오류가 발생했습니다.')
    }
    document.getElementById('startButton') = true;
});

// 클릭 이벤트 처리
const resultList = document.getElementById('resultList');
resultList.addEventListener('click', (event) => {
  if (event.target.classList.contains('non-click')) {
    // 모든 항목에서 "click" 클래스 제거
    document.querySelectorAll('.non-click').forEach((el) => {
      el.classList.remove('click');
    });

    // 클릭된 항목에 "click" 클래스 추가
    event.target.classList.add('click');
  }
});

document.getElementById('startButton').addEventListener('click', function () {
    alert('작업 시작하기 기능은 구현 중입니다.');
});
