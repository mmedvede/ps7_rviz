Particle array visualization using rviz.
========================================

See ./example/randomposes.py for python example. C++ is similar.
The hardest part is to assemble the PoseArray message. Rviz is able to
visualize it as an arrows.

The visualization.launch file also starts mapserver which publishes the map.


Running an example
------------------

    roslaunch ps7_rviz visualization.launch

In separate terminal:

    rosrun ps7_rviz randomposes.py

