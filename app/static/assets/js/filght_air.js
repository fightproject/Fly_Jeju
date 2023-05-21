function filterTable() {
    var selectElement = document.getElementById("status-select");
    var selectedOption = selectElement.value;
    var tableBody = document.getElementById("flight-table-body");
    var rows = tableBody.getElementsByTagName("tr");

    // Sort the rows based on the price column (ascending order)
    Array.from(rows).sort(function(a, b) {
        var priceA = parseInt(a.querySelector("td:last-child").innerText);
        var priceB = parseInt(b.querySelector("td:last-child").innerText);
        return priceA - priceB;
    }).forEach(function(row) {
        tableBody.appendChild(row);
    });
    
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var priceElement = row.querySelector("td:last-child");
        var price = parseInt(priceElement.innerText);

        if (selectedOption === ""|| selectedOption === "Choose...")  { 
            // 선택된 옵션이 없을 경우 모든 행을 출력
            row.style.display = "";
        } else if (selectedOption === "1" && (price > 50000)) {
            row.style.display = "none";
        } else if (selectedOption === "2" && (price <= 50000 || price > 100000)) {
            row.style.display = "none";
        } else if (selectedOption === "3" && (price <= 100000 || price > 150000)) {
            row.style.display = "none";
        } else if (selectedOption === "4" && (price <= 150000 || price > 200000)) {
            row.style.display = "none";
        } else if (selectedOption === "5" && (price <= 200000)) {
            row.style.display = "none";
        } else {
            row.style.display = "";
        }
    }
}