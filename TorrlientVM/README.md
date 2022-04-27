## TorrlientVM
This folder contains the source code for "TorrlientVM", a Virtual Machine intended to make it easier to develop Autonomous Virtual Machine Applications.

The purpose of this script is to execute programs only once at reboot, which crontab to my knowledge cannot do. 

We execute this script by name only. To replicate this behaviour use this command: 
```
cp TorrlientVM.py /bin/torrlientvm
```
CLI Options
```
torrlientvm -search
```
```
torrlientvm -init scriptname
```
```
torrlientvm -remove scriptname
```
```
torrlientvm -queue
```
```
torrlientvm -listen
```
```
torrlientvm -run
```

***Note*** This code contain a section with Telemetry that are completely unused. 
