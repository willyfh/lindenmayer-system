How to use the program
-----------------------

1. Execute the program from the console
	> py lindenmayer_system.py
	
2. The program will be running, and the resulting string (L-Systems) will be displayed at the console.


Output
---------------------
**Lindenmayer 1**

step= 0 ,        C

step= 1 ,        A

step= 2 ,        CA

step= 3 ,        ACA

step= 4 ,        CAACA

step= 5 ,        ACACAACA

**Lindenmayer 2**

step= 0 ,        R

step= 1 ,        RS

step= 2 ,        RSST

step= 3 ,        RSSTSTTR

step= 4 ,        RSSTSTTRSTTRTRRS

step= 5 ,        RSSTSTTRSTTRTRRSSTTRTRRSTRRSRSST

**Sample with Constants**

step= 0 ,        B

step= 1 ,        F[-B]+B

step= 2 ,        FF[-F[-B]+B]+F[-B]+B

step= 3 ,        FFFF[-FF[-F[-B]+B]+F[-B]+B]+FF[-F[-B]+B]+F[-B]+B