# Repeitier_CuraEngine_Speed_Fan_PWM_mod
Permet de contourner le bug de vitesse max du ventilateur d'extrusion sous Repetier avec CuraEngine.

Script initial de Crazymakers corrigé et adapté pour python 3
https://www.youtube.com/watch?v=MD7B-xMdRAU

Installation (à adapter)
Copier le fichier gcode.py dans "C:\Program Files\Python39\"
modifier Repetier:
#Dans Repetier, Configuration, Réglage imprimante, Avancée
#"C:\Program Files\Python39\python.exe" "C:\Program Files\Python39\gcode.py" #in #out
