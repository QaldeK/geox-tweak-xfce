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

# which yad > /dev/null
# if [ $? = 1 ];
# then
# 	echo "Install yad"
# 	x-terminal-emulator -e "echo Install yad ; \
# 			sudo apt-get install -y yad"
# else
# 	echo "yad OK"
# fi




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
    find $HOME/.config/geox-tweak-xfce -iname 'geox-tweak.conf' -exec sed -i 's/sxcdp.*/\sxcdp = error/' {} \;

    yad ${config} --title="Error" --text="${error}"  --width 800 --height 500
}

_installConf()
{
	share="/usr/share"
	gt=geox-tweak	
	echo "Install Plank, synapse, conky and xfdashboard extra theme and config file"
	mkdir -p $HOME/.gconf/apps/
	cp -v -Rf $share/geox-tweak/theme/dockbarx/* $HOME/.gconf/apps/
	echo $pw | sudo -S cp -v -Rf $share/geox-tweak/theme/plank/* $share/plank/
	echo $pw | sudo -S cp -v -Rf $share/geox-tweak/theme/xfdashboard/xfdashboard-dark-nodock/* $share/themes/xfdashboard-dark-nodock/
	cp -v -f $share/geox-tweak/theme/xfdashboard/xfdashboard.xml $HOME/.config/xfce4/xfconf/xfce-perchannel-xml 

	mkdir -p $HOME/.config/synapse/
	cp -v -f $share/geox-tweak/theme/synapse/* $HOME/.config/synapse/
	cp -v -Rf $share/geox-tweak/theme/conky/* $HOME/.conky/
	cp -v $share/geox-tweak/geox-tweak.conf $HOME/.config/geox-tweak-xfce
}

installation() 
	{ 
		
		if [ $os = "MX" ] || [ os = "Debian" ]; then
			_installationMX
		elif [ $os = "Ubuntu" ] || [ $os = "LinuxMint" ] ; then
			_installationUnbuntu
		fi

		echo $pw | sudo -S tar -xf /usr/share/geox-tweak/themes.tar.gz -C /usr/share/themes/ --skip-old-files

		_installConf

	}

_repoUbuntu()
	{
		echo $pw | sudo -S add-apt-repository -y ppa:ricotz/docky
		echo $pw | sudo add-apt-repository ppa:xubuntu-dev/extras
		echo $pw | sudo -S add-apt-repository -y ppa:xuzhen666/dockbarx
		echo $pw | sudo -S add-apt-repository -y ppa:papirus/papirus
		echo $pw | sudo add-apt-repository ppa:synapse-core/
		echo $pw | sudo apt-get update
	}

_reposMX()
	{
		echo $pw | sudo -S sed -i "/^#deb.*test/s/^#//g" /etc/apt/sources.list.d/mx.list
		if [ $distrib == "MX19" ] ; then
		echo $pw | sudo -S sh -c "echo 'deb http://ppa.launchpad.net/xuzhen666/dockbarx/ubuntu disco main' > /etc/apt/sources.list.d/xuzhen666-ubuntu-dockbarx-disco.list"
		echo $pw | sudo -S apt-key adv --recv-keys --keyserver keyserver.ubuntu.com  77d026e2eead66bd
		fi
		echo $pw | sudo -S apt-get update
	}

_installationUnbuntu()
	{
		installApp="echo $pw | sudo -S apt-get install -y "

		_repoUbuntu

		wget http://launchpadlibrarian.net/340091846/realpath_8.26-3ubuntu4_all.deb
		wget https://github.com/teejee2008/conky-manager/releases/download/v2.4/conky-manager-v2.4-amd64.deb
		echo $pw | sudo -S dpkg -i realpath_8.26-3ubuntu4_all.deb conky-manager-v2.4-amd64.deb

		for app in 'plank' 'xfdashboard' 'xfdashboard-plugins' 'synapse' 'zeitgeist' 'dockbarx' 'dockbarx-themes-extra' 'xfce4-dockbarx-plugin' 'conky-all' 'conky-manager'
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					echo $app installation ...
					$installApp $app

				else
					echo $app installed
			fi	
		done

		if [ ! -d "/usr/share/icons/Papirus"  ] ; then
			$installAPP papirus-icon-theme
		fi
		if [ ! -e "/usr/bin/papirus-folders" ]; then
			$installApp papirus-folders
			$installApp libreoffice-style-papirus
		fi


	}

_installationMX()
	{
		installApp="echo $pw | sudo -S apt-get install -y "
		_reposMX
		for app in 'plank'  'synapse' 'zeitgeist' 'dockbarx' 'dockbarx-themes-extra' \
				 'xfce4-dockbarx-plugin' 'papirus-icon-theme' 'libreoffice-style-papirus' \
				 'papirus-folders' 'conky-all' 'conky-manager' 'xfdashboard' 'xfdashboard-plugins'
			do
				if [ $(dpkg-query -W -f='${Status}' $app 2>/dev/null | grep -c "ok installed") -eq 0 ];
				then
					$installApp $app
			fi	
		done
		echo $pw | sudo -S sed -i 's/.* test/#&/'  /etc/apt/sources.list.d/mx.list
		wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-libreoffice-theme/master/install-papirus-root.sh | sh
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



