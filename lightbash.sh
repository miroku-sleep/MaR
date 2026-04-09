#!/bin/bash

# 1. Create a directory
mkdir  rover_mission
cd rover_mission

# 2. Create three empty files
touch log1.txt log2.txt log3.txt

# 3. Rename log1 to mission_log
mv log1.txt mission_log.txt

# 4. Search for any .log files 
#(This will be empty initially as we created only .txt files)
find . -maxdepth 1 -name "*.log"

# 5. Display content of the log (will be empty too)
cat mission_log.txt

# 6. Find and display all lines containing the word "ERROR" in mission_log.txt.(0)
grep "ERROR" mission_log.txt

# 7. Count the number of lines in the log file
wc -l < mission_log.txt

# 8. Display current system date and process status 
date

# 9. Display the CPU usage of your system in real time
top -n 1 -b | head -n 20

#10. Schedule a system shutdown
sudo shutdown +10 "see you later" 
