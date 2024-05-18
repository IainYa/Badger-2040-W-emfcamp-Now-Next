import time
import badger2040
import badger_os
import jpegdec
import json

URL = "https://2022.schedule.emfcamp.dan-nixon.com/now-and-next?fake_epoch=2024-05-16T10:00:00%2b01:00&venue=Stage+A&venue=Stage+B&venue=Stage+C"
#URL = "https://schedule.emfcamp.dan-nixon.com/now-and-next?venue=Stage+A&venue=Stage+B&venue=Stage+C" # For using at EMF

offline = 0

if badger2040.is_wireless():
    import urequests
else:
    offline = 1

state = {
    "display_time": "2022-06-03 10:15:00"
}


display = badger2040.Badger2040()
jpeg = jpegdec.JPEG(display.display)

badger_os.state_load("schedule", state)

display.led(255)

sleeptime = 10 #Minutes

if badger2040.woken_by_rtc():
    timeout = 10 #Seconds
else:
    timeout = 30 #Seconds

lastPress = time.time()


class Page():
    MAIN = 0
    NOWA = 1
    NEXTA = 2
    NOWB = 3
    NEXTB = 4
    NOWC = 5
    NEXTC = 6

curPage = Page.MAIN

class Event():
    def __init__(self, venue, nownext):
        self.venue = venue
        self.nownext = nownext
        self.prev_start = ""
        self.start_date = ""
        self.end_date = ""
        self.title = ""
        self.speaker = ""
        self.description = ""

EventNowA = Event("Stage A", "now")
EventNextA = Event("Stage A", "next")
EventNowB = Event("Stage B", "now")
EventNextB = Event("Stage B", "next")
EventNowC = Event("Stage C", "now")
EventNextC = Event("Stage C", "next")
    

URL = "https://2022.schedule.emfcamp.dan-nixon.com/now-and-next?fake_epoch=2024-05-16T10:00:00%2b01:00&venue=Stage+A&venue=Stage+B&venue=Stage+C"
#URL = "https://schedule.emfcamp.dan-nixon.com/now-and-next?venue=Stage+A&venue=Stage+B&venue=Stage+C" # For using at EMF

if badger2040.is_wireless():
    try:
        display.connect()
    except:
        offline = 1

display.set_pen(15)
display.clear()
display.set_pen(0)

display.set_update_speed(badger2040.UPDATE_MEDIUM)


def get_data():
    global nowA, nextA, nowB, nextB, nowC, nextC
    
    req = URL
    print(f"Requesting URL: {req}")
    if offline == 0:
        r = urequests.get(req)
        j = r.json()
        
        print("Data obtained!")
        try:
            start = j["guide"]["Stage A"]["now"][0]["start_date"][11:16]
        except:
            EventNowA.start_date = ""
            EventNowA.end_date = ""
            EventNowA.title = ""
            EventNowA.speaker = ""
            EventNowA.description = ""
            nowA = "Nothing on Stage A"
        else:
            EventNowA.start_date = j["guide"]["Stage A"]["now"][0]["start_date"]
            EventNowA.end_date = j["guide"]["Stage A"]["now"][0]["end_date"]
            EventNowA.title = j["guide"]["Stage A"]["now"][0]["title"]
            EventNowA.speaker = j["guide"]["Stage A"]["now"][0]["speaker"]
            EventNowA.description = j["guide"]["Stage A"]["now"][0]["description"]
            nowA = "{} {} - {} ".format(EventNowA.start_date[11:16], EventNowA.title, EventNowA.speaker)
        print (nowA)
        
        try:
            start = j["guide"]["Stage A"]["next"][0]["start_date"][11:16]
        except:
            EventNextA.start_date = ""
            EventNextA.end_date = ""
            EventNextA.title = ""
            EventNextA.speaker = ""
            EventNextA.description = ""
            nextA = "Nothing on Stage A"
        else:
            EventNextA.start_date = j["guide"]["Stage A"]["next"][0]["start_date"]
            EventNextA.end_date = j["guide"]["Stage A"]["next"][0]["end_date"]
            EventNextA.title = j["guide"]["Stage A"]["next"][0]["title"]
            EventNextA.speaker = j["guide"]["Stage A"]["next"][0]["speaker"]
            EventNextA.description = j["guide"]["Stage A"]["next"][0]["description"]
            nextA = "{} {} - {} ".format(EventNextA.start_date[11:16], EventNextA.title, EventNextA.speaker)
        print (nextA)
            
        try:
            start = j["guide"]["Stage B"]["now"][0]["start_date"][11:16]
        except:
            EventNowB.start_date = ""
            EventNowB.end_date = ""
            EventNowB.title = ""
            EventNowB.speaker = ""
            EventNowB.description = ""
            nowB = "Nothing on Stage B"
        else:
            EventNowB.start_date = j["guide"]["Stage B"]["now"][0]["start_date"]
            EventNowB.end_date = j["guide"]["Stage B"]["now"][0]["end_date"]
            EventNowB.title = j["guide"]["Stage B"]["now"][0]["title"]
            EventNowB.speaker = j["guide"]["Stage B"]["now"][0]["speaker"]
            EventNowB.description = j["guide"]["Stage B"]["now"][0]["description"]
            nowB = "{} {} - {} ".format(EventNowB.start_date[11:16], EventNowB.title, EventNowB.speaker)
        print (nowB)
        
        try:
            start = j["guide"]["Stage B"]["next"][0]["start_date"][11:16]
        except:
            EventNextB.start_date = ""
            EventNextB.end_date = ""
            EventNextB.title = ""
            EventNextB.speaker = ""
            EventNextB.description = ""
            nextB = "Nothing on Stage B"
        else:
            EventNextB.start_date = j["guide"]["Stage B"]["next"][0]["start_date"]
            EventNextB.end_date = j["guide"]["Stage B"]["next"][0]["end_date"]
            EventNextB.title = j["guide"]["Stage B"]["next"][0]["title"]
            EventNextB.speaker = j["guide"]["Stage B"]["next"][0]["speaker"]
            EventNextB.description = j["guide"]["Stage B"]["next"][0]["description"]
            nextB = "{} {} - {} ".format(EventNextB.start_date[11:16], EventNextB.title, EventNextB.speaker)
        print (nextB)
        
        try:
            start = j["guide"]["Stage C"]["now"][0]["start_date"][11:16]
        except:
            EventNowC.start_date = ""
            EventNowC.end_date = ""
            EventNowC.title = ""
            EventNowC.speaker = ""
            EventNowC.description = ""
            nowC = "Nothing on Stage C"
        else:
            EventNowC.start_date = j["guide"]["Stage C"]["now"][0]["start_date"]
            EventNowC.end_date = j["guide"]["Stage C"]["now"][0]["end_date"]
            EventNowC.title = j["guide"]["Stage C"]["now"][0]["title"]
            EventNowC.speaker = j["guide"]["Stage C"]["now"][0]["speaker"]
            EventNowC.description = j["guide"]["Stage C"]["now"][0]["description"]
            nowC = "{} {} - {} ".format(EventNowC.start_date[11:16], EventNowC.title, EventNowC.speaker)
        print (nowC)
        
        try:
            start = j["guide"]["Stage C"]["next"][0]["start_date"][11:16]
        except:
            EventNextC.start_date = ""
            EventNextC.end_date = ""
            EventNextC.title = ""
            EventNextC.speaker = ""
            EventNextC.description = ""
            nextC = "Nothing on Stage C"
        else:
            EventNextC.start_date = j["guide"]["Stage C"]["next"][0]["start_date"]
            EventNextC.end_date = j["guide"]["Stage C"]["next"][0]["end_date"]
            EventNextC.title = j["guide"]["Stage C"]["next"][0]["title"]
            EventNextC.speaker = j["guide"]["Stage C"]["next"][0]["speaker"]
            EventNextC.description = j["guide"]["Stage C"]["next"][0]["description"]
            nextC = "{} {} - {} ".format(EventNextC.start_date[11:16], EventNextC.title, EventNextC.speaker)
        print (nextC)


def get_events(venue, eventNow, eventNext):
    global state
        
    with open("/schedule/static-schedule.json") as f:
        j = json.load(f)
    
    if state["display_time"] == "":
        print("Display time not set")
        state["display_time"]= j[0]["start_date"]
        badger_os.state_save("schedule", state)
    
    eventNow.start_date = ""
    eventNext.start_date = ""
    
    for event in j:
        if event["venue"] == venue:
            if event["end_date"] < state["display_time"]:
                eventNow.prev_start = event["start_date"]
            if event["start_date"] <= state["display_time"] and state["display_time"] < event["end_date"]:
                if eventNow.prev_start == "" and event["end_date"] < state["display_time"]:
                    eventNow.prev_start = event["start_date"]
                eventNow.start_date = event["start_date"]
                eventNow.end_date = event["end_date"]
                eventNow.title = event["title"]
                eventNow.speaker = event["speaker"]
                eventNow.description = event["description"]
            if event["start_date"] > state["display_time"]:
                eventNext.start_date = event["start_date"]
                eventNext.end_date = event["end_date"]
                eventNext.title = event["title"]
                eventNext.speaker = event["speaker"]
                eventNext.description = event["description"]
                break
        
    

def get_local_data():
    global nowA, nextA, nowB, nextB, nowC, nextC, prev_time, next_time
    
    get_events("Stage A", EventNowA, EventNextA)
    if EventNowA.start_date == "":
        nowA = "Nothing on Stage A"
    else:
        nowA = "{} {} - {} ".format(EventNowA.start_date[11:16], EventNowA.title, EventNowA.speaker)
    if EventNextA.start_date == "":
        nextA = "Nothing on Stage A"
    else:
        nextA = "{} {} - {} ".format(EventNextA.start_date[11:16], EventNextA.title, EventNextA.speaker)
    
    get_events("Stage B", EventNowB, EventNextB)
    if EventNowB.start_date == "":
        nowB = "Nothing on Stage B"
    else:
        nowB = "{} {} - {} ".format(EventNowB.start_date[11:16], EventNowB.title, EventNowB.speaker)
    if EventNextB.start_date == "":
        nextB = "Nothing on Stage B"
    else:
        nextB = "{} {} - {} ".format(EventNextB.start_date[11:16], EventNextB.title, EventNextB.speaker)
    
    get_events("Stage C", EventNowC, EventNextC)
    if EventNowC.start_date == "":
        nowC = "Nothing on Stage C"
    else:
        nowC = "{} {} - {} ".format(EventNowC.start_date[11:16], EventNowC.title, EventNowC.speaker)
    if EventNextC.start_date == "":
        nextC = "Nothing on Stage C"
    else:
        nextC = "{} {} - {} ".format(EventNextC.start_date[11:16], EventNextC.title, EventNextC.speaker)
    
    prev_time = max(EventNowA.prev_start, EventNowB.prev_start, EventNowC.prev_start)
    next_time = min(EventNextA.start_date, EventNextB.start_date, EventNextC.start_date)
    print("{} {} {} ".format(EventNowA.prev_start, EventNowB.prev_start, EventNowC.prev_start))
    print("Prev time: {}".format(prev_time))
    print("{} {} {} ".format(EventNextA.start_date, EventNextB.start_date, EventNextC.start_date))
    print("Next time: {}".format(next_time))
    

def display_main():
    curPage = Page.MAIN
    
    w, h = display.get_bounds()
    
    display.set_pen(15)
    display.clear()
    display.set_pen(0)
    display.rectangle(0, 0, w, 10)
    display.rectangle(0, 0, 27, h)
    display.line(0, 49, w, 49)
    display.line(0, 89, w, 89)
    
    display.set_pen(15)
    display.set_font("bitmap8")
    display.set_thickness(4)
    if offline == 1:
        display.text("OFFLINE" , 2, 2, scale=1)
    display.text("EMF - Now and Next - Main Stages" , 50, 2, scale=1)
    display.text(state["display_time"][11:16], 270, 2, scale=1)
    
    s = 1.3
    display.set_pen(15)
    display.set_font("sans")
    display.set_thickness(4)
    display.text("A" , 2, 30, scale=s)
    display.text("B" , 0, 70, scale=s)
    display.text("C" , 0, 110, scale=s)
 
    s = 0.35
    l = 32
    display.set_pen(0)
    display.set_font("bitmap8")
    display.set_thickness(2)
    display.text(nowA , l, 15, scale=s)
    display.text(nextA , l, 30, scale=s)
    display.text(nowB , l, 55, scale=s)
    display.text(nextB , l, 70, scale=s)
    display.text(nowC , l, 95, scale=s)
    display.text(nextC , l, 110, scale=s)
    
    display.update()


def display_Stage(event):
    
    w, h = display.get_bounds()
    
    display.set_pen(15)
    display.clear()
    display.set_pen(0)
    display.rectangle(0, 0, w, 10)
    display.rectangle(0, 0, 27, h)
    
    display.set_pen(15)
    display.set_font("bitmap8")
    display.set_thickness(4)
    if offline == 1:
        display.text("OFFLINE" , 2, 2, scale=1)
    display.text("EMF - {} - {}".format(event.nownext, event.venue) , 50, 2, scale=1) ####
    
    s = 1.3
    display.set_pen(15)
    display.set_font("sans")
    display.set_thickness(4)
    display.text(event.venue.replace("Stage ", "") , 0, 70, scale=s) ####

    s1 = 0.5
    s2 = 0.4
    l = 35
    display.set_pen(0)
    display.set_font("bitmap14_outline")
    display.set_thickness(1)
    if event.start_date == "":
        jpeg.open_file("/icons/icon-cryingTilda.jpg")
        jpeg.decode(178,10)
        display.set_pen(0)
        display.set_font("sans")
        display.set_thickness(2)
        display.text("Nothing", l, 50, scale=1.2)
        display.text("{}".format(event.nownext), l, 85, scale=1.2 )
    else:
        display.set_font("bitmap14_outline")
        display.set_thickness(2)
        display.text("{} - {}".format(event.start_date[11:16],event.end_date[11:16]) , l, 15, scale=s1) ####
        display.text(event.title, l, 30, scale=s2)  ####
        display.set_font("bitmap8")
        display.text(event.speaker, l, 45, scale=1)  ####
        desc = event.description
        while desc.rfind("\r\n\r\n") != -1:
            desc = desc.replace("\r\n\r\n", "\r\n")
        display.text(desc, l, 60, wordwrap=w-l, scale=1.5)
    display.update()

    
if offline == 0:
    get_data()
else:
    get_local_data()

display_main()
badger2040.reset_pressed_to_wake()

while True:
    if display.pressed(badger2040.BUTTON_UP):
        lastPress = time.time()
        if curPage != Page.MAIN:
            display_main()
        else:
            if offline == 1:
                state["display_time"] = prev_time
                badger_os.state_save("schedule", state)
                print(state["display_time"])
                get_local_data()
                display_main()
    if display.pressed(badger2040.BUTTON_DOWN):
        lastPress = time.time()
        if offline == 1:
            state["display_time"] = next_time
            badger_os.state_save("schedule", state)
            print("down")
            print(state["display_time"])
            get_local_data()
            display_main()
        else:
            get_data()
            display_main()
    if display.pressed(badger2040.BUTTON_A):
        lastPress = time.time()
        if curPage == Page.NOWA:
            curPage = Page.NEXTA
            display_Stage(EventNextA)
        else:
            curPage = Page.NOWA
            display_Stage(EventNowA)
            
    if display.pressed(badger2040.BUTTON_B):
        lastPress = time.time()
        if curPage == Page.NOWB:
            curPage = Page.NEXTB
            display_Stage(EventNextB)
        else:
            curPage = Page.NOWB
            display_Stage(EventNowB)
            
    if display.pressed(badger2040.BUTTON_C):
        lastPress = time.time()
        if curPage == Page.NOWC:
            curPage = Page.NEXTC
            display_Stage(EventNextC)
        else:
            curPage = Page.NOWC
            display_Stage(EventNowC)
    
    if time.time() - lastPress > timeout:
        print("Going to sleep now.")
        if badger2040.is_wireless():
            badger2040.sleep_for(sleeptime)
        else:
            badger2040.turn_off()