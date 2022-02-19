if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }


$processes = "PDStyleAgent", "AdobeIPCBroker", "CCXProcess", "RichVideo64", "CCLibrary", "AdobeNotificationClient", "AdobeUpdateService", "PDHanumanSvr", "PDR"

Foreach ($process in $processes){
    try {
    $f = Get-Process $process -ErrorAction Stop
    $f | kill
    Write-Host "$process killed." -f red
        } 
    catch [Microsoft.PowerShell.Commands.ProcessCommandException]{
    Write-Host "No instances of $process running." -f green
        }   
}

Start-Sleep -Seconds 5
