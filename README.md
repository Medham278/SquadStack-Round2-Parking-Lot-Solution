# Problem Statement :
We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a
number starting at one increasing with increasing distance from the entry point in steps of one.
We want to create an automated ticketing system that allows our customers to use our parking
lot without human intervention.
When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket
issuing process includes:-

1. We are taking note of the number written on the vehicle registration plate and the age of
the driver of the car.
2. And we are allocating an available parking slot to the car before actually handing over a
ticket to the driver (we assume that our customers are kind enough to always park in the
slots allocated to them).
The customer should be allocated a parking slot that is nearest to the entry. At the exit, the
customer returns the ticket, marking the slot they were using as being available.
Due to government regulation, the system should provide us with the ability to find out:-<br>
● Vehicle Registration numbers for all cars which are parked by the driver of a certain age,<br>
● Slot number in which a car with a given vehicle registration plate is parked.<br>
● Slot numbers of all slots where cars of drivers of a particular age are parked.<br>
We get the input by reading input.txt directly (you’ll have to create it in your environment) .The
file will contain a set of commands separated by a newline, we need to execute the commands
in order and produce output.

# Approach :
A utility class named "Parking" is created with the following functions-
1. init() - Initializes a Parkig Lot of specific size <br>
2. park() - Parks the car into the nearest available Parking space<br>
3. getSlotAge() - Gets all the slot numbers (comma-separated) where age of driver is equal to the given age.<br>
4. getSlotRno() - Gets all the slot numbers (comma-separated) where Registration Number of driver is equal to the given Registration Number.<br>
5. getRno() - Gets all the Registration Numbers (comma-separated) where age of driver is equal to the given age.<br>
6. leave() - will vacate the specified Parking slot.<br>

Necessary statements have been added in cases where the command cannot be performed. This makes the program understandable during runtime.<br><br>
__NOTE : main.py print outputs onto Terminal. To make it print into output.py file, uncomment the file2 lines, change printf statements to file2.write and add '\n' to end of each write statement.__