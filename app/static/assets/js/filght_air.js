
function filterTable_air() {
    var selectElement = document.getElementById("status-select");
    var selectedOption = selectElement.value;
    var selectBox = document.getElementById("status-select2");
    var selectedValue = selectBox.value;  // 수정: selectedBox.selectedIndex 대신 selectedBox.value 사용
    var tableBody = document.getElementById("flight-table-body");
    var rows = tableBody.getElementsByTagName("tr");
  
    Array.from(rows).forEach(function(row) {
        tableBody.appendChild(row);
    });
        
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var departureCell = row.getElementsByTagName("td")[4];
        var departure = departureCell.textContent.trim();
        var priceCell = row.querySelector("td:last-child");
        var price = parseInt(priceCell.innerText);

        var priceMatch = true;
        var departureMatch = true;

        // Check if the selected price option matches
        if (selectedOption !== "Choose...") {
            priceMatch =
                (selectedOption === "1" && price > 0 && price <= 50000) ||
                (selectedOption === "2" && price > 50000 && price <= 100000) ||
                (selectedOption === "3" && price > 100000 && price <= 150000) ||
                (selectedOption === "4" && price > 150000 && price <= 200000) ||
                (selectedOption === "5" && price > 200000);
        }

        // Check if the selected departure option matches
        if (selectedValue !== "Choose...") {
            departureMatch =
                (selectedValue === "1" && departure === "GMP") || (selectedValue === "2" && departure === "CJU");
        }

        // Show or hide rows based on the matches
        if (priceMatch && departureMatch) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    }
}

// 이벤트 핸들러 등록
var selectElement = document.getElementById("status-select");
selectElement.addEventListener("change", filterTable_air);

var selectBox = document.getElementById("status-select2");
selectBox.addEventListener("change", filterTable_air);