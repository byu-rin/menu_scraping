document.getElementById("menu-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const foodName = document.getElementById("food-name").value;
    const foodDescription = document.getElementById("food-description").value;
    const foodPrice = document.getElementById("food-price").value;
    const isSpecial = document.getElementById("is-special").checked;

    // 입력 데이터를 LocalStorage에 저장
    localStorage.setItem("food-name", foodName);
    localStorage.setItem("food-description", foodDescription);
    localStorage.setItem("food-price", foodPrice);
    localStorage.setItem("is-special", isSpecial);

    // 결과 페이지로 이동
    window.location.href = "/menu_result";
});