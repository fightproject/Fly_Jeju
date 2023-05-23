function fetchData() {
    var selectedDate = document.getElementById('selectedDate').value;
    var date = JSON.stringify({ date: selectedDate });
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/filght', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // 서버로부터 응답을 받았을 때 수행할 동작을 여기에 작성합니다.
            var responseData = JSON.parse(xhr.responseText);
            renderTable(responseData);
        }
    }
    
    xhr.send(date);
}

function renderTable(data) {
    var flightTableBody = document.getElementById('flight-table-body');
    flightTableBody.innerHTML = '';
    
    data.forEach(function(flight, index) {
        var row = document.createElement('tr');
        
        var checkboxCell = document.createElement('td');
        var checkboxLabel = document.createElement('label');
        checkboxLabel.className = 'custom-control-label';
        checkboxLabel.htmlFor = 'customCheck' + (index + 1);

        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = 'flight-checkbox';
        checkbox.value = index;
        checkbox.className = 'custom-control-input';
        checkbox.id = 'customCheck' + (index + 1);
        checkbox.style.margin = 'auto';
        checkbox.style.display = 'block';
    
        
        checkboxCell.appendChild(checkbox);
        checkboxCell.appendChild(checkboxLabel);
        
        var dateCell = document.createElement('td');
        var dateString = flight.date;
        var dateObj = new Date(dateString);
        var formattedDate = dateObj.toISOString().slice(0, 10);
        dateCell.textContent = formattedDate;
        
        var dayCell = document.createElement('td');
        dayCell.textContent = flight.day;
        
        var nameCell = document.createElement('td');
        nameCell.textContent = flight.name;
        
        var airportCell = document.createElement('td');
        airportCell.textContent = flight.airport;
        
        var leavetimeCell = document.createElement('td');
        leavetimeCell.textContent = flight.leavetime;
        
        var reachtimeCell = document.createElement('td');
        reachtimeCell.textContent = flight.reachtime;
        
        var seatCell = document.createElement('td');
        seatCell.textContent = flight.seat;
        
        var chargeCell = document.createElement('td');
        chargeCell.textContent = flight.charge;
        
        row.appendChild(checkboxCell);
        row.appendChild(dateCell);
        row.appendChild(dayCell);
        row.appendChild(nameCell);
        row.appendChild(airportCell);
        row.appendChild(leavetimeCell);
        row.appendChild(reachtimeCell);
        row.appendChild(seatCell);
        row.appendChild(chargeCell);
        
        flightTableBody.appendChild(row);
    });
}

