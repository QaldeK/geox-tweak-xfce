#!/bin/bash

##################################################################################
# Install script for geox-tweak on Debian system (MXlinux, xubuntu, linux-mint)
#-------------------------------- 
#
#	For install geox-tweak-xfce : launch "install-geox" or open a terminal in the "install-script.sh" directory, 
# 	and enter "./install.sh"
# 	For uninstall : "sudo ./uninstall"
#
##################################################################################


echo "---------------------------------------------------------------------------------------"
echo "This script will check geox-tweak-xfce dependencies

:: 'python3' 'python3-gi' 'xfce4-datetime-plugin' 'xfce4-battery-plugin' 
'gconf2' 'gir1.2-gtk-3.0' 'gtk2-engines-murrine' 'gtk2-engines-pixbuf'

 ::'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'xfce4-dockbarx-plugin' 'conky-all' 'papirus-folders'
 'papirus-icon-theme'



 Network connection is require ! 

 
 Are you ok to procced  ? Tap enter for yes, tap ctrl+c or close terminal for no"
echo
read
echo "---------------------------------------------------------"
read -sp 'User password is require: ' pw
echo

mainFunction () {
	command="${1}"
	log="/tmp/$(date +%s)"
	${command} 2> "${log}" 
	checkErrorLog "${log}"
}

checkErrorLog () {
    log="${1}"
    error=$(cat "${log}")
    rm "${log}"

    if [ "${error}" != "" ]; then
    	echo "---------------------"
    	echo "Error during process :"
    	echo
        echo "${error}"
        echo "---------------------"
        echo
		echo "press enter for exit"
		read    
        exit 1
    
    else 
    	echo "----------------------------------------------"
		echo "Process completed, press enter for exit"
		echo "----------------------------------------------"
		read    
	fi
}


add_ppa() {
      for i in "$@"; do
        grep -h "^deb.*$i" /etc/apt/sources.list.d/* > /dev/null 2>&1
        if [ $? -ne 0 ]
        then
          echo "Adding ppa:$i \
........"
          echo $pw | sudo -S add-apt-repository -y ppa:$i
        else
          echo "ppa:$i already exists \
........"
        fi
      done
    }


_installation()	{
	
	_installationDep

	_installConf
}

_installConf()
{
	# Fixit Debian postinst
	echo "----------------------------------------------"
	echo "Copying extra configuration files"
	echo "----------------------------------------------"
	# Dockbarx
	mkdir -p $HOME/.gconf/apps/
	tar -xf /usr/share/geox-tweak/theme/dockbarx/dockbarx.tar.gz -C $HOME/.gconf/apps
	# xfdashboard
	sudo cp -Rf /usr/share/geox-tweak/theme/xfdashboard/xfdashboard-dark-nodock /usr/share/themes/
	cp -f /usr/share/geox-tweak/theme/xfdashboard/xfdashboard.xml $HOME/.config/xfce4/xfconf/xfce-perchannel-xml 
	# Synapse
	mkdir -p $HOME/.config/synapse/
	cp -f /usr/share/geox-tweak/theme/synapse/* $HOME/.config/synapse/
	# Conky
	mkdir -p $HOME/.conky
	tar -xf /usr/share/geox-tweak/theme/conky.tar.gz -C $HOME/.conky
	sudo cp -f /usr/share/geox-tweak/script/conkytoggle.sh	/usr/bin/conkytoggle.sh
	# Autostart
	mkdir -p $HOME/.config/autostart/
	cp -n /usr/share/geox-tweak/script/autostart/* $HOME/.config/autostart/
	# Geox-Tweak-Xfce
	mkdir $HOME/.config/geox-tweak-xfce/
	cp /usr/share/geox-tweak/geox-tweak.conf $HOME/.config/geox-tweak-xfce/
	cp -ru /usr/share/geox-tweak/panel/ $HOME/.config/geox-tweak-xfce/

	#conky fonts
	echo $pw | sudo -S cp -R /usr/share/geox-tweak/theme/Podkova /usr/share/fonts/truetype/


	echo '''#pulseaudio-button * {-gtk-icon-transform: scale(1);}
#xfce4-notification-plugin * {-gtk-icon-transform: scale(1);}
#xfce4-power-manager-plugin * {-gtk-icon-transform: scale(1);}''' >> $HOME/.config/gtk-3.0/gtk.css

	#  plank
	sudo tar -xf /usr/share/geox-tweak/theme/plank.tar.gz -C /usr/share/plank/themes/	

	xfconf-query -cv xfwm4 -p /general/show_dock_shadow --create --type bool -s "false"
	cp -Rf /usr/share/geox-tweak/panel/plank/* $HOME/.config/plank/
	gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ dock-items "['thunar.dockitem', 'firefox.dockitem', 'thunderbird.dockitem', 'torbrowser.dockitem', 'org.xfce.Catfish.dockitem', 'gmusicbrowser.dockitem', 'clementine.dockitem', 'shotwell.dockitem', 'libreoffice-startcenter.dockitem', 'mintinstall.dockitem', 'mx-packageinstaller.dockitem', 'org.gnome.Software.dockitem', 'org.keepassxc.KeePassXC.dockitem', 'exo-terminal-emulator.dockitem', 'xfce-settings-manager.dockitem']"
	xfconf-query -c thunar -p /misc-single-click --create --type bool  
	xfconf-query -c thunar -p /misc-folders-first --create --type bool  
	xfconf-query -c thunar -p /misc-text-beside-icons --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/single-click --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-trash --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-home --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-removable --create --type bool  


	# Change gtx launcher after first run
	echo $pw | sudo -S  sed -i s'%xfce4-terminal -e /usr/share/geox-tweak/script/firstrun.sh%python3 /usr/share/geox-tweak/gtx_gui.py'% /usr/share/applications/GeoX-Tweak.desktop
	
	sudo tar -xf /usr/share/geox-tweak/theme/themes.tar.gz -C /usr/share/themes/ --skip-old-files

	echo "=>  preserve whiskermenu config."
	path_panel=/usr/share/geox-tweak/panel
	echo $pw | sudo -S find $HOME/.config/xfce4/panel/ -name "whisker*" -exec cp -f -r -v {} $path_panel/whiskermenu-20.rc \;
	echo $pw | sudo -S find $path_panel/*/xfce4/panel/  -maxdepth 0 -exec cp -f $path_panel/whiskermenu-20.rc {} \;

	echo "Done."
}
	
_installationDep() 
	{ 
		if [ -f /etc/lsb-release ]; then
		    # For some versions of Debian/Ubuntu without lsb_release command
		    . /etc/lsb-release
		    os=$DISTRIB_ID
		    ver=$DISTRIB_RELEASE
		    echo " "
		    echo "for" $os $ver
		    echo " "
		fi

		distrib=$os$ver
		
		if [ $os = "MX" ] || [ $os = "Debian" ]; then
			_installationMX 
		elif [ $os = "Ubuntu" ] || [ $os = "LinuxMint" ] ; then
			_installationUbuntu 
		elif [ $os = "ManjaroLinux" ] ; then
			_installationManjaro
		fi
	}

_installationDebian()
	{	
		echo 
		echo "__Check depends packages ________________"
		echo 

				for app in 'python3' 'python3-gi' 'xfce4-datetime-plugin' \
				'xfce4-battery-plugin' 'gconf2' \
				'gir1.2-gtk-3.0' 'gtk2-engines-murrine' 'gtk2-engines-pixbuf'\
				'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist' \
				'xfce4-datetime-plugin' 'xfce4-battery-plugin' 'xfce4-dockbarx-plugin' \
				'conky-all' 'conky' 'papirus-icon-theme' 
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo $app installation ...
					echo $pw | sudo -S apt-get install -y $app

				else
					echo $app is installed

			fi	
		done

		# @ Papirus icon theme
		if [ ! -d "/usr/share/icons/Papirus"  ]
			# Install : Papirus-icon-theme
			then
				echo papirus-icon-theme installation ...
				wget -qO- https://git.io/papirus-icon-theme-install | sh
		fi		
		
		if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		fi	

		if [ ! -e "/usr/bin/papirus-folders" ]
			#Install : papirus-folders
			then 
				echo papirus-folders installation ...
				wget -qO- https://git.io/papirus-folders-install | sh
			else
				echo papirus-folders is installed
		fi

	}

_installationUnbuntu()
	{
		#FIXIT > autre distrib concerné !?

		echo 
		echo "__Check ppa: ________________"
		echo 

        if [ $distrib = "LinuxMint19.3" ] || [ $distrib = "Ubuntu18.04"]; then
            echo $pw | sudo -S sh -c "echo '
		deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
			echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd
            echo $pw | sudo -S apt update
			echo $pw | sudo -S apt install dockbarx xfce4-dockbarx-plugin dockbarx-themes-extra 
            echo $pw | sudo -S rm /etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list

        else
	        echo 
	        echo "__Install ppa: ________________"
	        echo 

			add_ppa ricotz/docky
			add_ppa xubuntu-dev/extras
			add_ppa xuzhen666/dockbarx
			# add_ppa synapse-core/testing >> present dans ubuntu 18.04
		fi
			
		add_ppa papirus/papirus

		echo $pw | sudo -S apt-get update



		_installationDebian

	}

_installationMX()
	{
	echo $pw | sudo -S sed -i "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list

#		if [ $distrib == "MX19" ] ; then
#			echo $pw | sudo -S sh -c "echo '
#			deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
#			echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd
#		fi

	echo $pw | sudo -S apt-get update

	if [ $(dpkg-query -W -f='${Status}' conky-manager 2>/dev/null | grep -c "ok installed") -eq 0 ];
	then
		echo $app installation ...
		echo $pw | sudo -S apt-get install -y $app

	else
		echo $app is installed
	fi	


	echo $pw | sudo -S sed -i 's/.* test/#/'  /etc/apt/sources.list.d/mx.list

	_installationDebian
}

_installationManjaro()
	{

		echo "Geox-Tweak-Xfce need xfce4-dockbarx-plugin for some layout desktop theme, but this script don't install it. Please try to install xfce4-dockbarx-plugin manually

		Press enter for continue..."

		read
		
		echo 
		echo "__Check depends packages ________________"
		echo


		for app in 'base-devel' 'yay'  'python3' 'python3-gi' 'xfce4-datetime-plugin' 'xfce4-battery-plugin' \
			'plank'  'synapse' 'zeitgeist'   
			do
				if not pacman -Qs $package > /dev/null
				then
					echo $app installation ...
					echo $pw | sudo -S pacman -S --noconfirm $app

				else
					echo $app is installed
			fi	
		done

		for app in 'xfdashboard' 'xfdashboard-plugins' 'conky-lua' 
			do
					echo $app installation ...
					yay -S --noconfirm $app
			done

	if [ ! -d "/usr/share/icons/Papirus"  ]
		# Install : Papirus-icon-theme
		then
			echo "----------------------"
			echo papirus-icon-theme installation ...
			echo ".................................."
			echo $pw | sudo -S sudo pacman -S --noconfirm papirus-icon-theme
		else
			echo papirus-icon-theme is installed
	fi

	if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
		wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
	fi	

	if [ ! -e "/usr/bin/papirus-folders" ]
		#Install : papirus-folders
		then 
			echo papirus-folders installation ...
			wget -qO- https://git.io/papirus-folders-install | sh
		else
			echo papirus-folders is installed
	fi
	
}


mainFunction _installation
