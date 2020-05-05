#!/bin/bash
# conkyaddrm, fork of conkytoggleflux.sh (Kerry and anticapitalista,
# secipolla for antiX
################################################################################

main()
{
  test=$(grep -q "conky -c" $HOME/.conky/conky-startup.sh && echo $?)
  if [ "$test" = "0" ]; then
       launch_conky
       autostart_on

  else
    killall conky 
    autostart_off
  fi

}

launch_conky()
{    
SLEEP=$(grep sleep $HOME/.conky/conky-startup.sh|cut -d\   -f2)
echo $SLEEP
sed -i s/sleep.*/sleep\ 1s/ $HOME/.conky/conky-startup.sh
echo $SLEEP
killall conky
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
