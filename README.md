# WEST-Instrument
Embedded system for playing remote simulated instrument (over WiFi network) developed by WEST Team

Hardware:  STM32F407VG Discovery kit, USART cp2102

Software:  STM32CubeMX, STM32CubeIDE
# 

#   /project

U STM32CubeIDE kao workspace zadaj mapu project, otvori projekte preko open project from directory

    test3           -> blinky sa timerom 

    wes-usart       -> sustav čita char znakove preko usart bridge-a i ponovo ih vraća

    audio-example   -> generiranje šuma na izlazu za zvuk

#   /python-scripts   
    
    keylogger.py    -> za događaje "pritisnuta tika na tipkovnici" i "puštena tipka na tipkovnici" 
                       šalje poruku o pritisnutoj i puštenoj tipki na USB port
    
    keylogger.sh    -> za pokretanje keylogger.py na Linux-u
    
    Wave_generator  -> računanje lookup tablice za sinusne signale
