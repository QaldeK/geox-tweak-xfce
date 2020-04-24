#!/bin/bash

cky=$1
conky=$2
ckstart="$HOME/.conky/conky-startup.sh"

main() {
	SLEEP=$(grep sleep $HOME/.conky/conky-startup.sh|cut -d\   -f2)
	echo $SLEEP
	sed -i s/sleep.*/sleep\ 1s/ $HOME/.conky/conky-startup.sh

	test=$(grep -q $conky $HOME/.conky/conky-startup.sh && echo $?)
	if [ "$test" = "0" ]; then
	     stop_conky
	else
		start_conky 
	fi
}

stop_conky() {

	awk -vLine="$cky" '!index($0,Line)' $ckstart
	sh $HOME/.conky/conky-startup.sh &

	sed -i s/sleep.*/sleep\ $SLEEP/ $HOME/.conky/conky-startup.sh

}


start_conky() {

	echo $cky >> $ckstart

	sh $HOME/.conky/conky-startup.sh &

	sed -i s/sleep.*/sleep\ $SLEEP/ $HOME/.conky/conky-startup.sh

}


# test2=$(grep -q "conky -c" $HOME/.conky/conky-startup.sh && echo $?)

# if [ "$test2" = "0" ]; then
# 	autostart_on
# else
# 	autostart_off
# fi

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