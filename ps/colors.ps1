# Created using
# https://www.petri.com/change-powershell-console-font-and-background-colors

# Useful SO question:
# https://stackoverflow.com/questions/33859498/how-can-i-reset-the-powershell-colors

# microsoft docs on the topic:
# https://docs.microsoft.com/en-gb/powershell/module/PSReadline/Set-PSReadlineOption?view=powershell-5.1

$currentTime = Get-Date -Format yyyymmddHHmmssfff

Function Get-ConsoleColor {
    Param(
        [switch]$Colorize
    )
 
    $wsh = New-Object -ComObject wscript.shell
  
    $data = [enum]::GetNames([consolecolor])
   
    if ($Colorize) {
        Foreach ($color in $data) {
            Write-Host $color -ForegroundColor $Color
        }
        [void]$wsh.Popup("The current background color is $([console]::BackgroundColor)", 16, "Get-ConsoleColor")
    }
    else {
        #display values
        $data
    }
		      
} #Get-ConsoleColor

Function Show-ConsoleColor {
    Param()
    $host.PrivateData.psobject.properties | 
        Foreach {
        #$text = "$($_.Name) = $($_.Value)"
        Write-host "$($_.name.padright(23)) = " -NoNewline
        Write-Host $_.Value -ForegroundColor $_.value
    }
} #Show-ConsoleColor

Function Test-ConsoleColor {
    [cmdletbinding()]
    Param()
 
    #Clear-Host
    $heading = "White"
    Write-Host "Pipeline Output" -ForegroundColor $heading
    Get-Service | Select -first 5
 
    Write-Host "`nError" -ForegroundColor $heading
    Write-Error "I made a mistake"
 
    Write-Host "`nWarning" -ForegroundColor $heading
    Write-Warning "Let this be a warning to you."
 
    Write-Host "`nVerbose" -ForegroundColor $heading
    $VerbosePreference = "Continue"
    Write-Verbose "I have a lot to say."
    $VerbosePreference = "SilentlyContinue"
 
    Write-Host "`nDebug" -ForegroundColor $heading
    $DebugPreference = "Continue"
    Write-Debug "`nSomething is bugging me. Figure it out."
    $DebugPreference = "SilentlyContinue"
 
    Write-Host "`nProgress" -ForegroundColor $heading
    1..10 | foreach -Begin {$i = 0} -process {
        $i++
        $p = ($i / 10) * 100
        Write-Progress -Activity "Progress Test" -Status "Working" -CurrentOperation $_ -PercentComplete $p
        Start-Sleep -Milliseconds 250
    }
} #Test-ConsoleColor

Function Export-ConsoleColor {
 
    [cmdletbinding(SupportsShouldProcess)]
    Param(
        [Parameter(Position = 0)]
        [ValidateNotNullorEmpty()]
        [string]$Path = '.\PSConsoleSettings.csv'
    )
 
    #verify this is the console and not the ISE
    if ($host.name -eq 'ConsoleHost') {
        $host.PrivateData | Add-Member -MemberType NoteProperty -Name ForegroundColor -Value $host.ui.rawui.ForegroundColor -Force
        $host.PrivateData | Add-Member -MemberType NoteProperty -Name BackgroundColor -Value $host.ui.rawui.BackgroundColor -Force
        Write-Verbose "Exporting to $path"
        Write-verbose ($host.PrivateData | out-string)

        $timedPath = $Path -replace ".csv$", "-$currentTime.csv"
        Write-Output "Saved ps colour settings in: $timedPath"

        $host.PrivateData | Export-CSV -Path $timedPath -Encoding ASCII -NoTypeInformation
    }
    else {
        Write-Warning "This only works in the console host, not the ISE."
 
    }
} #Export-ConsoleColor

Function Import-ConsoleColor {
    [cmdletbinding(SupportsShouldProcess)]
    Param(
        [Parameter(Position = 0)]
        [ValidateScript( {Test-Path $_})]
        [string]$Path = '.\PSConsoleSettings.csv'
    )
 
    #verify this is the console and not the ISE
    if ($host.name -eq 'ConsoleHost') {
        Write-Verbose "Importing color settings from $path"
        $data = Import-CSV -Path $Path
        Write-Verbose ($data | out-string)
 
        if ($PSCmdlet.ShouldProcess($Path)) {
            $host.ui.RawUI.ForegroundColor = $data.ForegroundColor
            $host.ui.RawUI.BackgroundColor = $data.BackgroundColor
            $host.PrivateData.ErrorForegroundColor = $data.ErrorForegroundColor
            $host.PrivateData.ErrorBackgroundColor = $data.ErrorBackgroundColor
            $host.PrivateData.WarningForegroundColor = $data.WarningForegroundColor
            $host.PrivateData.WarningBackgroundColor = $data.WarningBackgroundColor
            $host.PrivateData.DebugForegroundColor = $data.DebugForegroundColor
            $host.PrivateData.DebugBackgroundColor = $data.DebugBackgroundColor
            $host.PrivateData.VerboseForegroundColor = $data.VerboseForegroundColor
            $host.PrivateData.VerboseBackgroundColor = $data.VerboseBackgroundColor
            $host.PrivateData.ProgressForegroundColor = $data.ProgressForegroundColor
            $host.PrivateData.ProgressBackgroundColor = $data.ProgressBackgroundColor
 
            #Clear-Host
        } #should process
 
    }
    else {
        Write-Warning "This only works in the console host, not the ISE."
    }
 
} #Import-ConsoleColor

# https://social.technet.microsoft.com/Forums/en-US/7c87371d-5a9c-4463-9290-73e339f82b4e/how-do-i-change-the-text-colors-in-a-powershell-command-window?forum=win10itprogeneral
Function Set-ConsoleTokenColorLight {
    Set-PSReadlineOption -TokenKind comment -ForegroundColor black
    Set-PSReadlineOption -TokenKind none -ForegroundColor black
    Set-PSReadlineOption -TokenKind command -ForegroundColor black
    Set-PSReadlineOption -TokenKind parameter -ForegroundColor black
    Set-PSReadlineOption -TokenKind variable -ForegroundColor black
    Set-PSReadlineOption -TokenKind type -ForegroundColor black
    Set-PSReadlineOption -TokenKind number -ForegroundColor black
    Set-PSReadlineOption -TokenKind string -ForegroundColor black
    Set-PSReadlineOption -TokenKind operator -ForegroundColor black
    Set-PSReadlineOption -TokenKind member -ForegroundColor black

    Set-PSReadlineOption -TokenKind comment -BackgroundColor white
    Set-PSReadlineOption -TokenKind none -BackgroundColor white
    Set-PSReadlineOption -TokenKind command -BackgroundColor white
    Set-PSReadlineOption -TokenKind parameter -BackgroundColor white
    Set-PSReadlineOption -TokenKind variable -BackgroundColor white
    Set-PSReadlineOption -TokenKind type -BackgroundColor white
    Set-PSReadlineOption -TokenKind number -BackgroundColor white
    Set-PSReadlineOption -TokenKind string -BackgroundColor white
    Set-PSReadlineOption -TokenKind operator -BackgroundColor white
    Set-PSReadlineOption -TokenKind member -BackgroundColor white  
}

[console]::ForegroundColor = "Green"
[console]::BackgroundColor = "black"


#Get-ConsoleColor
#Show-ConsoleColor
#Test-ConsoleColor
#Export-ConsoleColor -Path c:\dev\console-color.csv

#Write-Output $currentTime

#Get-PSReadlineOption

# dark theme
# Import-ConsoleColor -Path ./psdark.csv
# Set-PSReadlineOption -ResetTokenColors 

# light theme
Import-ConsoleColor -Path ./pslight.csv
Set-ConsoleTokenColorLight
#Get-PSReadlineOption

Clear-Host
Write-Output "Useful Cmdlets: Get-PSReadlineOption"
