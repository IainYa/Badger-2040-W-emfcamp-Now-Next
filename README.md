# Badger-2040-emfcamp-Now-Next
An app for the Badger 2040 (Original and W versions) to display Now/Next info for the main stages at EMF2024.  Intended to be copied into the Badger OS that ships with the badge.

The app should work on both versions of the badge.  The app checks the version of the badge and uses a local copy of the schedule if WiFi is not available.

This app uses an adapter for the EMF API which can be found here:  https://github.com/DanNixon/emfcamp-schedule-api/tree/main/adapter
The adapter allows for testing by including a fake_epoch which offsets the schedule accordingly.  Thanks Dan! :-)

**N.B. This is all subject to change as the 2024 schedule has not been released yet.  Some changes are likely and there may be updates up to the start of the event and potentially during.**

![Main page showing now and next](/photos/Main.jpg)

# Installation
Copy the files from the Code folder into the Badger OS firmware folder structure.

# Setup for offline use.
No additional setup is required.

## Optionally:
  The `static_schedule.json` file can be manually updated by running the `make_static_schedule.py` script which can be found in the prebuild folder.

# Setup
WiFi is required for calls to the  so the app assumes you've already set up the WIFI_CONFIG.py file on the badge.


## fake_epoch for testing
In schedule.py, there is a variable called URL which includes the `fake_epoch` value.  The date and time should be set to something within the last couple of days for testing.  At EMF 2022, the first event in the schedule was at 10:00AM, the day before the opening ceremony so if you set the fake_epoch to yesterday at 10:00AM, it will be like reliving the first day of EMF 2022!
Once the 2024 schedule goes live, the offset will likely be different so the fake_epoch will need to be adjusted accordingly (and potentially as new events are added).


## Remove the fake_epoch for use at EMF 2024
The `fake_epoch` portion of the query should be removed from the `URL` when using the app at EMF 2024 - unless you really want to pretend you're living in a different timezone!
For live use, the URL should be defined as:

`URL = "https://schedule.emfcamp.dan-nixon.com/now-and-next?venue=Stage+A&venue=Stage+B&venue=Stage+C"`


## Sleep options
If no buttons are pressed for a certain time, the badge will go to sleep and wake up periodically to refresh, update the screen and go back to sleep again.  If a button is pressed then the badge will wake up and refresh straight away.

The `sleeptime` variable sets the time between updates.

The `timeout` variable defines how quickly the badge goes to sleep.  By default, this is 10 seconds when waking up to refresh or 30 seconds if woken up by a button press.

These values should be edited in the code if you wish to change them.


# Usage
When the app starts or wakes up, it will connect to WiFi and retrieve the Now and Next events for Stages A, B and C.  It will then display the main page with an overview of all three stages.

Pressing `BUTTON_A`, `BUTTON_B` or `BUTTON_C` will open the details for the "now" event on the respective stage.  Pressing the same button again will open the details for the "next" event on that Stage.  Subsequent presses will toggle between "now" and "next".

Pressing `BUTTON_UP` will go back to the main page.

Pressing `BUTTON_DOWN` will refresh the data and go back to the main page.

The LED indicates whether the app is running or the badge is sleeping.
