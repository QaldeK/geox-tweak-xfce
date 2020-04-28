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
	mkdir -p $HOME/.conky
	tar -xf /usr/share/geox-tweak/theme/conky.tar.gz -C $HOME/.conky
	sudo cp -f /usr/share/geox-tweak/script/conkytoggle.sh	/usr/bin/conkytoggle.sh
	# Autostart
	mkdir -p $HOME/.config/autostart/
	cp -n /usr/share/geox-tweak/script/autostart/* $HOME/.config/autostart/
	# Geox-Tweak-Xfce
	cp /usr/share/geox-tweak/geox-tweak.conf $HOME/.config/geox-tweak-xfce
	cp -ru /usr/share/geox-tweak/panel/ $HOME/.config/geox-tweak-xfce


	echo '''#pulseaudio-button * {-gtk-icon-transform: scale(1);}
#xfce4-notification-plugin * {-gtk-icon-transform: scale(1);}
#xfce4-power-manager-plugin * {-gtk-icon-transform: scale(1);}''' >> $HOME/.config/gtk-3.0/gtk.css

	# configure plank
	xfconf-query -cv xfwm4 -p /general/show_dock_shadow -s "false"
	cp -Rfv /usr/share/geox-tweak/panel/plank/* $HOME/.config/plank/
	gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ dock-items " ['thunar.dockitem', 'firefox.dockitem', thunderbird.dockitem', 'org.xfce.Catfish.dockitem', 'libreoffice-startcenter.dockitem', 'exo-terminal-emulator.dockitem', 'xfce-settings-manager.dockitem'] "

	# Change gtx launcher after first run
	echo $pw | sudo -S  sed -i 's/firstrun.*/firstrun = no/' $HOME/.config/geox-tweak-xfce/geox-tweak.conf
	echo $pw | sudo -S  sed -i s'%./usr/share/geox-tweak/script/firstrun.sh%python3 /usr/share/geox-tweak/gtx_gui.py/'% /usr/share/applications/GeoX-Tweak.desktop
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



		_installConf


		echo "----------------------------------------------"
		echo "Procces terminate, press enter for quit"
		echo "----------------------------------------------"

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
		    echo $pw | sudo -S add_ppa:ricotz/docky
		    echo $pw | sudo -S add_ppa:xubuntu-dev/extras
		    echo $pw | sudo -S add_ppa:xuzhen666/dockbarx
		    echo $pw | sudo -S add_ppa:papirus/papirus
		    echo $pw | sudo -S add_ppa:synapse-core/testing
		    echo $pw | sudo -S apt-get update
	fi
	}

_reposMX()
	{
		echo $pw | sudo sed -i "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list
		echo $pw | sudo apt-get update
	}

_installationUnbuntu()
	{
		installApp="sudo apt-get install -y "

		_repoUbuntu


		for app in 'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist'\
		 'dockbarx' 'dockbarx-themes-extra' 'xfce4-dockbarx-plugin' 'conky-all' 
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


		wget http://launchpadlibrarian.net/340091846/realpath_8.26-3ubuntu4_all.deb
		wget https://github.com/teejee2008/conky-manager/releases/download/v2.4/conky-manager-v2.4-amd64.deb
		echo $pw | sudo dpkg -i realpath_8.26-3ubuntu4_all.deb conky-manager-v2.4-amd64.deb
		rm $HOME/realpath_8.26-3ubuntu4_all.deb
		rm $HOME/conky-manager-v2.4-amd64.deb

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
		echo $pw | sudo sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list
		if [ ! -e '/usr/share/libreoffice/share/config/images_papirus.zip' ]; then
			wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
		fi

	}

add_ppa() {
      for i in "$@"; do
        grep -h "^deb.*$i" /etc/apt/sources.list.d/* > /dev/null 2>&1
        if [ $? -ne 0 ]
        then
          echo "Adding ppa:$i"
          sudo add-apt-repository -y ppa:$i
        else
          echo "ppa:$i already exists"
        fi
      done
    }

installation && exit


