# Badger-2040-W-emfcamp-Now-Next
An app for the Badger 2040 W to display Now/Next info for the main stages at EMF2024.  Intended to be copied into the Badger OS that ships with the badge.

This app uses and adapter for the EMF API which can be found here:  https://github.com/DanNixon/emfcamp-schedule-api/tree/main/adapter  Thanks Dan! :-)
The adapter allows for testing by including a fake_epoch which offsets the schedule accordingly.

**N.B. this is all subject to change as the 2024 schedule has not been released yet.  Some changes are likely.**


# Installation
Copy the files from the Code folder into the Badger OS firmware folder structure.


# Setup

## fake_epoch for testing
In schedule.py, there is a variable called URL which includes the `fake_epoch` value.  The date and time should be set to something within the last couple of days for testing.  At EMF 2022, the first event in the schedule was at 10:00AM, the day before the opening ceremony so if you set the fake_epoch to yesterday at 10:00AM, it will be like reliving the first day of EMF 2022!
Once the 2024 schedule goes live, the offset will likely be different so the fake_epoch will need to be adjusted accordingly (and potentially as new events are added).

## Remove the fake_epoch for use at EMF 2024
The `fake_epoch` portion of the event should be removed from the URL variable when using the app at EMF 2024 - unless you really want to pretend you're living in a different timezone!
For live use, the URL should be defined as:

`URL = "http://schedule.emfcamp.dan-nixon.com/now-and-next?venue=Stage+A&venue=Stage+B&venue=Stage+C"`

## Sleep options
If no buttons are pressed for a certain time, the badge will go to sleep and wake up periodically to refresh, update the screen and go back to sleep again.  If a button is pressed then the badge will wake up and refresh straight away.

The `sleeptime` variable sets the time between updates.

The `timeout` variable defines how quickly the badge goes to sleep.  By default, this is 10 seconds when waking up to refresh or 30 seconds if woken up by a button press.

