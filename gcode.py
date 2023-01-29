# coding: utf-8
#!/usr/bin/python

#
#Dans Repetier, Configuration, Réglage imprimante, Avancée
#"C:\Program Files\Python39\python.exe" "C:\Program Files\Python39\gcode.py" #in #out

import sys,re,os,tkinter.simpledialog,tkinter
root = tkinter.Tk()
root.withdraw()
SET_MAX_FAN_SPEED = tkinter.simpledialog.askinteger("Vitesse maximale du Ventilateur d'extrudeur:", "Veuillez indiquer la vitesse maximale du\nventilateur d'extrudeur (0-100%)" , initialvalue="100")
MAX_FAN_SPEED_PWM=SET_MAX_FAN_SPEED*2.55
FAN_COEFF=MAX_FAN_SPEED_PWM/76


NUM_LIGNE=0
FAN_SPEED=0
infile = sys.argv[1]
outfile = sys.argv[2]
#infile=r"C:\Users\XXXXXXXX\AppData\Local\RepetierHost\filter.gcode"
#outfile=r"C:\Users\XXXXXXXX\AppData\Local\RepetierHost\composition.gcode"

infile = open(infile, "r+")
CONTENU=infile.readlines()
for i in range (len(CONTENU)):
    if 'M106 S' in CONTENU[i]:
        FAN_SPEED=CONTENU[i].replace('M106 S','')
        if int(FAN_SPEED)>76:
            FAN_SPEED=round(int(MAX_FAN_SPEED_PWM))
        else:
            FAN_SPEED=round(int(FAN_SPEED)*FAN_COEFF)
        CONTENU[i]='M106 S'+str(FAN_SPEED)+"\n"
        DERNIERE_LIGNE=NUM_LIGNE+1
    NUM_LIGNE=NUM_LIGNE+1
outfile = open(outfile, "w+")
for i in range (len(CONTENU)):
        outfile.write(CONTENU[i])
print("post-traitement du G-Code pour correction de la vitesse de ventilateur.")
print("Vitesse maximale ("+str(SET_MAX_FAN_SPEED)+"%) du ventilateur atteinte a la ligne "+str(DERNIERE_LIGNE)+".")



