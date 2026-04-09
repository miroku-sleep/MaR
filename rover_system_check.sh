#!/bin/bash

battery=$(( RANDOM%101 )) #dividing any number by 101 gives 0-100 as remainder
if [ $battery -lt 20 ]; then 
echo "Battery low! return to base!"
exit 1
fi

ping -c 1 google.com &> /dev/null

if [ $? -ne 0 ]; then #$? stores the ping value
echo "communnication failure!"
exit 1
fi

echo "All systems operational!"
