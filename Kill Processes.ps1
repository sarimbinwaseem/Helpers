$f = Get-Process -Name PDStyleAgent
if ($f.Id -gt 0){
$f | kill
Write-Host "PD Killed"}
else{Write_Host "PD Not Running"}

$f = Get-Process -Name AdobeIPCBroker
if ($f.Id -gt 0){
$f | kill
Write-Host "Adobe IPC Killed"}
else{Write_Host "IPC Not Running"}

$f = Get-Process -Name CCXProcess
if ($f.Id -gt 0){
$f | kill
Write-Host "CCX Killed"}
else{Write_Host " CCX Not Running"}

$f = Get-Process -Name RichVideo64
if ($f.Id -gt 0){
$f | kill
Write-Host "Rich Video"}
else{Write_Host " RichVideo Not Running"}

$f = Get-Process -Name CCLibrary
if ($f.Id -gt 0){
$f | kill
Write-Host "CC Library"}
else{Write_Host " RichVideo Not Running"}

Start-Sleep -Seconds 2