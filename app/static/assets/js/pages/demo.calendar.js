var render = {
    renderTable: function() {
      // 함수 내용
    }
  };

! function(l) {
    "use strict";

    function e() {
        this.$body = l("body"),
            this.$modal = l("#event-modal"),
            this.$calendar = l("#calendar"),
            this.$formEvent = l("#form-event"),
            this.$btnNewEvent = l("#btn-new-event"),
            this.$btnDeleteEvent = l("#btn-delete-event"),
            this.$btnSaveEvent = l("#btn-save-event"),
            this.$modalTitle = l("#modal-title"),
            this.$calendarObj = null,
            this.$selectedEvent = null,
            this.$newEventData = null
    }

    e.prototype.onEventClick = function(e) {
            this.$newEventData = null,
                l("#event-title").val(this.$selectedEvent.title),
                l("#event-category").val(this.$selectedEvent.classNames[0])
        },
        e.prototype.onSelect = function(e) {
            this.$calendarObj.unselect()
        }, e.prototype.init = function() {
            var e = new Date(l.now());


            var t = [],
                a = this;
            a.$calendarObj = new FullCalendar.Calendar(a.$calendar[0], {
                    slotDuration: "00:15:00",
                    slotMinTime: "08:00:00",
                    slotMaxTime: "19:00:00",
                    themeSystem: "bootstrap",
                    bootstrapFontAwesome: !1,
                    buttonText: {
                        today: "Today",
                        month: "Month",
                        prev: "Prev",
                        next: "Next"
                    },
                    initialView: "dayGridMonth",
                    handleWindowResize: !0,
                    height: l(window).height() - 200,
                    headerToolbar: {
                        left: "prev,next today",
                        center: "title",
                        right: "dayGridMonth"
                    },

                    initialEvents: function(info, successCallback, failureCallback) {
                        var defaultEvents = [];
                        var $this = this;
                        $.ajax({
                            url: '/demo',
                            method: 'GET',
                            dataType: 'json',
                            success: function(data) {
                                var airplane = JSON.parse(data);
                                jQuery.each(airplane, function() {
                                    defaultEvents.push({
                                        title: Number(this.maxcharge).toLocaleString() + "원",
                                        start: dateformat(this.date),
                                        color: "#f2c2c2"
                                    }, {
                                        title: Number(this.avgcharge).toLocaleString() + "원",
                                        start: dateformat(this.date),
                                        color: "#ebddbc"
                                    }, {
                                        title: Number(this.mincharge).toLocaleString() + "원",
                                        start: dateformat(this.date),
                                        color: "#ff5b5b"
                                    });
                                });
                                successCallback(defaultEvents);
                                // console.log("defaultEvents", defaultEvents);
                            },
                            error: function() {
                                // 데이터를 가져오는 도중 에러가 발생한 경우 실행되는 콜백 함수
                                console.log('Failed to fetch events data.');
                            }
                        });
                    },
                    editable: false,
                    droppable: false,
                    selectable: false,
                    dateClick: function(e) {
                        var date = e.dateStr;
                        var xhr = new XMLHttpRequest();
                        xhr.open('POST', '/filght', true);
                        xhr.setRequestHeader('Content-Type', 'application/json');
                        xhr.onreadystatechange = function() {
                            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                                // 페이지 이동
                                window.location.href = 'filght';
                                render.renderTable();
                            }
                        }
                        xhr.send(JSON.stringify({ date: date }));
                    },
                    eventClick: function(e) {
                        var date = dateformat(e.event.start);
                        var xhr = new XMLHttpRequest();
                        xhr.open('POST', '/filght', true);
                        xhr.setRequestHeader('Content-Type', 'application/json');
                        xhr.onreadystatechange = function() {
                            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                                // 페이지 이동
                                window.location.href = 'filght';
                                render.renderTable();
                            }
                        }
                        xhr.send(JSON.stringify({ date: date }));
                        
                    }
                }),
                // 캘린더로 데이터 전달
                a.$calendarObj.render()
        },
        l.CalendarApp = new e,
        l.CalendarApp.Constructor = e

    function dateformat(date_str) {
        var date = new Date(date_str);
        var year = date.getFullYear();
        var month = ("0" + (date.getMonth() + 1)).slice(-2);
        var day = ("0" + date.getDate()).slice(-2);
        var formatted_date = year + "-" + month + "-" + day;
        return formatted_date;
    }
}(window.jQuery),
function() {
    "use strict";
    window.jQuery.CalendarApp.init()
}();

