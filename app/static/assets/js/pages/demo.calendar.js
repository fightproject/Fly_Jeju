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
            this.$modalTitle = l("#modal-title")

    }
    e.prototype.init = function() {
            var e = new Date(l.now());
            new FullCalendar.Draggable(document.getElementById("external-events"), {
                itemSelector: ".external-event",
                eventData: function(e) {
                    return {
                        title: e.innerText,
                        className: l(e).data("class")
                    }
                }
            });
console.log("didididididididididdi");
            // var t = [{
            //     title: "Meeting with Mr. Shreyu",
            //     start: new Date(l.now() + 158e6),
            //     end: new Date(l.now() + 338e6),
            //     className: "bg-warning"
            // }];
            var t = [];
            // Ajax를 사용하여 데이터 받아오기
            l.ajax({
                url: '/demo',
                method: 'GET',
                dataType: 'json',
                success: function(data) {
                    var airplane = JSON.parse(data);
                    // console.log(typeof 'airplane');
                    for (var i = 0; i < airplane.length; i++) {
                        t.push({
                            title: airplane[i].charge,
                            start: new Date(airplane[i].date),
                            // end: new Date(airplane[i].date),
                            className: "bg-warning"
                        });
                    }

                    console.log("ttttt", t);
                },
                error: function() {
                    // 데이터를 가져오는 도중 에러가 발생한 경우 실행되는 콜백 함수
                    console.log('Failed to fetch events data.');
                }
            });
            var a = this;
            a.$calendarObj = new FullCalendar.Calendar(
                a.$calendar[0], {
                    slotDuration: "00:15:00",
                    slotMinTime: "08:00:00",
                    slotMaxTime: "19:00:00",
                    themeSystem: "bootstrap",
                    bootstrapFontAwesome: !1,
                    buttonText: {
                        today: "Today",
                        month: "Month",
                        week: "Week",
                        day: "Day",
                        list: "List",
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
                    initialEvents: t, // 빈 배열로 초기화
                    editable: !0,
                    droppable: !0,
                    selectable: !0,
                    // dateClick: function(e) { a.onSelect(e) },
                    // eventClick: function(e) { a.onEventClick(e) }
                }
            );
            a.$calendarObj.render(),
                a.$btnNewEvent.on("click", function(e) {
                    a.onSelect({ date: new Date, allDay: !0 })
                }),
                a.$formEvent.on("submit", function(e) {
                    e.preventDefault();
                    var t, n = a.$formEvent[0];
                    n.checkValidity() ? (
                        a.$selectedEvent ? (
                            a.$selectedEvent.setProp(
                                "title",
                                l("#event-title").val()
                            ), a.$selectedEvent.setProp(
                                "classNames", [l("#event-category").val()]
                            )
                        ) : (t = {
                                title: l("#event-title").val(),
                                start: a.$newEventData.date,
                                allDay: a.$newEventData.allDay,
                                className: l("#event-category").val()
                            },
                            a.$calendarObj.addEvent(t)), a.$modal.modal("hide")) : (e.stopPropagation(), n.classList.add("was-validated"))
                }),
                l(a.$btnDeleteEvent.on("click", function(e) {
                    a.$selectedEvent &&
                        (
                            a.$selectedEvent.remove(),
                            a.$selectedEvent = null,
                            a.$modal.modal("hide")
                        )
                }))
        },
        l.CalendarApp = new e,
        l.CalendarApp.Constructor = e
}(window.jQuery),
function() {
    "use strict";
    window.jQuery.CalendarApp.init()
}();