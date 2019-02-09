LINKS: 
----------
AWR1642: <https://bit.ly/2swR75V> 
TI mmwave ROS Driver Setup Guide: <https://bit.ly/2tdHRnt>

INSTRUCTIONS:
--------------
Add the following alias to .bash_aliases to launch all nodes at once:

alias awr1642='roslaunch awr1642 awr1642.launch & roslaunch ti_mmwave_rospkg rviz_1642_2d.launch'


NODES:
--------
	/awr1642
	/mmWave_Manager
	/rosout
	/rviz
	/static_tf_map_to_base_radar_link

	TOPICS:
	--------
		/clicked_point
		/initialpose
		/mmWaveDataHdl/RScan
		/move_base_simple/goal
		/rosout
		/rosout_agg
		/tf
		/tf_static


TODO:
------
> Create a 0.5m x 0.5m x 0.5m "invisible cube" about 2 meters away from radar for data collection. 
Visually provide some feedback on the presence or absence of objects within the cube.														


