#!/bin/bash

location=/storage/self/primary/MIUI/sound_recorder/call_rec/;
destination=~/Desktop/Calls/;

# Can change Timezone
todaysdate=$(date --date='TZ="Asia/Karachi" now' +%Y%m%d);

# Don't change this
callsfile=$destination'calls.txt';

cd $destination;

adb start-server
adb devices -l
read -p "Press any key when authorized on phone:"

adb shell ls $location > $callsfile


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
        echo
        echo
#     else
#         echo Noooo...
    fi

done <$callsfile

echo $todaysdate > lastdate.txt
