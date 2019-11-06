#!/bin/bash

# Verification de la presence et installation des logiciels d'optimisation de XFCE

dir=$(dirname "$0")  # 'dirname $0' renvoie le nom du répertoire dans lequel le script actuel se trouve.

#Check lla distribution linux
if [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    os=$DISTRIB_ID
    ver=$DISTRIB_RELEASE
fi

distrib=$os$ver

which yad > /dev/null
if [ $? = 1 ];
then
	x-terminal-emulator -e "echo Install yad \
			sudo apt-get install -y yad"
fi



mainFunction () {
	pw=$(yad --entry --title="Password required" --text="Please enter user password" --hide-text)

	if [[ $? == 1 ]] ; then exit 
		fi	

	title="${1}"
	command="${2}"
	log="/tmp/$(date +%s)"
	config="--progress --pulsate --center --no-buttons --auto-close
	--progress-text='Installation ...' --width=600"

	${command} 2> "${log}" |
	while read -r line; do echo "# ${line}"; done |
	yad ${config} --title="$title"

	checkErrorLog "${log}"
}


checkErrorLog () {
    log="${1}"
    error=$(cat "${log}")
    rm "${log}"
    dirconf="/usr/share/geox-tweak/"
    find $dirconf -iname '*activ*' -exec sed -i 's/sxcdp = .*/\sxcdp = ok/' {} \;


    if [ "${error}" != "" ]; then
        echo "${error}" >&2
        errorWindow "${error}"
        exit 1
    else yad --title="finish" --text=" installation ok " --button=OK:1
    fi


}


errorWindow () {
    error="${1}"
    config="--center --button=OK:1"

    yad ${config} --title="Error" --text="${error}"  --width 800 --height 500
}


installation() 
{ 
	
	if [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    os=$DISTRIB_ID
    ver=$DISTRIB_RELEASE
	fi

	distrib=$os$ver


		#update
		#echo $pw | sudo -S apt-get update	
		
		#plank
		which plank > /dev/null
		if [ $? = 1 ]
		then
			echo $pw | sudo -S apt-get install -y plank 

		fi
		
		#Xfdashboard
		which xfdashboard > /dev/null
		if [ $? = 1 ]
		then
			echo $pw | sudo -S apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins
		fi
				
		#Synapse
		which synapse > /dev/null
		if [ $? = 1 ]
		then
			echo $pw | sudo -S apt-get install -y synapse
		fi
		
		
		#Redshift
		which redshift > /dev/null
		if [ $? = 1 ]
		then
			echo $pw | sudo -S apt-get install -y redshift
			echo $pw | sudo -S apt-get install -y redshift-gtk
		fi

		#Conky
		which conky > /dev/null
		if [ $? = 1 ]
		then
			echo $pw | sudo -S apt-get install -y conky-all
			echo $pw | sudo -S apt-get install -y conky-manager
		fi 
		
		#Dockbarx & xfce4-dockbarx-plugin
		which dockx >/dev/null
		if [ $? = 1 ] ;
		then
			#for mx 19
			if [ $distrib == "MX19" ] ; then
			echo $pw | sudo -S sh -c "echo 'deb
			http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >
			/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
			echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd 
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 
			
			#for ubuntu and derivative
			elif [ $distrib == "MX18" ] ; then
			echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 

			elif [ $os == "Ubuntu" ] ; then
			echo $pw | sudo -S add-apt-repository ppa:xuzhen666/dockbarx
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 
			
			elif [ $os == "LinuxMint" ] ; then
			echo $pw | sudo -S add-apt-repository ppa:xuzhen666/dockbarx
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 
			
			fi	
		fi
	### THEME ###
	# Arc
	#echo $pw | sudo -S apt-get install -y arc-theme arc-theme-hdpi arc-theme-xhdpi arc-grey-theme
	# Adapta
	#echo $pw | sudo -S apt-get install -y adapta-gtk-theme adapta-gtk-theme-colorpack
	
	
		# Papirus icon
	#test -d "/usr/share/icons/Papirus" 
			
		#if [ $? = 1 ] ; 
		if [ ! -d "/usr/share/icons/Papirus"  ]
			# Install : Papirus-icon-theme
			then
				if [ $distrib = "MX19" ] ; then
					echo $pw | sudo -S apt-get install papirus-icon-theme
				elif [ $distrib = "MX18" ] ; then
					echo $pw | sudo -S apt-get install papirus-icon-theme
				elif [ $os = "LinuxMint" ]; then
					 echo $pw | sudo -S add-apt-repository ppa:papirus/papirus ; $pw | sudo -S apt-get update ; $pw | sudo -S apt-get install papirus-icon-theme
				elif [ $os = "Ubuntu" ]; then
					 echo $pw | sudo -S add-apt-repository ppa:papirus/papirus ; $pw | sudo -S apt-get update ; $pw | sudo -S apt-get install papirus-icon-theme
				else echo $pw | sudo -S wget -qO- https://git.io/papirus-icon-theme-install | sh
				fi
		fi		
		
		#test -e "/usr/bin/papirus-folders"
		#if [ $? = 1 ] ; 
		if [ ! -e "/usr/bin/papirus-folders" ]
			#Install : papirus-folders
			then 
				if [ $distrib = "MX18" ] ; then
					echo $pw | sudo -S apt-get install papirus-folders
				elif [ $distrib = "MX19" ]; then
					echo $pw | sudo -S apt-get install papirus-folders
				elif [ $os = "Ubuntu" ]; then
					echo $pw | sudo -S add-apt-repository ppa:papirus/papirus
					apt-get update 
					sudo apt-get install
				else 
					echo $pw | sudo -S wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-folders/master/install.sh | sh
				fi
		fi
		
	# copie des themes
	#echo $pw | sudo -S tar -zxfk theme.tar.gz -C /usr/share/themes/
	
}


#Interface graphique YAD
yadgui() {

 GUI=$(yad --width=500 --heigth=600 \
		--text="Some packages are required by GeoX-Tweak-Xfce to work properly.	Do you want to proceed installation ? "
	)
	if [[ $? == 1 ]] ; then
	   exit
	else [[ $? == 0 ]]
	mainFunction "Installation" installation
	fi
	
}

yadgui && exit



