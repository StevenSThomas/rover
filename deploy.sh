#!/bin/bash

sshpass -p "maker" scp -r rover/robotController/* robot@ev3dev.local:~/rover/robotController
