#!/bin/bash

# Verification de la presence et installation des logiciels d'optimisation de XFCE

dir=$(dirname "$0")  # 'dirname $0' renvoie le nom du répertoire dans lequel le script actuel se trouve.

#Interface graphique YAD
if GUI=$(yad --text="Les logiciels suivants vont être installé : 

- Plank : Une barre de lancement d'applications
- Xfdashboard : Affiche les applications et fenetres en cours
- Synapse : Lanceur d'applications rapide (raccourci Ctrl-espace)
- Conky : Permet d'afficher divers informations sur le bureau (date, heure,
ressources PCU, RAM...)
- Redshift : Permet de moins se fatiguer les yeux
- Collection de theme GTK et icones (Arc, Adapta, Materia...) "

)

then 
	#plank
	
	which plank > /dev/null
	if [ $? = 1 ]
	then
		sudo apt -y install plank
		notify-send -i system-software-update "Installation de Plank" -t 5000
	
	fi
	
	#Xfdashboard
	
	which xfdashboard > /dev/null
	if [ $? = 1 ]
	then
		notify-send -i system-software-update "Installation de xfdashboard" -t 5000
		sudo apt -y install xfdashboard
		sudo apt -y install xfdashboard-plugins
	fi
	
	
	
	#Synapse
	
	which synapse > /dev/null
	if [ $? = 1 ]
	then
		notify-send -i system-software-update "Installation de synapse" -t 5000
		sudo apt -y install synapse
	fi
	
	
	#Redshift
	
	which redshift > /dev/null
	if [ $? = 1 ]
	then
		notify-send -i system-software-update "Installation de redshift" -t 5000
		sudo apt -y install redshift
		sudo apt -y install redshift-gtk

	fi

	#Conky
	
	witch conky > /dev/null
	if [ $? = 1 ]
	then
		notify-send -i system-software-update "Installation de conky" -t 5000
		sudo apt -y install conky-all
		sudo apt -y install conky-manager
	fi 

	### THEME ###
	
	# Arc
	#notify-send -i system-software-update "Installation du theme Arc" -t 5000
	#sudo apt -y install arc-theme arc-theme-hdpi arc-theme-xhdpi arc-grey-theme
	
	# Adapta
	#notify-send -i system-software-update "Installation du theme Adapta" -t 5000
	#sudo apt -y install adapta-gtk-theme adapta-gtk-theme-colorpack
	
	
	# Papirus icon
	notify-send -i system-software-update "Installation du theme d'icones papyrus" -t 5000
	sudo apt -y install papirus-icon-theme papirus-folders
	
	# copie des themes
	sudo tar -zxfk theme.tar.gz -C /usr/share/themes/
	
fi

yad --text="installation terminée"


