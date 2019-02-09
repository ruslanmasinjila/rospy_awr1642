LINKS: 
<br/>
AWR1642: <https://bit.ly/2swR75V> 
<br/>
TI mmwave ROS Driver Setup Guide: <https://bit.ly/2tdHRnt>
<br/>
<br/>
INSTRUCTIONS:
<br/>
1. Add the following alias to .bash_aliases to launch all nodes at once:
<br/>
alias awr1642='roslaunch awr1642 awr1642.launch & roslaunch ti_mmwave_rospkg rviz_1642_2d.launch'
<br/>
<br/>
NODES:
<br/>
	/awr1642
	/mmWave_Manager
	/rosout
	/rviz
	/static_tf_map_to_base_radar_link
<br/>
	TOPICS:
		/clicked_point
		/initialpose
		/mmWaveDataHdl/RScan
		/move_base_simple/goal
		/rosout
		/rosout_agg
		/tf
		/tf_static


