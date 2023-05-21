// // 항공권 체크박스 변경 시 총 금액 업데이트
// function updateFlightTotal() {
//     var checkboxes = document.querySelectorAll('#flight-table-body input[type="checkbox"]');
//     var totalAmount = 0;
  
//     checkboxes.forEach(function (checkbox) {
//       if (checkbox.checked) {
//         var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
//         totalAmount += parseFloat(price);
//       }
//     });
  
//     document.getElementById('totalAmount').textContent = totalAmount.toFixed(2);
//   }
  
//   // 호텔 체크박스 변경 시 총 금액 업데이트
//   function updateHotelTotal() {
//     var checkboxes = document.querySelectorAll('#flight-table-body3 input[type="checkbox"]');
//     var totalAmount = 0;
  
//     checkboxes.forEach(function (checkbox) {
//       if (checkbox.checked) {
//         var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
//         totalAmount += parseFloat(price);
//       }
//     });
  
//     document.getElementById('totalAmount').textContent = totalAmount.toFixed(2);
//   }
  
//   // 항공권 체크박스에 이벤트 리스너 추가
//   var flightCheckboxes = document.querySelectorAll('#flight-table-body input[type="checkbox"]');
//   flightCheckboxes.forEach(function (checkbox) {
//     checkbox.addEventListener('change', updateFlightTotal);
//   });
  
//   // 호텔 체크박스에 이벤트 리스너 추가
//   var hotelCheckboxes = document.querySelectorAll('#flight-table-body3 input[type="checkbox"]');
//   hotelCheckboxes.forEach(function (checkbox) {
//     checkbox.addEventListener('change', updateHotelTotal);
//   });


// 항공권 체크박스 변경 시 총 금액 업데이트
function updateFlightTotal() {
    var flightCheckboxes = document.querySelectorAll('#flight-table-body input[type="checkbox"]');
    var hotelCheckboxes = document.querySelectorAll('#flight-table-body3 input[type="checkbox"]');
    var totalAmount = 0;
  
    flightCheckboxes.forEach(function (checkbox) {
      if (checkbox.checked) {
        var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
        totalAmount += parseFloat(price);
      }
    });
  
    hotelCheckboxes.forEach(function (checkbox) {
      if (checkbox.checked) {
        var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
        totalAmount += parseFloat(price);
      }
    });
  
    document.getElementById('totalAmount').textContent = totalAmount.toFixed(2);
  }
  
  // 항공권 체크박스에 이벤트 리스너 추가
  var flightCheckboxes = document.querySelectorAll('#flight-table-body input[type="checkbox"]');
  flightCheckboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', updateFlightTotal);
  });
  
  // 호텔 체크박스에 이벤트 리스너 추가
  var hotelCheckboxes = document.querySelectorAll('#flight-table-body3 input[type="checkbox"]');
  hotelCheckboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', updateFlightTotal);
  });