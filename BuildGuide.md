# Micromouse Build Guide

## Materials and Tools

1 Raspberry Pi Pico

1 Adafruit BNO055

1 Breadboard

2 stepper motors

1 Motor Controller

1 AA battery pack

5 proximety sensors

2 wheels

1 Marble front wheel

Wire

Nuts and Bolts


Soddering Iron and Soder

Wire Strippers

Screwdriver

Hot Glue Gun




## 3D Printing

## Assembly

### Adding Holes to Body

First we will solder the two boards, raspberry pi pico and BNO055, to our breadboard. Fit the pins through the boards, then push them onto the bread board. Make sure the long end of the pin sticks all the way into the breadboard and the short end sticks through the top of the boards. There are plenty of resources on how to solder pins, we will link some here

https://youtu.be/VxMV6wGS3NY?t=66

https://youtu.be/3230nCz3XQA

Make sure to not do too many pins in one area at once, as the heat can damage the boards. When finished, ensure none of the pins are touching one and other.

![](https://drive.google.com/uc?export=view&id=19VUmnpGrQMH44aSw0LhqlAt_P_vNcfS1)
_In this photo, the BNO055 board is the wrong way around, later pictures show correct positioning_

Now we will shift to preparing the body of the mouse. Some extra holes need to be made for two extra sensors, the battery pack, and the front wheel. We will be using a meatal bolt that is the
same size as the rest of the bolt to make the holes. Using tweezers/plyers, hold the bolt in the position of the hole, and put the soldering iron on top with gentle pressure. After ~30 sec (soldering iron dependent)
the plastic should melt the bolt can be gently pushed in. 

We will be adding two sensors sticking out the side of the body. These are mounted onto the bottom post that hold the front facing sensor. Position the sensors they rest on the bottom of the body. In the pictures the sensors are in the wrong place.  Place the other sensors
in their position to make sure there is no interference. Once the positions have been marked, we can use the hot bolt method to make out holes. The bolt does not need to be pushed all the way though, just about the depth of the bolt used to hold the sensor, about half a centimeter. 
See the video and pictures below. 

[Video of making holes for sensors](https://drive.google.com/file/d/19ATOih4IEB0pujOk8rHGE2_MhbnvWNPe/view?usp=sharing)


Position the battery pack as shown below. Ensure that there is room for the front wheel riser on the bottom as well. The battery pack should not overhang the back too much, as it may run into the motor controller which will hang off the back of the body.

![](https://drive.google.com/uc?export=view&id=18_NGns4V_zMAYg9FI1SqnSFjND-s1R_l)

![](https://drive.google.com/uc?export=view&id=18Ungi7RT6A9-nWc5OqpGnNqBDtQ2Qp8Q)
_These photos are from later in the build_

Once the battery pack is in the correct position, mark one of the inner two holes and use the hot bolt method to make a hole. It should go all the way through the base.

![](https://drive.google.com/uc?export=view&id=1982umvpv1W4_adWE7HY-_2t_n6J1h2im)


### Gluing

Several parts and screws are held down using hot glue. The first thing we will down is the battery pack. Add hot glue on the bottom of the body and filling the hole for the screw, then **quickly** place the battery pack and the screw. Make sure the screw and battery pack are pressed down firmly. Avoid squeezing glue into other holes, as it will block other bolts later. If needed, place a bolt in the unused hole to ensure no glue seeps in.

[Video of gluing battery pack and wheel riser](https://drive.google.com/file/d/194cp8UChZ6uAa3yq5Reyt7Vx2YEZrlo1/view?usp=sharing)

Now we will move on to the motors and motor mounts. Press the motors into the 3D printed mount. Do at test fit, placing the motor and mount in position with the three screws. I the holes do no line up for some reason, use the hot screw method again. Make sure the motor sits flat on the body and not allowed to move in the mount. Once you are sure of the fit, without moving the mount add hot glue to a hole and screw in a bolt. Make sure the press the screw into position as the glue hardens. Repeat for the rest of the holes. Stress test your connections as you go, try to pull the motor out and make sure it is secure.

Next we will glue the riser for the front wheel. Add hot glue to the bottom of the mouse and press the riser on firmly. Make sure to put bolts in the holes for the sensors. See video above.

While we are working on the riser, we will make the final pair of holes. Place the wheel on its riser and mark the two hole positions. With the same method as before, make two holes to attach the wheel to the riser.

Now we can finally glue the front wheel on. As before add glue to the riser and fill the holes, then firmly press on wheel with bolts.

_See pictures above for finished underside_

### Final Assembly

Push the wheels onto the motors, careful to not rip them out of the mounts. The mouse should now be stable when sitting on a flat surface.

Attach the motor driver to the back. Use a stand-off, bolt and nut. Push the bolt through the body, then attach the standoff. Finally hang the motor controller off the bolts and secure with nuts.

![](https://drive.google.com/uc?export=view&id=18NLLlD8ht0rcpdyMzZoAGB0ODV9KM1Ru)

![](https://drive.google.com/uc?export=view&id=17mLeJrcFiOVl_M-XIbPsL88aFJMEj-vw)

Plug in the included wires into the motors. Attach the sensors in each of the five positions, follow the order below. Plug in the wires as you go, some of the sensor pins need to be bent to stick strait up. Route the sensor wires to stick out the front and the motor wires to stick out the back, likin in picture below. The only exception in the purple, green and blue sesnor wires coming out the back. That should be routed with the rest of the sensors out the front. If you decide to twist the wires, make sure to mark which is left and right befor hand. Place the bread board on top of all the components.

![](https://drive.google.com/uc?export=view&id=16TwKRqmR6D-hn6E5z7vDTsoDSE2w402d)

## Wiring

Below is a wiring diagram for the micromouse. You can use this and route the wires as you see fit. The only error in the wiring diagram is the encoders for teh motors, teh yellow and green wires. The yellow and green should be flipped, the order should go yellow green green yellow.

![](https://drive.google.com/uc?export=view&id=1pzRai8rGGtg09KoscXExky3qvh6skgD5)

First we will run all the voltage and ground wires on the board. Everything shares a common ground. As seen in the picture below, the left power bus runs at 3V provided by the pico, and the right is 5V taken from the motor controller. 

![](https://drive.google.com/uc?export=view&id=16WRvHdAfsYwCEhHNXd14On4lbiXIG5Qp)


With the bread board in place, run short green and white wires for the SCL and SDA from the BNO055 to pins 20 and 19 respectivly. Next place the encoder wires with the yellow and green fliped from the wiring diagram and the picture below. The right encoder should be pins 1 and 2, and the left encoder pinst 4 and 5. Also plug in the blue and black cables from motors into the 5V rails. 

![](https://drive.google.com/uc?export=view&id=16Qsl-VeQIxkwBld_Qz9MLijhpvSyvk3B)

Next run all the sensor wires. The wiring diagram shows how they should be connected and what order. Run four more wires to connect the motor controller to the pico. Then run the wires to the motor controller. Be careful when unscreing the wire holder, as the screw will strip very easitly. 

![](https://drive.google.com/uc?export=view&id=16F1qy9ZgYmh_aKV9ryn_UTAJyWjUAnvf)

![](https://drive.google.com/uc?export=view&id=166pFO1wkkjoJGEHYvktakMn4yjAlVE-4)

![](https://drive.google.com/uc?export=view&id=16PFqQpktVyI33SfUr6fUxsdJxnkLMPrD)
   
[Link for more build photos and videos](https://drive.google.com/drive/folders/1XMsHvihriH0pR1_bTGnOD59lvcFpvU8G?usp=sharing)
