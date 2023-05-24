function updateFlightTotal() {
  var flightCheckboxes = document.querySelectorAll('#flight-table-body input[name="flight-checkbox1"]');
  var hotelCheckboxes = document.querySelectorAll('#flight-table-body3 input[name="flight-checkbox2"]');
  var carCheckboxes = document.querySelectorAll('#flight-table-body4 input[name="flight-checkbox3"]');
  var totalAmount = 0;

  // 항공권
  flightCheckboxes.forEach(function (checkbox) {
    if (checkbox.checked) {
      var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
      totalAmount += parseFloat(price);
    }
  });

  // 호텔
  hotelCheckboxes.forEach(function (checkbox) {
    if (checkbox.checked) {
      var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
      totalAmount += parseFloat(price);
    }
  });

  // 렌터카
  carCheckboxes.forEach(function (checkbox) {
    if (checkbox.checked) {
      var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
      totalAmount += parseFloat(price);
    }
  });

  document.getElementById('totalAmount').textContent = totalAmount.toFixed(0);
}

// 항공권 체크박스에 이벤트 리스너 추가
var flightTableBody = document.getElementById('flight-table-body');
flightTableBody.addEventListener('change', function(event) {
  if (event.target.matches('input[name="flight-checkbox1"]')) {
    updateFlightTotal();
  }
});

// 호텔 체크박스에 이벤트 리스너 추가
var hotelCheckboxes = document.querySelectorAll('#flight-table-body3 input[name="flight-checkbox2"]');
hotelCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', updateFlightTotal);
});

// 렌트카 체크박스에 이벤트 리스너 추가
var carCheckboxes = document.querySelectorAll('#flight-table-body4 input[name="flight-checkbox3"]');
carCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', updateFlightTotal);
});

// // 항공권 데이터가 업데이트되기 전에 체크박스의 change 이벤트가 발생하여 updateFlightTotal 함수가 호출되어도 업데이트된 데이터가 아직 화면에 표시되지 않는 것
// yourAjaxFunction(function() {
//   updateFlightTotal();
// });