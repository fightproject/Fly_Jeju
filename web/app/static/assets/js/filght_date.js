var selectElement = document.getElementById("date-select");

// 시작 날짜를 2023년 7월 1일로 설정
var startDate = new Date(2023, 6, 1); // 6은 7월을 의미합니다.
// 종료 날짜를 2023년 8월 31일로 설정
var endDate = new Date(2023, 7, 31); // 7은 8월을 의미합니다.

while (startDate <= endDate) {
  var option = document.createElement("option");
  option.value = formatDate(startDate);
  option.text = formatDate(startDate);
  selectElement.appendChild(option);

  startDate.setDate(startDate.getDate() + 1); // 다음 날짜로 이동
}

selectElement.addEventListener("change", filterByDate);

function filterByDate() {
  var selectedDate = selectElement.value; // Get the selected date value

  // Fetch flight data from the server based on the selected date
  fetchFlightData(selectedDate)
    .then(function(filteredData) {
      updateFlightData(filteredData);
    })
    .catch(function(error) {
      console.log("Error fetching flight data:", error);
    });
}

function fetchFlightData(selectedDate) {
  return fetch("/fetch-flight-data", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ selectedDate: selectedDate })
  })
    .then(function(response) {
      if (!response.ok) {
        throw new Error("Failed to fetch flight data");
      }
      return response.json();
    })
    .then(function(data) {
      return data.filteredData;
    });
}

function updateFlightData(filteredData) {
  var flightListElement = document.getElementById("flight-list");
  flightListElement.innerHTML = ""; // Clear the existing flight list

  // Update the flight list with the filtered data
  for (var i = 0; i < filteredData.length; i++) {
    var flight = filteredData[i];
    var flightItemElement = createFlightItemElement(flight);
    flightListElement.appendChild(flightItemElement);
  }
}

function createFlightItemElement(flight) {
  var flightItemElement = document.createElement("div");
  flightItemElement.classList.add("flight-item");

  return flightItemElement;
}

function formatDate(date) {
  var year = date.getFullYear();
  var month = String(date.getMonth() + 1).padStart(2, "0");
  var day = String(date.getDate()).padStart(2, "0");
  return year + "-" + month + "-" + day;
}