#!/bin/bash
# Filename:      conkytoggleflux.sh
# Purpose:       toggle conky on/off from fluxbox menu
# Authors:       Kerry and anticapitalista, secipolla for antiX
# Authors:       modified for mx linux version 17 by dolphin oracle
# Latest change: Sun December 10, 2017.
################################################################################

main()
{
if pidof conky | grep [0-9] > /dev/null
 then
  killall conky 
  autostart_off
 else
    test=$(grep -q "conky -c" $HOME/.conky/conky-startup.sh && echo $?)
    if [ "$test" = "0" ]; then
         launch_conky
         autostart_on
    else
    conky-manager &
    fi
fi
}

launch_conky()
{    
SLEEP=$(grep sleep $HOME/.conky/conky-startup.sh|cut -d\   -f2)
echo $SLEEP
sed -i s/sleep.*/sleep\ 1s/ $HOME/.conky/conky-startup.sh

sh $HOME/.conky/conky-startup.sh &

sed -i s/sleep.*/sleep\ $SLEEP/ $HOME/.conky/conky-startup.sh
}

autostart_off()
{
    
if [ -e $HOME/.config/autostart/conky.desktop ]; then 
    sed -i -r s/Hidden=.*/Hidden=true/ $HOME/.config/autostart/conky.desktop
fi

}

autostart_on()
{
    
if [ -e $HOME/.config/autostart/conky.desktop ]; then 
    sed -i -r s/Hidden=.*/Hidden=false/ $HOME/.config/autostart/conky.desktop
fi

}

main
exit 0
