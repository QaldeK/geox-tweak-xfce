#!/bin/bash

##################################################################################

# script for complete installation of geox-tweak on Debian system (MXlinux, xubuntu, linux-mint), and perhaps Manjaro

# Part of  GeoX-Tweak-Xfce
# Copyright: 2019 QaldeK <aldek at vivaldi dot net>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License with
#  the Debian GNU/Linux distribution in file /usr/share/common-licenses/GPL;
#  if not, write to the Free Software Foundation, Inc., 51 Franklin St,
#  Fifth Floor, Boston, MA 02110-1301, USA.

# On Debian systems, the complete text of the GNU General
# Public License can be found in `/usr/share/common-licenses/GPL'.

##################################################################################


echo "---------------------------------------------------------------------------------------"
echo "This script will check geox-tweak-xfce dependencies

'python3' 'python3-gi' 'xfce4-datetime-plugin'  
'gconf2' 'gir1.2-gtk-3.0' 'gtk2-engines-murrine'
'gtk2-engines-pixbuf'

 'plank' 
 'xfdashboard' 'xfdashboard-plugins' 
 'synapse' 
 'xfce4-dockbarx-plugin' 
 'conky-all' 
 'papirus-icon-theme' 'papirus-folders'

==> Network connection is require ! <== 
 
 Are you ok to procced  ? Tap your password if asked (Press ENTER if not), or close terminal for abort
 "
read
echo "---------------------------------------------------------"
read -sp 'Please enter your user password: ' pw
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

    if [ "${error}" != "" ]; then
    	echo "---------------------"
    	echo "Check Error during process : /tmp/"$log
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
	mkdir $HOME/.config/synapse/
	cp -f /usr/share/geox-tweak/theme/synapse/* $HOME/.config/synapse/
	# Conky
	mkdir $HOME/.conky
	tar -xf /usr/share/geox-tweak/theme/conky.tar.gz -C $HOME/.conky
	sudo cp -f /usr/share/geox-tweak/script/conkyaddrm.sh	/usr/bin/conkyaddrm.sh
	# Autostart
	mkdir $HOME/.config/autostart/
	cp -n /usr/share/geox-tweak/script/autostart/* $HOME/.config/autostart/
	# Geox-Tweak-Xfce
	mkdir -p $HOME/.config/geox-tweak-xfce/panel
	cp /usr/share/geox-tweak/geox-tweak.conf $HOME/.config/geox-tweak-xfce/
	cp -r /usr/share/geox-tweak/panel/* $HOME/.config/geox-tweak-xfce/panel/

	#conky fonts
	echo $pw | sudo -S cp -R /usr/share/geox-tweak/theme/Podkova /usr/share/fonts/truetype/



	echo '''#pulseaudio-button * {-gtk-icon-transform: scale(1);}
#xfce4-notification-plugin * {-gtk-icon-transform: scale(1);}
#xfce4-power-manager-plugin * {-gtk-icon-transform: scale(1);}''' >> $HOME/.config/gtk-3.0/gtk.css

	#  plank
	sudo tar -xf /usr/share/geox-tweak/theme/plank.tar.gz -C /usr/share/

	xfconf-query -cv xfwm4 -p /general/show_dock_shadow --create --type bool -s "false"

	if [ ! -d "$HOME/.config/plank" ]; then
		echo plank not installed
		
		for app in 'thunar' 'firefox' 'thunderbird' 'torbrowser' 'org.xfce.Catfish' 'gmusicbrowser' 'clementine' 'shotwell' 'libreoffice-startcenter' 'mintinstall' 'mx-packageinstaller' 'org.gnome.Software' 'org.keepassxc.KeePassXC' 'exo-terminal-emulator' 'xfce-settings-manager'
	 	do
			APPS=/usr/share/applications/$app.desktop
	 		if [ -f "$APPS" ]; then 
	 			
	 		mkdir -p $HOME/.config/geox-tweak-xfce/panel/plank/dock1/launchers/
			
			mkdir -p $HOME/.config/plank/dock1/launchers/
	 		
	 		cp -Rf /usr/share/geox-tweak/theme/plank/dock1/launchers/$app.dockitem $HOME/.config/plank/dock1/launchers/

			fi
		done
		
		gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ dock-items "['thunar.dockitem', 'firefox.dockitem', 'thunderbird.dockitem', 'torbrowser.dockitem', 'org.xfce.Catfish.dockitem', 'gmusicbrowser.dockitem', 'clementine.dockitem', 'shotwell.dockitem', 'libreoffice-startcenter.dockitem', 'mintinstall.dockitem', 'mx-packageinstaller.dockitem', 'org.gnome.Software.dockitem', 'org.keepassxc.KeePassXC.dockitem', 'exo-terminal-emulator.dockitem', 'xfce-settings-manager.dockitem']"

	else
		echo "=>  preserve plank config."
		
		cp -Rf $HOME/.config/plank/* $HOME/.config/geox-tweak-xfce/panel/plank/
		dconf dump /net/launchpad/plank/docks/ > $HOME/.config/geox-tweak-xfce/panel/plank/plank.ini

		# find $HOME/.config/geox-tweak-xfce/panel/*/plank  -exec cp -f $HOME/.config/geox-tweak-xfce/panel/plank/plank.ini {} \;

		echo "Done."
	fi


	xfconf-query -c thunar -p /misc-single-click --create --type bool -s false  
	xfconf-query -c thunar -p /misc-folders-first --create --type bool -s true 
	xfconf-query -c thunar -p /misc-text-beside-icons --create --type bool -s false 
	xfconf-query -c xfce4-desktop -p /desktop-icons/single-click --create --type bool -s false 
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-trash --create --type bool -s true 
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-home --create --type bool -s true 
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-removable --create --type bool -s true  

	# sudo tar -xf /usr/share/geox-tweak/theme/themes.tar.gz -C /usr/share/themes/ --skip-old-files

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
		 'gconf2' \
		'gir1.2-gtk-3.0' 'gtk2-engines-murrine' 'gtk2-engines-pixbuf'\
		'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist' \
		'xfce4-datetime-plugin' 'conky-all' 'conky' 'papirus-icon-theme' 'tar' 'xz-utils'
		#xfce4-dockbarx-plugin >> move in specific distrib
		do
			if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
			then
				echo $app "==> try installation ..."
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
		_installationDebian

		echo 
		echo "__Check ppa: ________________"
		echo 

		# TODO check if needed in || [ $distrib = "Ubuntu18.04"]
        if [ $distrib = "LinuxMint19.3" ] ; then
            echo $pw | sudo -S sh -c "echo '
		deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
			echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd
			sleep 2
            echo $pw | sudo -S apt update
			echo $pw | sudo -S apt install dockbarx xfce4-dockbarx-plugin dockbarx-themes-extra 
            # echo $pw | sudo -S rm /etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list
		fi

		if [ $(dpkg-query -W -f='${Status}' plank  2>/dev/null | grep -c "ok installed") -eq 0 ];
		then
			echo "---> PPA for Plank  ... 
			 "
			add_ppa ricotz/docky
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y plank
		fi			

		if [ $(dpkg-query -W -f='${Status}' xfdashboard 2>/dev/null | grep -c "ok installed") -eq 0 ];
		then
			echo "---> PPA for xfdashboard  ... 
						 "
			add_ppa xubuntu-dev/extras
			echo $pw | sudo -S apt-get update
			echo $pw | sudo -S apt-get install -y xfdashboard 
		fi			
		
		if [ $(dpkg-query -W -f='${Status}' synapse 2>/dev/null | grep -c "ok installed") -eq 0 ];
		then
			echo "---> PPA for synapse  ... 
			 "
			add_ppa synapse-core/testing
 			echo $pw | sudo -S apt-get update
 			echo $pw | sudo -S apt-get install -y synapse
		fi	
	
		if [ $(dpkg-query -W -f='${Status}' dockbarx 2>/dev/null | grep -c "ok installed") -eq 0 ];
		then
			echo "---> PPA for xfce4-dockbarx-plugin  ... 
			 "
			add_ppa xuzhen666/dockbarx
			echo $pw | sudo -S apt-get update

			echo $pw | sudo -S apt-get install -y xfce4-dockbarx-plugin dockbarx-themes-extra
		fi	
		
	}

_installationMX()
	{
	_installationDebian

	echo "_____Missing Software ... Retry From Test Repo______
	"

	echo $pw | sudo -S sed -i "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list

		# if [ $distrib == "MX19" ] ; then
		# 	echo $pw | sudo -S sh -c "echo '
		# 	deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
		# 	echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd
		# fi

	sleep 2

	if [ $distrib = "MX19" ]; then 
		echo $pw | sudo -S sh -c "echo 'deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu focal main' >/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-focal.list"
	    echo $pw | sudo -S apt-key adv --recv-keys --keyserver
	    keyserver.ubuntu.com  77d026e2eead66bd sleep 2 echo $pw | sudo -S
	    apt update echo $pw | sudo -S apt install dockbarx
	    xfce4-dockbarx-plugin dockbarx-themes-extra
	    # echo $pw | sudo -S rm /etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list
	
	# echo $pw | sudo -S apt-get update


		for app in 	'python-gconf' 'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist' 'xfce4-dockbarx-plugin' \
		'conky-all' 'conky-manager'
		do
			if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
			then
				echo $app "installation from test repo"
				echo $pw | sudo -S apt-get install -y $app
			fi	
		done


	echo $pw | sudo -S sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list

}

_installationManjaro()
	{

	echo "Geox-Tweak-Xfce need xfce4-dockbarx-plugin for some layout desktop theme, but this script don't install it. Please try to install xfce4-dockbarx-plugin manually

	Press enter for continue..."

	read
	
	echo 
	echo "__Check depends packages ________________"
	echo


	for app in 'base-devel' 'yay'  'python3' 'python3-gi' 'xfce4-datetime-plugin'  \
		'plank'  'synapse' 'zeitgeist' 'tar' 'xz-utils'  
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
