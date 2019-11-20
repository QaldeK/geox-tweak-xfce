	#!/bin/bash
	
share="/usr/share"
gt=geox-tweak

_configure()
	{ #FIXIT : pas de mot de passe, ou bien prend HOME pour root
	xfce4-terminal -e ''' echo "Process to geox-tweak-xfce configuration." ; \
			" sudo bash cp -v -R $share/geox-tweak/theme/plank/* $share/plank/ ;\
			cp -v -R $share/geox-tweak/theme/xfdashboard/xfdashboard-dark-nodock/* $share/themes/xfdashboard-dark-nodock/"'''
	cp -v -R $share/geox-tweak/theme/dockbarx/* ~/.gconf/apps/
	cp -v -f $share/geox-tweak/theme/xfdashboard/xfdashboard.xml ~/.config/xfce4/xfconf/
	cp -v -f $share/geox-tweak/theme/synapse/config.json $HOME/.config/synapse/
	cp -v -Rf $share/geox-tweak/theme/conky/* ~/.conky/
	# chmod +x $share/geox-tweak/script/*
	# chmod 666 $share/geox-tweak/activ.conf
	# chmod +x $share/geox-tweak
	# chmod +x $share/geox-tweak/GeoX-Tweak.desktop
	# chmod +x $share/applications/GeoX-Tweak.desktop
	# chmod +x /usr/bin/geox-tweak



	#preserve whiskermenu config.
	path_panel=$share/geox-tweak/panel
	find $HOME/.config/xfce4/panel/ -name "whisker*" -exec cp -f -r -v {} $path_panel/whiskermenu-20.rc \;
	find $path_panel/*/.config/xfce4/panel/  -maxdepth 0 -exec cp -f -v $path_panel/whiskermenu-20.rc {} \;
	
	}

_firstrunOk()
	{ 	# change firstrun value
	sed -i 's/firstrun.*/firstrun = no/' $HOME/.config/geox-tweak-xfce/geox-tweak.conf
}

_configure && _firstrunOk 
