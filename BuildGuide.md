# Micromouse Build Guide

## Materials and Tools

## 3D Printing

## Assembly

### Adding Holes to Body

First we will solder the two boards, raspberry pi pico and BNO055, to our breadboard. Fit the pins through the boards, then push them onto the bread board. Make sure the long end of the pin
sticks all the way into the breadboard and the short end sticks through the top of the boards. There are plenty of resources on how to solder pins, we will link some here

https://youtu.be/VxMV6wGS3NY?t=66

https://youtu.be/3230nCz3XQA

Make sure to not do too many pins in one area at once, as the heat can damage the boards. When finished, ensure none of the pins are touching one and other.

_ solder Pins picture_

Now we will shift to preparing the body of the mouse. Some extra holes need to be made for two extra sensors, the battery pack, and the front wheel. We will be using a meatal bolt that is the
same size as the rest of the bolt to make the holes. Using tweezers/plyers, hold the bolt in the position of the hole, and put the soldering iron on top with gentle pressure. After ~30 sec (soldering iron dependent)
the plastic should melt the bolt can be gently pushed in. 

We will be adding two sensors sticking out the side of the body. These are mounted onto the bottom post that hold the front facing sensor. Position the sensors they rest on the bottom of the body. In the pictures the sensors are in the wrong place.  Place the other sensors
in their position to make sure there is no interference. Once the positions have been marked, we can use the hot bolt method to make out holes. The bolt does not need to be pushed all the way though, just about the depth of the bolt used to hold the sensor, about half a centimeter. 
See the video and pictures below. 

_Making holes for sensors_


Position the battery pack as shown below. Ensure that there is room for the front wheel riser on the bottom as well. The battery pack should not overhang the back too much, as it may run into the motor controller which will hang off the back of the body.

_Battery pack positioning with front wheel riser, screenshot from vid_

Once the battery pack is in the correct position, mark one of the inner two holes and use the hot bolt method to make a hole. It should go all the way through the base.

_Picture of the hole_


### Gluing

Several parts and screws are held down using hot glue. The first thing we will down is the battery pack. Add hot glue on the bottom of the body and filling the hole for the screw, then **quickly** place the battery pack and the screw. Make sure the screw and battery pack are pressed down firmly. Avoid squeezing glue into other holes, as it will block other bolts later. If needed, place a bolt in the unused hole to ensure no glue seeps in.

_Pictures/vid of gluing battery pack_

Now we will move on to the motors and motor mounts. Press the motors into the 3D printed mount. Do at test fit, placing the motor and mount in position with the three screws. I the holes do no line up for some reason, use the hot screw method again. Make sure the motor sits flat on the body and not allowed to move in the mount. Once you are sure of the fit, without moving the mount add hot glue to a hole and screw in a bolt. Make sure the press the screw into position as the glue hardens. Repeat for the rest of the holes. Stress test your connections as you go, try to pull the motor out and make sure it is secure.

_Video of mounting the motor_

Next we will glue the riser for the front wheel. Add hot glue to the bottom of the mouse and press the riser on firmly. Make sure to put bolts in the holes for the sensors.

_Video of glueing riser_

While we are working on the riser, we will make the final pair of holes. Place the wheel on its riser and mark the two hole positions. With the same method as before, make two holes to attach the wheel to the riser.

_Adding front wheel holes_

Now we can finally glue the front wheel on. As before add glue to the riser and fill the holes, then firmly press on wheel with bolts.

_Glueing Front wheel_

### Final Assembly

Push the wheels onto the motors, careful to not rip them out of the mounts. The mouse should now be stable when sitting on a flat surface.

_Pic of mouse on table_

Attach the motor driver to the back. Use a stand-off, bolt and nut. Push the bolt through the body, then attach the standoff. Finally hang the motor controller off the bolts and secure with nuts.

_Attaching motor controller_

Plug in the included wires into the motors. Attach the sensors in each of the five positions, follow the order below. Plug in the wires as you go, some of the sensor pins need to be bent to stick strait up. Route the sensor wires to stick out the front and the motor wires to stick out the back. Place the bread board on top of all the components.

_Picture of assembled Mouse_
