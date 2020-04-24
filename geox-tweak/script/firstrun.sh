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
	sudo tar -xf /usr/share/geox-tweak/theme/plank.tar.gz -C /usr/share/plank
	# xfdashboard
	sudo cp -Rf /usr/share/geox-tweak/theme/xfdashboard/xfdashboard-dark-nodock/* /usr/share/themes/
	cp -f /usr/share/geox-tweak/theme/xfdashboard/xfdashboard.xml $HOME/.config/xfce4/xfconf/xfce-perchannel-xml 
	# Synapse
	mkdir -p $HOME/.config/synapse/
	cp -f /usr/share/geox-tweak/theme/synapse/* $HOME/.config/synapse/
	# Conky
	tar -xf /usr/share/geox-tweak/theme/conky.tar.gz -C $HOME/.conky
	sudo cp -f /usr/share/geox-tweak/script/conkytoggle.sh	/usr/bin/conkytoggle.sh
	# Autostart
	cp -f /usr/share/geox-tweak/script/autostart/* $HOME/.config/autostart/
	# Geox-Tweak-Xfce
	cp /usr/share/geox-tweak/geox-tweak.conf $HOME/.config/geox-tweak-xfce
	cp -ru /usr/share/geox-tweak/panel $HOME/.config/geox-tweak-xfce
}

installation() 
	{ 
		echo "-----------------------------------------------------------------"
		echo " This scrip will ending the Geox-Tweak-Xfce configuration..."
		echo " The following application will be installed if there missing: "
		echo " Plank, synapse, conky, xfdashboard and extra themes"
		echo "-----------------------------------------------------------------"

		echo ""
		if [ $os = "MX" ] || [ os = "Debian" ]; then
			_installationMX
		elif [ $os = "Ubuntu" ] || [ $os = "LinuxMint" ] ; then
			_installationUnbuntu
		fi

		sudo tar -xf /usr/share/geox-tweak/theme/themes.tar.gz -C /usr/share/themes/ --skip-old-files

		# change firstrun value
		_installConf

		sed -i 's/firstrun.*/firstrun = no/' $HOME/.config/geox-tweak-xfce/geox-tweak.conf

		echo "----------------------------------------------"
		echo "Procces terminate, press enter for quit"
		echo "----------------------------------------------"

		read

	}

_repoUbuntu()
	{
		sudo add-apt-repository -y ppa:ricotz/docky
		sudo add-apt-repository ppa:xubuntu-dev/extras
		sudo add-apt-repository -y ppa:xuzhen666/dockbarx
		sudo add-apt-repository -y ppa:papirus/papirus
		sudo add-apt-repository ppa:synapse-core/
		sudo apt-get update
	}

_reposMX()
	{
		sudo sed -i "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list
		sudo apt-get update
	}

_installationUnbuntu()
	{
		installApp="sudo apt-get install -y "

		_repoUbuntu

		wget http://launchpadlibrarian.net/340091846/realpath_8.26-3ubuntu4_all.deb
		wget https://github.com/teejee2008/conky-manager/releases/download/v2.4/conky-manager-v2.4-amd64.deb
		sudo dpkg -i realpath_8.26-3ubuntu4_all.deb conky-manager-v2.4-amd64.deb

		for app in 'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist'\
		 'dockbarx' 'xfce4-dockbarx-plugin' 'conky-all' 'conky-manager'
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo $app "installation ..."
					$installApp $app

				else
					echo $app " installed"
			fi

		#

		done

		if [ ! -d "/usr/share/icons/Papirus"  ] ; then
			$installApp papirus-icon-theme
		fi
		
		if [ ! -e "/usr/bin/papirus-folders" ]; then
			$installApp papirus-folders
		fi
		
		if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		fi

	}

_installationMX()
	{
		installApp="sudo apt-get install -y "
		_reposMX
		for app in 'plank'  'synapse' 'zeitgeist' 'dockbarx' 'dockbarx-common' \
				 'xfce4-dockbarx-plugin' 'papirus-icon-theme'  \
				 'papirus-folders' 'conky-all' 'conky-manager' \
				 'xfdashboard' 'xfdashboard-plugins'
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					$installApp $app
				else
					echo $app " installed"
			fi	
		done
		sudo sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list
		if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		fi

	}



installation && exit


