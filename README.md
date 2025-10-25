# HOAS laundry reservation bot
This bot is used to make laundry reservations in the HOAS booking service (booking-hoas.tampuuri.fi). It makes it possible to select a specific time slot which will be booked automatically for each week. The script should be run on the first day of each month at midnight as that is when the slots for the next month become available.

## Usage
This script can either be used as stand-alone or with the Docker container provided in the packages section. Running the script requires the following environment variables to be set:

- HOAS_USER - a username which is used to log in to the service
- HOAS_PASSWORD - password for the selected user
- HOAS_MACHINE - machine number to be used
- HOAS_TIME - time slot, for example 14.00
- HOAS_WEEKDAY - weekday, 0 for Monday, 6 for Sunday

All environment variables need to be set in order to make the script work. The machine number can be observed on the booking page by hovering over the booking button. The link is in the format https://booking-hoas.tampuuri.fi/varaus/service/reserve/MACHINE_NUMBER/TIME/DATE

**Note:** If the login credentials are incorrect the script does not complete the booking. But if the time slots are already taken, it still tries to book all the slots but does not give any indication on whether the booking was successful or not. The API of the website is not that easy to work with.
