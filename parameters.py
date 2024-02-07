from random import randint
PORT = str(randint(1000, 9999))
URL_0D = "http://127.0.0.1:"+PORT+"/satvision/sketchs/base"  
URL_3D = "http://127.0.0.1:"+PORT+"/satvision/sketchs/3_d"
URL_2D = "http://127.0.0.1:"+PORT+"/satvision/sketchs/2_d"
URL_CELESTRAK = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"
g0 = 9.80665 #m/s
Omega_e = 6.300387486749 # rad/d
R_e = 6378.137 #km
GM_e = 3.986005e5 #km^3/s^2