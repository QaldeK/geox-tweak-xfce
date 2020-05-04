#!/usr/bin/env python3

import configparser  # traiter les fichiers de configuration
import os
import os.path
import subprocess  # os et subprocess : executer des commandes et script bash
from os.path import expanduser

import gi  # nécessaire pour utiliser le fichier glade
# nécessaire pour utiliser le fichier glade/ GObject?
from gi.repository import Gtk

gi.require_version('Gtk', '3.0')

home = expanduser("~")  # path home de l'user
sdir = os.path.dirname(os.path.abspath(__file__))  # path du script py

paneldir = home + '/.config/geox-tweak-xfce/panel/'
config = configparser.ConfigParser()
gtconf = home + '/.config/geox-tweak-xfce/geox-tweak.conf'


class GeoxTweak:

    def __init__(self):

        # TODO :  copier def
        self.var_adapta = ""
        self.var_arc = ""
        # config.read(gtconf)     # Lire la configuration tel que loggué
        config.read(gtconf)
        self.conf_actual()




    def conf_actual(self):

        # TODO no more need config.get for theme windows_decor and icons ?
        self.theme = subprocess.getoutput(
            "xfconf-query -c xsettings -p /Net/ThemeName")
        self.windows_decor = subprocess.getoutput(
            "xfconf-query -c xfwm4 -p /general/theme")
        self.icons = subprocess.getoutput(
            "xfconf-query -c xsettings -p /Net/IconThemeName")
        self.libreoffice_icons = config.get('Style', 'libreoffice_icons')

        self.folder = config.get('Style', 'folder')
        self.plank_theme = config.get('Style', 'plank_theme')

        config.set('Style', 'theme', self.theme)
        config.set('Style', 'windows_decor', self.windows_decor)
        config.set('Style', 'icons', self.icons)

        if '-dark' in self.theme:
            config.set('Style', 'dark_theme', 'yes')

        elif'Nokto' in self.theme:
            config.set('Style', 'dark_theme', 'yes')

        elif'-Dark' in self.theme:
            config.set('Style', 'dark_theme', 'yes')

        else:
            config.set('Style', 'dark_theme', 'no')

        config.write(open(gtconf, 'w'))

# @ GTK/icon/libreofficeicons/plank Theme_________________

    def change_theme(self, change_folder=True):

        # TODO: theme Materia !
        if "Adapta" in self.theme:
            theme = self.theme + self.var_adapta
        # Pour theme arc : theme hdpi
        elif "Arc" in self.theme:
            theme = self.theme + self.var_arc
        else:
            theme = self.theme
      
        subprocess.run('''notify-send "GTX-Indicator" " "Switch theme >> ''' + theme + '''" -t 5000''', shell=True)


        subprocess.Popen(
            '''xfconf-query -c xsettings -p /Net/IconThemeName -s ''' +
            self.icons + "; ",
            shell=True)
        print("new icon theme : " + self.icons)

        subprocess.Popen(
            '''xfconf-query -c xfwm4 -p /general/theme -s ''' +
            self.windows_decor + "&",
            shell=True)  # Decoration pour le compositeur xfwm4 (et compton?)
        print("new windows decorator theme : " + self.windows_decor)


        subprocess.Popen(
            '''xfconf-query -c xsettings -p /Net/ThemeName -s ''' +
            theme + " &",
            shell=True)
        print("new theme : " + theme)

        if config.get('Style', 'libreoffice_icons') != self.libreoffice_icons:

            subprocess.Popen('''
                if [ ! -e "$HOME/.config/libreoffice/4/user/registrymodifications.xcu ]; then
                sed -i s'#"SymbolStyle" oor:op="fuse"><value>.*</value></prop></item>#"SymbolStyle" oor:op="fuse"><value>'''
                + self.libreoffice_icons +
                '''</value></prop></item>'# $HOME/.config/libreoffice/4/user/registrymodifications.xcu ;
                sed -i s'#papirus</item>#''' + self.libreoffice_icons +
                '''</value></prop></item>'# $HOME/.config/libreoffice/4/user/registrymodifications.xcu 
                fi 
                ''', shell=True)

            config.set('Style', 'libreoffice_icons', self.libreoffice_icons)
            
        print("libreoffice icon style : " + self.libreoffice_icons)

        if change_folder:
            if config.get('Style', 'folder') != self.folder:
                self.change_folder_color()

        if config.get('Style', 'plank_theme') != self.plank_theme:
            subprocess.check_call(
                "gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "
                + self.plank_theme + " ;",
                shell=True)

            config.set('Style', 'plank_theme', self.plank_theme)
            print('new plank theme : ' + self.plank_theme)

        # inscription dans le fichier geox-tweak.conf des options selectionnees
        # config. fonction pour les fichiers structurés comme les fichier .ini
        config.set('Style', 'theme', self.theme)
        config.set('Style', 'windows_decor', self.windows_decor)
        config.set('Style', 'icons', self.icons)

        if '-dark' in self.theme:
            config.set('Style', 'dark_theme', 'yes')

        elif '-Darker' in self.theme:
            config.set('Style', 'dark_theme', 'no')

        elif'Nokto' in self.theme:
            config.set('Style', 'dark_theme', 'yes')

        elif'-Dark' in self.theme:
            config.set('Style', 'dark_theme', 'yes')

        else:
            config.set('Style', 'dark_theme', 'no')

        config.write(open(gtconf, 'w'))

    def theme_var(self, var_arc="", var_adapta=""):
        self.var_arc = var_arc
        self.var_adapta = var_adapta

    def select_theme(self, theme='', windows_decor='',
                     icons_name='Papirus', libreoffice_icons='papirus',
                     folder_color='blue', plank_theme='geox-dark'):
        self.theme = theme
        self.windows_decor = windows_decor
        self.icons = icons_name

        # if self.libreoffice_icons != config.get('Style', 'libreoffice_icons'):
        self.libreoffice_icons = libreoffice_icons

        # if self.folder != config.get('Style', 'folder'):
        self.folder = folder_color

        # if self.plank_theme != config.get('Style', 'plank_theme'):
        self.plank_theme = plank_theme

    # Folder ICON COLOR ___________________
    def on_folderc(self, folderc):
        self.folder = folderc
        self.change_folder_color()

    def change_folder_color(self):
        ''' change folder icon color for papirus icons theme '''

        cfolder = self.folder
        # import pdb; pdb.set_trace()
        script = '''#!/bin/bash
Theme=$(xfconf-query -c xsettings -p /Net/IconThemeName)
xfce4-terminal -e "sudo papirus-folders -t $Theme -C ''' + cfolder + ''' " '''

        subprocess.Popen(script, shell=True)

        config.set('Style', 'folder', cfolder)
        config.write(open(gtconf, 'w'))
        print("new folder color : " + cfolder)

    def dark_mode(self):
        self.theme = subprocess.getoutput(
            "xfconf-query -c xsettings -p /Net/ThemeName")
        dtheme = self.theme
        
        if 'Mint' in dtheme:
            if 'Darker' in dtheme:
                darktheme = dtheme.replace('Darker', 'Dark')
            else:
                darktheme = dtheme[:6] + '-Dark' + dtheme[6:]

        elif 'Matcha' in dtheme:
            darktheme = dtheme[:6] + '-dark' + dtheme[6:]

        elif 'Adapta' in dtheme:
            if 'Eta' in dtheme:
                darktheme = dtheme.replace('Eta', 'Nokto-Eta')
                wdarktheme = dtheme
            else:
                darktheme = dtheme + '-Nokto'

        elif 'Arc' in dtheme:
            darktheme = dtheme + '-Dark'

        elif 'MJV' in dtheme:
            darktheme = 'McOS-MJV-Dark-XFCE-Edition-2.3'

        elif 'Materia' in dtheme or 'Qogir' in dtheme or 'Adwaita' in dtheme:
            darktheme = dtheme + '-dark'
            darktheme = darktheme.replace('-light', '')

        else:
            subprocess.run('''notify-send "GTX-Indicator" " ''' + self.theme + ''' have no dark-theme option" -t 5000''', shell=True)

        if '-Eta' in darktheme:
            wdarktheme = darktheme.replace('-Eta', '')

        else:
            wdarktheme = darktheme


        print(darktheme)
        self.select_theme(
            theme=darktheme,
            windows_decor=wdarktheme,
            icons_name="Papirus-Dark",
            libreoffice_icons="papirus-dark",
            )

        self.change_theme(change_folder=False)               

    def light_mode(self):

        self.theme = subprocess.getoutput(
            "xfconf-query -c xsettings -p /Net/ThemeName")
        lighttheme = self.theme

        if 'Adapta' in self.theme:
            lighttheme = lighttheme.replace('-Nokto', '')

        elif 'Arc' in self.theme:
            lighttheme = lighttheme.replace('-Dark', '')

        elif 'MJV' in self.theme:
            lighttheme = 'McOS-MJV-XFCE-Edition-2.3'

        elif 'Matcha' in self.theme:
            lighttheme = lighttheme.replace('-dark', '')

        elif 'Materia' in self.theme or 'Qogir' in self.theme or 'Adwaita' in self.theme:
            lighttheme = lighttheme.replace('-dark', '')

        elif 'Mint' in self.theme:
            lighttheme = lighttheme.replace('-Dark', '')

        else:
            subprocess.run('''notify-send "GTX-Indicator" " ''' + self.theme + ''' have no dark-theme option" -t 5000''', shell=True)


        if 'Eta' in self.theme:
            wlighttheme = lighttheme.replace('-Eta', '')
        else:
            wlighttheme = lighttheme

        print(lighttheme)
        self.select_theme(
            theme=lighttheme,
            windows_decor=wlighttheme,
            icons_name="Papirus",
            libreoffice_icons="papirus"
        )


        self.change_theme(change_folder=False)



# class Commands():
#    def cmd_foo(self):
#        print("Foo")

#    def callFunction(self, name):
#        fn = getattr(self, 'cmd_'+name, None)
#        if fn is not None:
#             fn()

#         method_to_call = getattr(foo, 'bar')
#         result = method_to_call()


#@ Desktop Layout ___________

    def change_layout(self, layout):
        """ Change xfce panel orientations and plugins """
        args = '''xfce4-panel --quit; pkill xfconfd; rm -Rf ~/.config/xfce4/panel; \
         cp -Rf ''' + paneldir + layout + '''/xfce4/panel ~/.config/xfce4/panel; \
                    cp -f ''' + paneldir + layout + '''/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml \
                    ~/.config/xfce4/xfconf/xfce-perchannel-xml; \
                    sleep 2; xfce4-panel &'''

        subprocess.check_call(args, shell=True)
        config.set('Style', 'layout', layout)
        config.write(open(gtconf, 'w'))


    def plank_config(self, pinned, offset, position, theme):
        args = "gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ pinned-only " + pinned + " ; \
                gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ offset " + offset + " ; \
                gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ position " + position + " ; \
                gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme " + theme + " ;"
        subprocess.Popen(args, shell=True)
        config.set('Style', 'plank_theme', theme)
        config.write(open(gtconf, 'w'))

   # path des fichiers de conf !!
    # TODO > config dockbarx : /home/geo/.gconf/apps/dockbarx/%gconf.xml

    def dockbarx_config(self, launcher, theme, the_me):
        args0 = "pkill -f dockbarx-plug "
        args1 = '''gconftool-2 --type list --list-type string --set /apps/dockbarx/launchers "''' + \
            launcher + '''" '''
        args2 = '''gconftool-2 --type string --set /apps/dockbarx/theme "''' + theme + '''" '''
        args3 = ''' gconftool-2 --type string --set /apps/dockbarx/themes/''' + \
            the_me + '''/popup_style_file Magic_trans.tar.gz '''
        subprocess.Popen(args0, shell=True)
        subprocess.check_call(args1, shell=True)
        subprocess.check_call(args2, shell=True)
        subprocess.check_call(args3, shell=True)

    # TODO > if css exist but not line !!
    def pulseaudio_config(self, size):
        """ Workaround : Change gtk.css for not have BIG pulseaudio 
        (and other) icon plugins on large panel """
        gtkcss = os.path.expanduser('~/.config/gtk-3.0/gtk.css')
        args1 = "sed -i s'/{-gtk-icon-transform: scale(.*);}/{-gtk-icon-transform: scale(" + \
            size + ");}'/ $HOME/.config/gtk-3.0/gtk.css "
        gtktransform = '''
 #pulseaudio-button * {-gtk-icon-transform: scale(''' + size + ''');} 
 #xfce4-notification-plugin * {-gtk-icon-transform: scale(''' + size + ''');} 
 #xfce4-power-manager-plugin * {-gtk-icon-transform: scale(''' + size + ''');}'''

        if not os.path.isfile(gtkcss):
            file = open(gtkcss, 'w')
            file.write(gtktransform)
        else:
              subprocess.call(args1, shell=True)

    def app_activ(self, app, xf='', xd='', ck='', nt=''):
        """ s'execture quand les logiciels tiers sont activés, avec les arguments définis
        dans on_app_toggled, permettant de s'adapter aux specificité
        d'exectution/extinction des app """

        args = nt + app + ck + xd + "&"
        subprocess.check_call(args, shell=True)

        os.system('''
            find $HOME/.config/autostart -iname '*''' + app + '''*' -exec sed -i 's/Hidden=true.*/\Hidden=false/' {} \;'''
                  )
        os.system('''
            find $HOME/.config/autostart -iname '*''' + app + '''*' -exec sed -i 's/X-GNOME-Autostart-enabled=false.*/\X-GNOME-Autostart-enabled=true/' {} \;'''
                  )

    def app_inactiv(self, app, pkill, xf='', xq='', nt=''):
        """ s'execture quand les logiciels tiers sont activés;
        modifie les fichier .desktop du dossier autostart """

        args = pkill + nt + app + xq + "&"
        subprocess.check_call(args, shell=True)

        os.system('''
            find $HOME/.config/autostart -iname '*''' + app + '''*' -exec sed -i 's/Hidden=false.*/\Hidden=true/' {} \;'''
                  )
        os.system('''
            find $HOME/.config/autostart -iname '*''' + app + '''*' -exec sed -i 's/X-GNOME-Autostart-enabled=true.*/\X-GNOME-Autostart-enabled=false/' {} \;'''
                  )

    def activ_app(self, app):

        ck = xf = xd = nt = ""

        if app == "conky":
                ck = "toggle.sh"  
                #FIXIT : dép:  conky est lancé par conkytoggle.sh >> OK ?
                self.app_activ(app, xf, xd, ck, nt)

        elif app == "xfdashboard":
            xf = "-autostart"
            xd = " -d"
            self.app_activ(app, xf, xd, ck, nt)

        elif app == "notes":
            xf = "-autostart"
            nt = "xfce4-"
            self.app_activ(app, xf, xd, ck, nt)

        else:
            self.app_activ(app, xf, xd, ck, nt)

    def inactiv_app(self, app):

        xf = xq = nt = ""
        pkill = "pkill "

        if app == "conky":
            self.app_inactiv(app, pkill, xf, xq, nt)

        elif app == "xfdashboard":
            xf = "-autostart"
            xq = " -q"
            pkill = ""
            self.app_inactiv(app, pkill, xf, xq, nt)

        elif app == "notes":
            xf = "-autostart"
            nt = "xfce4-"
            self.app_inactiv(app, pkill, xf, xq, nt)

        else:
            self.app_inactiv(app, pkill, xf, xq, nt)

    def conky_remove(self, conky):
        ''' gtx-indicator function for hide conky'''

        ckdir = '''conky -c "$HOME/.conky/Geox/'''
        ckremove = ckdir + conky
        ckstart = home + '''/.conky/conky-startup.sh'''

        ckrm = [conky, 'cd', '/home']
        print(ckremove)

        #Del lines contain ckrm
        with open(ckstart,"r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if not any(ckrmv in line for ckrmv in ckrm):
                    f.write(line)
            f.truncate()

        subprocess.run(sdir + "/script/conkyaddrm.sh")

    def conky_add(self, conky):
        ''' gtx-indicator function for show conky'''

        ckdir = '''\nconky -c "$HOME/.conky/Geox/'''
        ckadd = ckdir + conky
        ckstart = home + '''/.conky/conky-startup.sh'''

        with open(ckstart,"r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                # for cleaning the lines adding by conky-manager 
                # when it close without active conky
                if "exit 0" not in line and "# No widgets enabled!" not in line:
                    f.write(line)
            f.truncate()

        with open(ckstart, "a") as f:
            f.write(ckadd)

        subprocess.run(sdir + "/script/conkyaddrm.sh")


########################
