                       The Global Airport Database
                         Release Version 0.0.2

Author: Arash Partow

Copyright notice:
Free use of the Global Airport Database is permitted under the
guidelines and in accordance with the most current version of
the MIT License.
http://www.opensource.org/licenses/MIT


[INTRODUCTION]
The Global Airport Database (GADB) is a FREE downloadable database  of
9300 airports big and small from all around the world. The database is
presented in a simple token delimited format.


For more information please visit:

http://www.partow.net/miscellaneous/airportdatabase/index.html


---

eg. EGLL:LHR:HEATHROW:LONDON:ENGLAND:051:028:039:N:000:027:041:W:00025:51.477:-0.461

00	EGLL        ICAO Code	                String  (3-4 chars, A - Z)
01	LHR         IATA Code	                String  (3 chars,   A - Z)
02	HEATHROW    Airport Name	            String
03	LONDON      City/Town	                String
04	ENGLAND     Country	                    String

05	051         Latitude Degrees	        Integer [0, 360]
06	028         Latitude Minutes	        Integer [0,  60]
07	039         Latitude Seconds	        Integer [0,  60]
08	N           Latitude Direction	        Char    (N or S)

09	000         Longitude Degrees	        Integer [0, 360]
10	027         Longitude Minutes	        Integer [0,  60]
11	041         Longitude Seconds	        Integer [0,  60]
12	W           Longitude Direction	        Char    (E or W)

13	00025       Altitude	                Integer [-99999,+99999]     (Altitude in meters from mean sea level)

14	51.477      Latitude Decimal Degrees	Float   [- 90, 90]
15	-0.461      Longitude Decimal Degrees	Float   [-180,180]