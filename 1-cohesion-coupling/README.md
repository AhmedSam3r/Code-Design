# Problem 
* There's a direct coupling of brand name and catalogue price (bad)
* We've a brand information, but also we've vechile instance information such as ID and lisence plate.
* register_vehicle method has to know the implementation details of generate_id() and generate_lisence()

* Printing info is now two things; printing vehicle and model info


# Solution

* Look at the information stored & where it's accessed from.

* Start to group the code around the information, that will lead to lower coupling as it's more closer to the information it uses. 
* The methods will have higher cohesion as they can only do one thing with that particular information.

* As Craig Larman in his book (Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and Iterative Development) where the information of your application is centred. You should look for information expert he stated.

* We've to separate the brand info and vehicle info from each other 

* Seprated print in two different classes where it's more closer to the info they're printing to reduce coupling and increse cohesion

* Adding new models just require one change in one place

* The code now is more maintainable and extendable

* The changes 