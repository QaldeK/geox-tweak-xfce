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
echo $os $ver

which yad > /dev/null
if [ $? = 1 ];
then
	echo "Install yad"
	x-terminal-emulator -e "echo Install yad \
			sudo apt-get install -y yad"
else
	echo "yad OK"
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
    else 
 		yad --title="finish" --text=" installation ok " --button=OK:1
    	find $HOME/.config/geox-tweak-xfce -iname 'geox-tweak.conf' -exec sed -i 's/sxcdp.*/\sxcdp = ok/' {} \;
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
			if [ $distrib = "MX19" ] || [ $distrib = "MX18" ]  ; then
			echo $pw | sudo -S apt-get install -y plank 

			elif [ $os = "LinuxMint" ] || [ $os = "Ubuntu" ]; then
			echo $pw | sudo -S add-apt-repository -y ppa:ricotz/docky
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y plank
			fi
		fi

		#Xfdashboard
		which xfdashboard > /dev/null
		if [ $? = 1 ]
		then
			if [ $distrib = "MX19" ] ; then
			echo $pw | sudo -S sed -e "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list^C
			echo $pw | sudo -S apt-get update ; apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins
			echo $pw | sudo -S sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list
			elif [ $distrib = "MX18" ] ; then
			echo $pw | sudo -S apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins
			elif [ $os = "LinuxMint" ] || [ $os = "Ubuntu" ] ; then
			sudo add-apt-repository ppa:xubuntu-dev/extras
			sudo apt-get update
			echo $pw | sudo -S apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins	
			fi	
		fi		


		#Synapse
		which synapse > /dev/null
		if [ $? = 1 ]
		then
			echo $pw | sudo -S apt-get install -y synapse
			# sudo add-apt-repository ppa:synapse-core/testing
		fi
		
		

		#Conky
		which conky > /dev/null
		if [ $? = 1 ]
		then

			if [ $os == "MX" ] ; then
				echo $pw | sudo -S apt-get install -y conky-all
				echo $pw | sudo -S apt-get install -y conky-manager

			elif [ $os == "Ubuntu" ] || [ $os == "LinuxMint" ]; then
				wget http://launchpadlibrarian.net/340091846/realpath_8.26-3ubuntu4_all.deb
				wget https://github.com/teejee2008/conky-manager/releases/download/v2.4/conky-manager-v2.4-amd64.deb
				sudo dpkg -i realpath_8.26-3ubuntu4_all.deb conky-manager-v2.4-amd64.deb
				sudo apt -f install

				# sudo add-apt-repository -y ppa:mark-pcnetspec/conky-manager-pm9
				# sudo apt-get update
				# echo $pw | sudo -S apt-get install -y conky-manager
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
			# echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 
			echo $pw | sudo -S sed -i 's/.* /#&/' /etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list
		
			elif [ $distrib == "MX18" ] ; then
			# echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 

			#for ubuntu and derivative
			elif [ $os == "Ubuntu" ] || [ $os = "LinuxMint" ]; then
			echo $pw | sudo -S add-apt-repository -y ppa:xuzhen666/dockbarx
			echo $pw | sudo -S apt-get update
			# echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 
			fi	
		fi
	### THEME ###
	# Arc
	#echo $pw | sudo -S apt-get install -y arc-theme arc-theme-hdpi arc-theme-xhdpi arc-grey-theme
	# Adapta
	#echo $pw | sudo -S apt-get install -y adapta-gtk-theme adapta-gtk-theme-colorpack
	
	
		# Papirus icon

		if [ ! -d "/usr/share/icons/Papirus"  ]
			# Install : Papirus-icon-theme
			then
				if [ $os = "MX" ] ; then
					echo $pw | sudo -S apt-get install -y papirus-icon-theme
				elif [ $os = "LinuxMint" ] || [ $os = "Ubuntu" ] ; then
					 echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus ; $pw | sudo -S apt-get update ; $pw | sudo -S apt-get install -y papirus-icon-theme
				else echo $pw | sudo -S wget -qO- https://git.io/papirus-icon-theme-install | sh
				fi
		fi		
		
		#test -e "/usr/bin/papirus-folders"
		#if [ $? = 1 ] ; 
		if [ ! -e "/usr/bin/papirus-folders" ]
			#Install : papirus-folders
			then 
				if [ $os = "MX" ] ; then
					echo $pw | sudo -S apt-get install -y papirus-folders
				elif [ $os = "Ubuntu" ] || [ $os = "LinuxMint" ]; then
					echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus
					apt-get update 
					sudo apt-get install -y papirus-folders
				else 
					echo $pw | sudo -S wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-folders/master/install.sh | sh
				fi
		fi

	# Copie des fichier de configuration des logiciels tiers et geox	
		share="/usr/share"
		gt=geox-tweak	
			
		echo $pw | sudo -S cp -v -Rf $share/geox-tweak/theme/dockbarx/* $HOME/.gconf/apps/
		echo $pw | sudo -S cp -v -Rf $share/geox-tweak/theme/plank/* $share/plank/
		echo $pw | sudo -S cp -v -f $share/geox-tweak/theme/xfdashboard/xfdashboard.xml $HOME/.config/xfce4/xfconf/
		echo $pw | sudo -S cp -v -Rf $share/geox-tweak/theme/xfdashboard/xfdashboard-dark-nodock/* $share/themes/xfdashboard-dark-nodock/
		echo $pw | sudo -S cp -v -f $share/geox-tweak/theme/synapse/config.json $HOME/.config/synapse/
		echo $pw | sudo -S cp -v -Rf $share/geox-tweak/theme/conky/* $HOME/.conky/
		
		
			### Theme of synapse, plank & dockbarx ###

		# copie des themes
		echo $pw | sudo -S tar -jxvf /usr/share/geox-tweak/themes.tar.bz2 -C /usr/share/themes/  --skip-old-files    
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



