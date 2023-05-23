// 항공권 체크박스 변경 시 총 금액 업데이트
function updateFlightTotal() {
    var flightCheckboxes = document.querySelectorAll('#flight-table-body input[type="checkbox"]');
    var hotelCheckboxes = document.querySelectorAll('#flight-table-body3 input[type="checkbox"]');
    var carCheckboxes = document.querySelectorAll('.customCheck3'); 
    var totalAmount = 0;
    
    carCheckboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
          var price = checkbox.parentNode.parentNode.parentNode.querySelector('td:last-child').textContent;
          totalAmount += parseFloat(price);
        }
      });
    
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
    
    document.getElementById('totalAmount').textContent = totalAmount.toFixed(0);
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

  // 렌트카 체크박스에 이벤트 리스너 추가
  var carCheckboxes = document.querySelectorAll('.customCheck3'); // 변경된 부분: 클래스 선택자 사용
  carCheckboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', updateFlightTotal);
  });

  