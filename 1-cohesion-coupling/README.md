# Code Analaysis
<br>
This method register_vehicle() is an example of (A)weak cohesion and (B)high coupling.<br>
    (A)<br>
        *Weak cohesion as it does a lot of different things (6) with no clear single responsibility.<br>
        *It's hard to add a new car brand, as we have to add new if condition with the car brand and we will add it too in checking if electric or not
        Comment: This one could be easily solved if we get the car from DB table, we won't need all this hassle. <br>
    (B)<br>
        *High coupling as it directly depends on the implementation details of VechileRegistry class.<br>
        If anything changed in VechileRegistery class, I have to change register_vechile method in CarApplication class.<br>
