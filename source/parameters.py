from random import randint
PORT = str(randint(1000, 9999))
URL_0D = "http://127.0.0.1:"+PORT+"/satvision/sketchs/base"  
URL_3D = "http://127.0.0.1:"+PORT+"/satvision/sketchs/3_d"
URL_2D = "http://127.0.0.1:"+PORT+"/satvision/sketchs/2_d"
URL_CELESTRAK = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"
