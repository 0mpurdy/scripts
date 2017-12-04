# Create a task to kill spotify at a certain time
schtasks.exe /create /TN sleepspotify /sc once /ST 00:15 /tr "taskkill /im Spotify.exe"

# Print out the list of tasks to double check it has worked
schtasks.exe /query | grep -A 4 -B 4 spot

# Give user time to read the output
 Read-Host -Prompt "Press enter to quit"
 