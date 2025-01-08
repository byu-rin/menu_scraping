window.addEventListener("load", function() {
    // LocalStorage에서 메뉴 데이터를 가져옴
    const foodName = localStorage.getItem("food-name");
    const foodDescription = localStorage.getItem("food-description");
    const foodPrice = localStorage.getItem("food-price");
    const isSpecial = localStorage.getItem("is-special");

    // 메뉴 데이터가 없으면 경고 메시지 표시
    if (!foodName || !foodDescription || !foodPrice) {
        alert("메뉴 정보가 없습니다.");
        return;
    }

    // 결과 페이지에 데이터 삽입
    document.getElementById("food-name-result").textContent = foodName;
    document.getElementById("food-description-result").textContent = foodDescription;
    document.getElementById("food-price-result").textContent = `₩ ${foodPrice}`;

    // 대표메뉴 표시 여부
    if (isSpecial === "true") {
        document.getElementById("special-badge").textContent = "대표메뉴";
    }
});