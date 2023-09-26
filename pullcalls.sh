#!/bin/bash

location=/storage/self/primary/MIUI/sound_recorder/call_rec/;
destination=~/Desktop/Calls/;
callsfile=$destination'calls.txt';
todaysdate=$(date --date='TZ="Asia/Karachi" now' +%Y%m%d);

cd $destination;

adb start-server

adb shell ls $location > $callsfile
adb devices -l

if [[ -r lastdate.txt ]]
then

    lastdate=$(date -d $( cat lastdate.txt ));
    lastdateepoch=$(date -d $( cat lastdate.txt ) +%s );
else
    lastdate=$(date --d "20000101");
fi

echo Last Date: $lastdate
echo Last Date Epoch: $lastdateepoch

c=1;
while read -r callinfo; do


    numberdate=$( echo $callinfo | cut -d '_' -f2 | cut -c 1-8 );
#     echo $numberdate
    dateobj=$( date -d $numberdate +%s);

    if [[ $lastdateepoch < $dateobj ]]
    then
        echo $c: Copying: $callinfo
        echo
        ((c++));
            adb pull "${location}${callinfo}"
#     else
#         echo Noooo...
    fi

done <$callsfile

echo $todaysdate > lastdate.txt
