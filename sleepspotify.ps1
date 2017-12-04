# This is a script to stop spotify late at night after going to sleep

# Choose the time to stop spotify
$bedtime = Read-Host -Prompt "What time do you wish to close Spotify? (HH:MM)"

# Create a task to kill spotify at a certain time
schtasks.exe /create /TN sleepspotify /sc once /ST $bedtime /tr "taskkill /im Spotify.exe"

# Print out the list of tasks to double check it has worked
schtasks.exe /query | grep -A 4 -B 4 spot

# Give user time to read the output
 Read-Host -Prompt "Press enter to quit"
 