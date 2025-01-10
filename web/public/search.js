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

        const data = await response.json();
        const resultList = document.getElementById('resultList');
        resultList.innerHTML = '';

        if (data.items && data.items.length > 0) {
            data.items.forEach(item => {
                const listItem = document.createElement('div');
                listItem.className = 'list-item';

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
    document.getElementById('startButton').disabled = true;
});

document.getElementById('startButton').addEventListener('click', function () {
    alert('작업 시작하기 기능은 구현 중입니다.');
});
