#!/bin/bash

sshpass -p "maker" scp -r rover/ev3/* robot@ev3dev.local:~/rover/ev3
