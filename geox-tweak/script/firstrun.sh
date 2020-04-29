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


add_ppa() {
      for i in "$@"; do
        grep -h "^deb.*$i" /etc/apt/sources.list.d/* > /dev/null 2>&1
        if [ $? -ne 0 ]
        then
		echo "-----------------"
          echo "Adding ppa:$i"
		echo "-----------------"
          echo $pw | sudo -S  add-apt-repository -y ppa:$i
        else
          echo "ppa:$i already exists ..."
        fi
      done
    }


_installConf()
	{
	# Fixit Debian postinst
	echo "----------------------------------------------"
	echo "Copying extra themes and configuration files"
	echo "----------------------------------------------"
	# Dockbarx
	mkdir -p $HOME/.gconf/apps/
	tar -xf /usr/share/geox-tweak/theme/dockbarx/dockbarx.tar.gz -C $HOME/.gconf/apps
	sudo tar -xf /usr/share/geox-tweak/theme/dockbarx/dockbarx-themes-master.tar.gz -C /usr/share/dockbarx/themes/ --skip-old-files
	# Plank
	sudo tar -xf /usr/share/geox-tweak/theme/plank.tar.gz -C /usr/share/plank/themes/
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

	# configure plank
# Fixit > Property "/general/show_dock_shadow" does not exist on channel "xfwm4". If a new property should be created, use the --create option.
	xfconf-query -cv xfwm4 -p /general/show_dock_shadow --create --type bool -s "false"
	cp -Rfv /usr/share/geox-tweak/panel/plank/* $HOME/.config/plank/
	gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ dock-items " /net/launchpad/plank/docks/dock1/dock-items ['thunar.dockitem', 'firefox.dockitem', 'thunderbird.dockitem', 'torbrowser.dockitem', 'org.xfce.Catfish.dockitem', 'gmusicbrowser.dockitem', 'clementine.dockitem', 'shotwell.dockitem', 'libreoffice-startcenter.dockitem', 'mintinstall.dockitem', 'mx-packageinstaller.dockitem', 'org.gnome.Software.dockitem', 'org.keepassxc.KeePassXC.dockitem', 'exo-terminal-emulator.dockitem', 'xfce-settings-manager.dockitem']"


	xfconf-query -c thunar -p /misc-single-click --create --type bool  
	xfconf-query -c thunar -p /misc-folders-first --create --type bool  
	xfconf-query -c thunar -p /misc-text-beside-icons --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/single-click --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-trash --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-home --create --type bool  
	xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-removable --create --type bool  


	# Change gtx launcher after first run
	echo $pw | sudo -S  sed -i 's/firstrun.*/firstrun = no/' $HOME/.config/geox-tweak-xfce/geox-tweak.conf
	echo $pw | sudo -S  sed -i s'%xfce4-terminal -e /usr/share/geox-tweak/script/firstrun.sh%python3 /usr/share/geox-tweak/gtx_gui.py'% /usr/share/applications/GeoX-Tweak.desktop
	
	sudo tar -xf /usr/share/geox-tweak/theme/themes.tar.gz -C /usr/share/themes/ --skip-old-files

	}

installation() 
	{ 
		echo ""
		if [ $os = "MX" ] || [ os = "Debian" ]; then
			_installationMX
		elif [ $os = "Ubuntu" ] || [ $os = "LinuxMint" ] ; then
			_installationUnbuntu
		elif [ $os = "Manjaro" ] ; then
			_installationManjaro
		fi


		_installConf

		echo "----------------------------------------------------------"
		echo "Procces terminate, press enter quit. \
		Please re-launch Geox-Tweak-Xfce. "
		echo "-----------------------------------------------------------"

		read
	}

_repoUbuntu()
	{
#FIXIT > autre distrib concerné !?

        if [ $distrib = "LinuxMint19.3" ]; then
            echo $pw | sudo -S sh -c "echo '
		deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' >/etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
		echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd
            echo $pw | sudo -S apt update
            echo $pw | sudo -S apt install dockbarx xfce4-dockbarx-plugin  
       
	else            
		add_ppa ricotz/docky
		add_ppa xubuntu-dev/extras
		add_ppa xuzhen666/dockbarx
		add_ppa papirus/papirus
		# add_ppa synapse-core/testing >> present dans ubuntu 18.04
		echo $pw | sudo -S apt-get update
		
	fi
	}


_installationUnbuntu()
	{
		installApp="sudo apt-get install -y "

		_repoUbuntu

		echo 
		echo "__Check depends packages ________________"
		echo 

		for app in 'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist'\
		 'dockbarx' 'dockbarx-themes-extra' 'xfce4-dockbarx-plugin' 'conky-all'  'xfce4-datetime-plugin' 'xfce4-battery-plugin' 
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo "-----------------"
					echo $app " installation ..."
					echo "-----------------"
					$installApp $app

				else
					echo "-----------------"
					echo $app " installed "
					echo "-----------------"
			fi

		#

		done

		if [ ! -d "/usr/share/icons/Papirus"  ] ; then
			$installApp papirus-icon-theme
		fi
		
        #FIXIT Papirus-folder not in MINT 19.03 repos (manual install?
		
		if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		fi

	}

_installationMX()
	{
		installApp="sudo apt-get install -y "
		
		echo $pw | sudo sed -i "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list
		echo $pw | sudo apt-get update

		echo 
		echo "__Check depends packages ________________"
		echo 

		for app in 'plank'  'synapse' 'zeitgeist' 'dockbarx' 'dockbarx-common' \
				 'xfce4-dockbarx-plugin' 'papirus-icon-theme'  \
				 'papirus-folders' 'conky-all' 'conky-manager' \
				 'xfdashboard' 'xfdashboard-plugins' 
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo 
					echo $app "installation ... "
					echo 
					$installApp $app
				else
					echo 
					echo $app " installed "
					echo 
			fi	
		done
		echo $pw | sudo sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list
		if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		fi

	}
_installationManjaro()
	{
		
		echo 
		echo "__Check depends packages ________________"
		echo
		for app in 'base-devel' 'yay' 'plank'  'synapse' 'zeitgeist'   
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo $app installation ...
					echo $pw | sudo -S pacman -S --noconfirm $app

				else
					echo $app is installed
			fi	
		done

		for app in 'xfdashboard' 'xfdashboard-plugins' 'dockbarx' 'xfce4-dockbarx-plugin' 'conky-lua' 
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo $app installation ...
					yay -S --noconfirm $app

				else
					echo $app is installed
			fi	
		done

	if [ ! -d "/usr/share/icons/Papirus"  ]
		# Install : Papirus-icon-theme
		then
			echo papirus-icon-theme installation ...
			echo $pw | sudo -S sudo pacman -S --noconfirm papirus-icon-theme
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		else
			echo papirus-icon-theme is installed
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


echo "-----------------------------------------------------------------"
echo " This scrip will the configure Geox-Tweak-Xfce ..."
echo
echo " The following software will be installed if necessary :"
echo " Plank, synapse, conky, xfdashboard and extra themes"
echo "-----------------------------------------------------------------"
echo ""
 
echo "Are you ok to procced  ? Tap enter for yes, tap ctrl+c or close terminal for no"

read

installation && exit