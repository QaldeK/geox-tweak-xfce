#!/bin/bash

# Verification de la presence et installation des logiciels d'optimisation de XFCE

dir=$(dirname "$0")  # 'dirname $0' renvoie le nom du répertoire dans lequel le script actuel se trouve.

#Check lla distribution linux
if [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    os=$DISTRIB_ID
    ver=$DISTRIB_RELEASE
    
    echo $os $ver
   
fi

distrib=$os$ver

which yad > /dev/null
if [ $? = 1 ];
then
	echo "Install Yad"
	x-terminal-emulator -e "echo Install yad \
			sudo apt-get install -y yad"
			
else echo "yad OK"
fi

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
			echo "Install plank"
			if [ $distrib = "MX19" ] ; then
			echo $pw | sudo -S apt-get install -y plank 

			elif [ $distrib = "MX18" ] ; then
			echo $pw | sudo -S apt-get install -y plank 

			elif [ $os = "LinuxMint" ]; then
			echo $pw | sudo -S add-apt-repository -y ppa:ricotz/docky
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y plank
			
			elif [ $os = "Ubuntu" ]; then
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
			echo "Install xfdashboard"
			echo $pw | sudo -S sed -e "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list^C
			echo $pw | sudo -S apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins
			echo $pw | sudo -S sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list
			elif [ $distrib = "MX18" ] ; then
			echo $pw | sudo -S apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins
			elif [ $os = "LinuxMint" ]; then
			sudo add-apt-repository ppa:xubuntu-dev/extras
			sudo apt-get update
			echo $pw | sudo -S apt-get install -y xfdashboard
			echo $pw | sudo -S apt-get install -y xfdashboard-plugins		
			elif [ $os = "Ubuntu" ]; then
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
		
		
		#Redshift
		# which redshift > /dev/null
		# if [ $? = 1 ]
		# then
		# 	echo $pw | sudo -S apt-get install -y redshift
		# 	echo $pw | sudo -S apt-get install -y redshift-gtk
		# fi

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
			echo $pw | sudo -S sed -i 's/.* /#&/' /etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list
		
			elif [ $distrib == "MX18" ] ; then
			echo $pw | sudo -S apt-get install -y dockbarx
			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin
			echo $pw | sudo -S apt-get install -y dockbarx-themes-extra 

			#for ubuntu and derivative
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

		if [ ! -d "/usr/share/icons/Papirus"  ]
			# Install : Papirus-icon-theme
			then
				if [ $distrib = "MX19" ] ; then
					echo $pw | sudo -S apt-get install -y papirus-icon-theme
				elif [ $distrib = "MX18" ] ; then
					echo $pw | sudo -S apt-get install -y papirus-icon-theme
				elif [ $os = "LinuxMint" ]; then
					 echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus ; $pw | sudo -S apt-get update ; $pw | sudo -S apt-get install -y papirus-icon-theme
				elif [ $os = "Ubuntu" ]; then
					 echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus ; $pw | sudo -S apt-get update ; $pw | sudo -S apt-get install -y papirus-icon-theme
				else echo $pw | sudo -S wget -qO- https://git.io/papirus-icon-theme-install | sh
				fi
		fi		
		
		#test -e "/usr/bin/papirus-folders"
		#if [ $? = 1 ] ; 
		if [ ! -e "/usr/bin/papirus-folders" ]
			#Install : papirus-folders
			then 
				if [ $distrib = "MX18" ] ; then
					echo $pw | sudo -S apt-get install -y papirus-folders
				elif [ $distrib = "MX19" ]; then
					echo $pw | sudo -S apt-get install -y papirus-folders
				elif [ $os = "Ubuntu" ]; then
					echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus
					apt-get update 
					sudo apt-get install -y papirus-folders
				elif [ $os = "LinuxMint" ]; then
					echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus
					echo $pw | sudo -S apt-get update 
					echo $pw | sudo -S apt-get install -y papirus-folders

				else 
					echo $pw | sudo -S wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-folders/master/install.sh | sh
				fi
		fi
		

		### Theme of synapse, plank & dockbarx ###
	share="/usr/share"
	gt=geox-tweak
	cp -v -Rf $share/geox-tweak/theme/dockbarx/* $HOME/.gconf/apps
	cp -v -Rf $share/geox-tweak/theme/plank/* $share/plank
	cp -v -f $share/geox-tweak/theme/xfdashboard/xfdashboard.xml $HOME/.config/xfce4/xfconf/
	cp -v -Rf $share/geox-tweak/theme/xfdashboard/xfdashboard-dark-nodock/* $share/themes/xfdashboard-dark-nodock
	cp -v -f $share/geox-tweak/theme/synapse/config.json $HOME/.config/synapse
	cp -v -Rf $share/geox-tweak/theme/conky/* $HOME/.conky
	mkdir -v $HOME/.config/geox-tweak-xfce
	cp -v $share/geox-tweak/activ.conf $HOME/.config/geox-tweak-xfce
	echo $pw | sudo -S tar -jxvf /usr/share/geox-tweak/themes.tar.bz2 -C /usr/share/themes/  --skip-old-files    
	echo ""
	echo "Process completed, press enter for exit"
	read

