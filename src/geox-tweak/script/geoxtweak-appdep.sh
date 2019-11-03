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

mainFunction () {
	title="${1}"
	command="${2}"
	log="/tmp/$(date +%s)"
	config="--progress --pulsate --center --no-buttons --auto-close
	--progress-text='Installation ...' --width=600"

	${command} 2> "${log}" |
	while read -r line; do echo "# ${line}"; done |
	yad ${config} --title="${title}"

	checkErrorLog "${log}"
}


checkErrorLog () {
    log="${1}"
    error=$(cat "${log}")
    rm "${log}"

    if [ "${error}" != "" ]; then
        echo "${error}" >&2
        errorWindow "${error}"
        exit 1
    else yad --text=" installation terminée " --button=OK:1
    fi
}


errorWindow () {
    error="${1}"
    config="--center --button=OK:1"

    yad ${config} --title="Error" --text="${error}" --width 800 --height 500
}

installation() 
{ 
		#plank
		which plank > /dev/null
		if [ $? = 1 ]
		then
			sudo apt-get install -y plank
		fi
		
		#Xfdashboard
		which xfdashboard > /dev/null
		if [ $? = 1 ]
		then
			sudo apt-get install -y xfdashboard
			sudo apt-get install -y xfdashboard-plugins
		fi
				
		#Synapse
		which synapse > /dev/null
		if [ $? = 1 ]
		then
			sudo apt-get install -y synapse
		fi
		
		
		#Redshift
		which redshift > /dev/null
		if [ $? = 1 ]
		then
			sudo apt-get install -y redshift
			sudo apt-get install -y redshift-gtk
		fi

		#Conky
		which conky > /dev/null
		if [ $? = 1 ]
		then
			sudo apt-get install -y conky-all
			sudo apt-get install -y conky-manager
		fi 
		
		#Dockbarx & xfce4-dockbarx-plugin
		which dockx >/dev/null
		if [ $? = 1 ] ;
		then
			#for mx 19
			if [ $distrib = MX19 ] ; then
			sudo sh -c "echo 'deb
			http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >
			/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
			sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd 
			sudo apt-get update
			sudo apt-get install -y xfce4-dockbarx-plugin
			sudo apt-get install -y dockbarx-themes-extra 
			
			#for ubuntu and derivative
			elif [ $distrib = MX18 ] ; then
			sudo apt-get install -y xfce4-dockbarx-plugin
			sudo apt-get install -y dockbarx-themes-extra 

			elif [ $os = Ubuntu ] ; then
			sudo add-apt-repository ppa:xuzhen666/dockbarx
			sudo apt-get update
			sudo apt-get install -y xfce4-dockbarx-plugin
			sudo apt-get install -y dockbarx-themes-extra 
			
			elif [ $os = LinuxMint ] ; then
			sudo add-apt-repository ppa:xuzhen666/dockbarx
			sudo apt-get update
			sudo apt-get install -y xfce4-dockbarx-plugin
			sudo apt-get install -y dockbarx-themes-extra 
			
			fi	
		fi
	### THEME ###
	# Arc
	#sudo apt-get install -y arc-theme arc-theme-hdpi arc-theme-xhdpi arc-grey-theme
	# Adapta
	#sudo apt-get install -y adapta-gtk-theme adapta-gtk-theme-colorpack
	
	
	# Papirus icon
	sudo apt-get install -y papirus-icon-theme papirus-folders
	
	# copie des themes
	#sudo tar -zxfk theme.tar.gz -C /usr/share/themes/
	
}

#Interface graphique YAD
yadgui() {

 GUI=$(yad --width=500 --heigth=600 \
	--text="Les logiciels suivants vont être installé : 

	- Plank : Une barre de lancement d'applications
	- Xfdashboard : Affiche les applications et fenetres en cours
	- Synapse : Lanceur d'applications rapide (raccourci Ctrl-espace)
	- Conky : Permet d'afficher divers informations sur le bureau (date, heure,
	ressources PCU, RAM...)
	- Redshift : Permet de moins se fatiguer les yeux
	- Collection de theme GTK et icones (Arc, Adapta, Materia...)"  \
	)
	
	mainFunction "Installation" installation
}

yadgui



