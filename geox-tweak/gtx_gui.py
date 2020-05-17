#!/usr/bin/env python3


# GeoX-Tweak-Xfce
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

import subprocess  # os et subprocess : executer des commandes et script bash
from os.path import expanduser
import os.path
import os
import configparser  # traiter les fichiers de configuration
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import shutil
from geox_tweak_xfce import GeoxTweak

home = expanduser("~")  # path home de l'user
sdir = os.path.dirname(os.path.abspath(__file__))  # path du script py
paneldir = home + '/.config/geox-tweak-xfce/panel/'
savedLayoutDir = paneldir + 'saved_layout/'
config = configparser.ConfigParser()
gtconf = home + '/.config/geox-tweak-xfce/geox-tweak.conf'


class Geox:
    def on_main_window_destroy(self, data=None):
        Gtk.main_quit()

    # @ INIT______________________________________________
    def __init__(self):
        """ Initialisation : chargement du gtk builder 
        lisant le fichier glade ..."""

        self.builder = Gtk.Builder()
        glade_file = os.path.join(sdir, "geox_0.3.glade")
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)
        go = self.builder.get_object

        self.gtweak = GeoxTweak()

    # @ bouton pref
        self.btn_plank_pref = go("btn_plank_pref")
        self.btn_xfdashboard_pref = go("btn_xfdashboard_pref")
        self.btn_conky_pref = go("btn_conky_pref")
        self.btn_notes_pref = go("btn_notes_pref")
        self.btn_ddterm_pref = go("btn_ddterm_pref")

    # @ Toogle Tools
        self.plank = go("plank")
        self.xfdashboard = go("xfdashboard")
        self.synapse = go("synapse")
        self.conky = go("conky")
        self.ddterm = go("ddterm")
        self.notes = go("notes")
        self.gtxi = go("gtxi")

    # @    # Toggle Help TODO A traduire avant d'activer ?
        self.btn_plank_help = go("btn_plank_help")
        self.btn_xfdashboard_help = go("btn_xfdashboard_help")
        self.btn_synapse_help = go("btn_synapse_help")
        self.btn_conky_help = go("btn_conky_help")
        self.btn_notes_help = go("btn_notes_help")

        self.help_txt_zone = go("help_txt_zone")
        self.defaut_help()

    # @ Layout preview
        self.geox = go("geox")
        self.geox.set_from_file(sdir + "/img/pv-geox.png")
        self.xubuntu = go("xubuntu")
        self.xubuntu.set_from_file(sdir + "/img/pv-xubuntu.png")
        self.ubuntu = go("ubuntu")
        self.ubuntu.set_from_file(sdir + "/img/pv-ubuntu.png")
        self.W95 = go("W95")
        self.W95.set_from_file(sdir + "/img/pv-W95.png")
        self.W7 = go("W7")
        self.W7.set_from_file(sdir + "/img/pv-W7.png")
        self.budgie = go("budgie")
        self.budgie.set_from_file(sdir + "/img/pv-budgie.png")
        self.mate = go("mate")
        self.mate.set_from_file(sdir + "/img/pv-mate.png")
        self.mxlinux = go("mxlinux")
        self.mxlinux.set_from_file(sdir + "/img/pv-mxlinux.png")

        # self.cb_adapta = go("cb_adapta")
        self.btn_all_theme = go("btn_all_theme")
        self.btn_widows_decor = go("btn_widows_decor")
        self.btn_apply = go("btn_apply")
        self.toggle_adapta_compact = go("toggle_adapta_compact")

    # @ Onglet "Other"
        self.btn_simpleclic_thunar = go("btn_simpleclic_thunar")
        self.btn_simpleclic_desktop = go("btn_simpleclic_desktop")
        self.btn_txt_next_icons = go("btn_txt_next_icons")
        self.btn_folder_file = go("btn_folder_file")
        self.btn_removable_desktop = go("btn_removable_desktop")
        self.btn_trash_desktop = go("btn_trash_desktop")
        self.btn_allhome_desktop = go("btn_allhome_desktop")
        self.btn_home_desktop = go("btn_home_desktop")
        self.btn_xfce_settings = go("btn_xfce_settings")
        self.btn_lightdm_settings = go("btn_lightdm_settings")
        self.btn_xfwm4_tweaks_settings = go("btn_xfwm4_tweaks_settings")
        self.btn_notification_settings = go("btn_notification_settings")
        self.btn_panel_settings = go("btn_panel_settings")
        self.btn_desktop_settings = go("btn_desktop_settings")
        self.btn_thunar_settings = go("btn_thunar_settings")

    # @ POPOVER windows decor
        # self.popover_wd = go("popover_wd")
        # self.preview_wd_arc_light = go('preview_wd_arc_light')
        # self.preview_wd_arc_light.set_from_file(sdir + '/img/wd_arc_light.png')

    # @ preview self.theme
        self.preview_adapta = go("preview_adapta")
        self.preview_adapta.set_from_file(sdir + "/img/adapta.png")
        self.preview_various = go("preview_various")
        self.preview_various.set_from_file(sdir + "/img/various.png")
        self.preview_matcha = go("preview_matcha")
        self.preview_matcha.set_from_file(sdir + "/img/matcha-sea.png")
        self.preview_arc = go("preview_arc")
        self.preview_arc.set_from_file(sdir + "/img/arc.png")
        self.preview_mint = go("preview_mint")
        self.preview_mint.set_from_file(sdir + "/img/mint-y.png")
        self.preview_qogir = go("preview_qogir")
        self.preview_qogir.set_from_file(sdir + "/img/qogir.png")

    # @ Icon color
        self.folder = ""

        self.icon_black = go("icon_black")
        self.icon_black.set_from_file(sdir + "/img/black.svg")
        self.icon_cyan = go("icon_cyan")
        self.icon_cyan.set_from_file(sdir + "/img/cyan.svg")
        self.icon_green = go("icon_green")
        self.icon_green.set_from_file(sdir + "/img/green.svg")
        self.icon_blue = go("icon_blue")
        self.icon_blue.set_from_file(sdir + "/img/blue.svg")
        self.icon_bluegrey = go("icon_bluegrey")
        self.icon_bluegrey.set_from_file(sdir + "/img/bluegrey.svg")
        self.icon_brown = go("icon_brown")
        self.icon_brown.set_from_file(sdir + "/img/brown.svg")
        self.icon_teal = go("icon_teal")
        self.icon_teal.set_from_file(sdir + "/img/teal.svg")
        self.icon_orange = go("icon_orange")
        self.icon_orange.set_from_file(sdir + "/img/orange.svg")
        self.icon_red = go("icon_red")
        self.icon_red.set_from_file(sdir + "/img/red.svg")
        self.icon_violet = go("icon_violet")
        self.icon_violet.set_from_file(sdir + "/img/violet.svg")
        self.icon_yellow = go("icon_yellow")
        self.icon_yellow.set_from_file(sdir + "/img/yellow.svg")
        self.icon_grey = go("icon_grey")
        self.icon_grey.set_from_file(sdir + "/img/grey.svg")

    # @ Configuration xfce actuelle / Etat des logiciel tiers
        self.state_settings()

        # /!\ Positionner apres la declaration des btn rapportées aux états
        # testés ;
        self.state_app(self)
        self.state_gtxi()
        self.on_btn_install_miss_clicked = go('on_btn_install_miss_clicked')

    # @ APP missing
        self.warning_app_miss = go("warning_app_miss")
        self.txt_app_miss = go("txt_app_miss")
        self.status_app_dep()    

    # @ Bar Theme : Apply / install / rmv
        self.apply_bar_theme = go('apply_bar_theme')
        self.apply_bar_theme.hide()
        self.install_bar_theme = go("install_bar_theme")
        self.install_bar_theme.hide()
        self.rm_theme = go('rm_theme')

        # self.on_rm_theme_clicked = go('on_rm_theme_clicked')

    # @    # ID des label du fichier de configuration geox-tweak.conf (> modifié par "config.")
        self.var_theme = ""
        self.theme = ""
        self.windows_decor = ""
        self.icons = ""
        self.layout = ""
        self.libreoffice_icons = ""

        # TODO : Renommer (confusion) assigné glade...
        self.theme_name = go("theme_name")

        self.chk_folder_color = go("chk_folder_color")

    # @ Save Layout
        # self.ls_layout = Gtk.ListStore(str)

        # self.tv_layouts = go('tv_layouts')
        self.tv_layouts = self.builder.get_object('tv_layouts')
        self.tmodel = self.tv_layouts.get_model()
        self.entry_layout = go('entry_layout')
        self.slayout_list()

    # @ affichage de la fenetre
        self.window = go("main_window")
        self.window.show()

        config.read(gtconf)
        plank_theme = config.get("Style", "plank_theme")
        self.plank_theme = plank_theme

    @staticmethod
    def on_btn_quit_clicked(widget):
        Gtk.main_quit()

    def defaut_help(self):
        defaut = ""
        self.help_txt_zone.get_buffer().set_text(defaut)


    # @ pane :Panel layout ###############################

    # @ Status App / Installed ?
    def status_app_dep(self):
        '''check if the other software are install
        Show a warning if not'''
        
        #TODO GtkwarningDialog ?

        self.warning_app_miss.hide()

        app_miss = []
        app_test = ['plank', 'xfdashboard',
                    'xfce4-dockbarx-plugin', 'synapse', 'gconf2',
                    'xfce4-datetime-plugin', 'conky']

        for app in app_test:
            script = '''dpkg-query -W -f='${Status}' ''' + \
                app + ''' >/dev/null '''

            if subprocess.call(script, shell=True):
                app_miss += [app]

        # Si liste non-vide
        if (app_miss):
            warning_txt = ('''Some software necessary are not installed : '''
                           + str(app_miss) + '''
                           Some layout will don't work properly. Please click on "install it" or try to install them manually ''')
          
            self.txt_app_miss.set_label(warning_txt)
            self.warning_app_miss.show()


    def on_btn_install_miss_clicked(self, widget):
        script = sdir + '/script/firstrun.sh'
        subprocess.run("xfce4-terminal -e " + script, shell=True)
        self.warning_app_miss.hide()
        self.status_app_dep()

    # @ Verification de l'etat des logiciels (actif ou pas)

    def state_gtxi(self):
        arg = '''pgrep -f "gtx_indicator.py" &>/dev/null'''
        test_gtxi = subprocess.run(arg, shell=True, stdout=subprocess.PIPE)
        if not test_gtxi.stdout:
            self.gtxi.handler_block_by_func(self.on_gtxi_toggled)
            self.gtxi.set_active(False)
            self.gtxi.handler_unblock_by_func(self.on_gtxi_toggled)
            self.gtxi.set_label("off")
        else:
            self.gtxi.handler_block_by_func(self.on_gtxi_toggled)
            self.gtxi.set_active(True)
            self.gtxi.handler_unblock_by_func(self.on_gtxi_toggled)
            self.gtxi.set_label("on")

    def state_app(self, widget):
        # dictinnaire des app a verifier
        apps = {
            "synapse": self.synapse,
            "plank": self.plank,
            "xfdashboard": self.xfdashboard,
            "conky": self.conky,
            "xfce4-notes": self.notes,
        }

        prefapps = {
            "plank": self.btn_plank_pref,
            "xfdashboard": self.btn_xfdashboard_pref,
            "conky": self.btn_conky_pref,
            "xfce4-notes": self.btn_notes_pref
        }

        appactive = bool

        # Verifie si le logiciel est actif
        for app in apps.keys():
            selfapp = apps[app]

            if os.system("pidof " + app +
                         " >/dev/null 2>&1"):  # /!\ Renvoie True si non-actif
                self.app_state(selfapp, appactive(True))

            else:
                self.app_state(selfapp, appactive(False))

        for prefapp in prefapps.keys():
            selfprefapp = prefapps[prefapp]
            if os.system("pidof " + prefapp + " >/dev/null 2>&1"):
                self.state_btn_pref(selfprefapp, appactive(True))

            else:
                self.state_btn_pref(selfprefapp, appactive(False))

    def app_state(self, selfapp, appactive):
        """ Adapter le label on/off en fonction de l'etat des logiciels"""

        if appactive:
            # Bloque la fonction du bouton pour pouvoir changer
            # son état sans l'activer
            selfapp.handler_block_by_func(self.on_app_toggled)
            selfapp.set_active(False)
            selfapp.handler_unblock_by_func(self.on_app_toggled)
            selfapp.set_label("off")

        else:
            selfapp.handler_block_by_func(self.on_app_toggled)
            state = selfapp.get_active()
            selfapp.set_active(not state)
            selfapp.handler_unblock_by_func(self.on_app_toggled)
            selfapp.set_label("on")

    @staticmethod
    def state_btn_pref(selfprefapp, appactive):

        if appactive:
            selfprefapp.hide()

        else:
            selfprefapp.show()

    # @ TOOLS : Bouton Toggle des App tieres

    def on_gtxi_toggled(self, widget):
        if widget.get_active():
            subprocess.Popen(
                'python3 /usr/share/geox-tweak/gtx_indicator.py', shell=True)
            widget.set_label("on")
            subprocess.Popen('''
                sed -i 's/Hidden=true.*/\Hidden=false/' /$HOME/.config/autostart/gtx-indicator.desktop''', shell=True)

        else:
            subprocess.Popen('pkill -f gtx_indicator.py', shell=True)
            widget.set_label("off")
            subprocess.Popen('''
                sed -i 's/Hidden=false.*/\Hidden=true/' /$HOME/.config/autostart/gtx-indicator.desktop''', shell=True)

    def on_app_toggled(self, widget):
        """ Fonction permettant d'envoyer les commandes d'execution et
        d'extinction spécifique aux logiciels (notamment conky, lancer par
         le script conkyaddrm.sh, et xfdashboard lancer en mode démo """

        app = Gtk.Buildable.get_name(widget)
        ck = xf = xq = xd = nt = ""

        if widget.get_active():

            if app == "conky":
                self.btn_conky_pref.show()

            elif app == "xfdashboard":
                self.btn_xfdashboard_pref.show()

            elif app == "notes":
                self.btn_notes_pref.show()

            else:
                if app == "plank":
                    self.btn_plank_pref.show()

            self.gtweak.activ_app(app)
            widget.set_label("on")

        else:

            if app == "conky":
                self.btn_conky_pref.hide()

            elif app == "xfdashboard":
                self.btn_xfdashboard_pref.hide()

            elif app == "notes":
                self.btn_notes_pref.hide()

            else:
                if app == "plank":
                    self.btn_plank_pref.hide()

            self.gtweak.inactiv_app(app)
            widget.set_label("off")

    # Activé/Désactiver le démon du terminal drop-down de xfce
        # What ? : déjà en raccourci clavier !!
    def on_ddterm_toggled(self, widget):
        # TODO > xfconf query command & state app fct.
        if widget.get_active():
            os.system(
                '''xfce4-terminal --drop-down --hide-menubar --hide-toolbar''')
            self.btn_ddterm_pref.show()
        else:
            self.btn_ddterm_pref.hide()

    # Bouton préférences #########
    @staticmethod
    def on_btn_plank_pref_clicked(widget):
        os.system(''' plank --preferences ''')

    @staticmethod
    def on_btn_xfdashboard_pref_clicked(widget):
        os.system(''' xfdashboard-settings ''')

    @staticmethod
    def on_btn_conky_pref_clicked(widget):
        os.system(''' conky-manager ''')

    @staticmethod
    def on_btn_ddterm_pref_clicked(widget):
        os.system("xfce4-notes-settings")

    @staticmethod
    def on_btn_notes_pref_clicked(widget):
        os.system(''' xfce4-notes-settings ''')

    # Bouton Toggle HELP ############
    # TODO Trad et rendre de nouveau visible
    def on_btn_plank_help_clicked(self, widget):
        help_txt = _("PLANK est une barre de lancement d'application.")
        self.help_txt_zone.get_buffer().set_text(help_txt)

    def on_btn_synapse_help_clicked(self, widget):
        help_txt = _("Synapse permet lancer des \n "
                     "applications mais aussi de trouver et d'accéder rapidement aux documents et"
                     "fichiers désirés (en utilisant le moteur Zeitgeist)."
                     "Pour l'utiliser, appuyez sur les touches Ctrl+Espace, commencez à taper ce que vous cherchez"
                     "puis appuyez sur la touche Entrer pour ouvrir l'application ou le fichier sélectionné")
        self.help_txt_zone.get_buffer().set_text(help_txt)

    def on_btn_xfdashboard_help_clicked(self, widget):
        help_txt = _("Xfdashboard permet d'exposer les logiciels en cours d'execution \
        sous forme de miniature, à la manière de gnome 3. \
         Pointez votre curseur au coin en haut à gauche de l'écran pour l'activer")

        self.help_txt_zone.get_buffer().set_text(help_txt)

    def on_btn_conky_help_clicked(self, widget):
        help_txt = _(
            "Conky affiche des informations sur votre bureau (date, heure, CPU, RAM...")
        self.help_txt_zone.get_buffer().set_text(help_txt)

    def on_btn_ddterm_help_clicked(self, widget):
        help_txt = _(
            "Permet d'afficher un terminal déroulant en haut de l'écran.")
        self.help_txt_zone.get_buffer().set_text(help_txt)

    def on_btn_notes_help_clicked(self, widget):
        help_txt = _("Xfce4-notes permet d'écrire de petites notes et d'y acceder facilement \
         depuis la zone de notification")

        self.help_txt_zone.get_buffer().set_text(help_txt)


    # TODO  autre configuration : theme xfdashboard ? &

    # @ Layout backup


    def slayout_list(self):
        '''append ListStore from /saved_layout/slayouts'''
        for saved_layout in os.listdir(paneldir + 'saved_layout/'):
            self.tmodel.append([saved_layout])

    def on_entry_layout_icon_press(self, widget, Gtk_Entry_Icon_Secondary, event):
        '''Save actual Layout configuration and append to SavedListStore when btn clicked'''
        #FIXIT Add directory to firstrun/install_script 

        new_layout = self.entry_layout.get_text()
        new_layout = new_layout.replace(' ', '_')

        if new_layout not in os.listdir(paneldir + 'saved_layout/'):
            self.add_new_layout(new_layout)

        else:
            dialog = Gtk.MessageDialog(
                None,
                0,
                Gtk.MessageType.ERROR,
                Gtk.ButtonsType.CANCEL,
                "This layout name allready exist",
            )
            dialog.format_secondary_text(
                "Please choose an another name"
            )
            response = dialog.run()
            if response == Gtk.ResponseType.CANCEL:
                self.entry_layout.grab_focus()

            dialog.destroy()


    def on_tv_select_layout_changed(self, selection):
        ls_layout, layout = selection.get_selected()
        if layout is not None:
            print('select :', ls_layout[layout][0])
            self.tv_selected_layout = ls_layout[layout][0]


    def on_tb_load_ly_clicked(self, widget):
        layout = self.get_selected_savedLayout()

        # Xfce4 panel
        cmd = '''xfce4-panel --quit; pkill xfconfd; rm ~/.config/xfce4/panel/*; \
        cp -Rf ''' + savedLayoutDir + layout + '''/xfce4/panel ~/.config/xfce4/; \
        cp -f ''' + savedLayoutDir + layout + '''/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml ~/.config/xfce4/xfconf/xfce-perchannel-xml; \
        cp -f ''' + savedLayoutDir + layout + '''/gtk.css ~/.config/gtk-3.0/gtk.css; \
        sleep 1; xfce4-panel &'''
        subprocess.check_call(cmd, shell=True)


        # plank
        if os.path.isfile(savedLayoutDir + layout + "/plank/plank.ini"):
            
            cmd2 = '''cp -Rf ''' + savedLayoutDir + layout + '''/plank/ ~/.config/plank/ ;  
            cat ''' + savedLayoutDir + layout + '''/plank/plank.ini | dconf load /net/launchpad/plank/docks/
            '''
            subprocess.check_call(cmd2, shell=True)
            
            self.plank.set_active(True)
        else: 
            self.plank.set_active(False)

        # Dockbarx
        args0 = "pkill -f dockbarx-plug "
        subprocess.Popen(args0, shell=True)

        cmd3 = '''gconftool-2 --load ''' + savedLayoutDir + layout + '''/dockbarx/dockbarx.xml '''
        subprocess.run(cmd3, shell=True)

        config.set('Style', 'layout', layout)
        config.write(open(gtconf, 'w'))

        # Xfdashboard
        if os.path.isfile(savedLayoutDir + layout + "/xfdashboard.xml"):
            src = savedLayoutDir + layout + "/xfdashboard.xml"
            dst = home + "/.config/xfce4/xfconf/xfce-perchannel-xml/"
            shutil.copy(src, dst)

            self.xfdashboard.set_active(True)
        else:
            self.xfdashboard.set_active(False)


    def on_tb_rm_ly_clicked(self, widget):
        tmodel, treeiter, values = self.get_selected_layout()
        layout = values[0]

        dialog = Gtk.MessageDialog(
            None,
            0,
            Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL,
            "The selected Layout will be removed",
        )
        dialog.format_secondary_text(
            "This is OK ?"
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            dst = home + "/.config/geox-tweak-xfce/panel/saved_layout/" + layout
            shutil.rmtree(dst)
            tmodel.remove(treeiter)

        elif response == Gtk.ResponseType.CANCEL:
            pass
    
        dialog.destroy()


    def get_selected_layout(self):
        tmodel, treeiter = self.tv_layouts.get_selection().get_selected()
        values = tmodel[treeiter][:]
        return (tmodel, treeiter, values)


    def get_selected_savedLayout(self):
        values = self.get_selected_layout()[2]
        layout = values[0]
        return layout


    def add_new_layout(self, new_layout):

        # Xfce-panel
        dst = home + "/.config/geox-tweak-xfce/panel/saved_layout/" +new_layout + "/xfce4/panel"
        src = home + "/.config/xfce4/panel/"
        shutil.copytree(src, dst)

        dst = home + "/.config/geox-tweak-xfce/panel/saved_layout/" +new_layout + "/xfce4/xfconf/xfce-perchannel-xml/"
        src = home + "/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml"
        os.makedirs(dst)
        shutil.copy(src, dst)

        src = home + "/.config/gtk-3.0/gtk.css"
        dst = savedLayoutDir + new_layout
        shutil.copy(src, dst)

        # Plank
        if not os.system("pidof plank >/dev/null 2>&1"):
            src = home + "/.config/plank/"
            dst = home + "/.config/geox-tweak-xfce/panel/saved_layout/" + new_layout + "/plank/"
            shutil.copytree(src, dst)

            cmdPlank = '''dconf dump /net/launchpad/plank/docks/ > ''' + savedLayoutDir + new_layout + '''/plank/plank.ini'''
            subprocess.run(cmdPlank, shell=True)
    
        # Xfdashboard
        if not os.system("pidof xfdashboard >/dev/null 2>&1"):
            
            src = home + "/.config/xfce4/xfconf/xfce-perchannel-xml//xfdashboard.xml"
            dst = savedLayoutDir + new_layout
            shutil.copy(src, dst)

        # Dockbarx
        src = home + "/.gconf/apps/dockbarx/"
        dst = home + "/.config/geox-tweak-xfce/panel/saved_layout/" + new_layout + "/dockbarx/"
        shutil.copytree(src, dst)

        cmd3 = '''gconftool-2 --dump /apps/dockbarx >  ''' + savedLayoutDir + new_layout + '''/dockbarx/dockbarx.xml'''
        subprocess.run(cmd3, shell=True)


        self.tmodel.append([new_layout])

    def on_tv_layouts_cursor_changed(self, widget):
        pass

    # @ Layout

    def on_btn_ly_geox_clicked(self, widget):
            self.gtweak.plank_config(dirLy='geox')
            self.gtweak.dockbarx_config(
                launcher="[]", theme="Unite Faenza", the_me="Unite_Faenza")
            self.gtweak.change_layout(layout="geox")
            self.gtweak.pulseaudio_config(size="0.6")
            self.xfdashboard.set_active(True)
            self.plank.set_active(True)

    def on_btn_ly_mx_clicked(self, widget):
            self.gtweak.pulseaudio_config(size="0.6")
            self.gtweak.plank_config(dirLy='mxlinux')
            self.gtweak.change_layout(layout="mxlinux")
            self.plank.set_active(False)
            self.xfdashboard.set_active(False)

    def on_btn_ly_win95_clicked(self, widget):
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.change_layout(layout="win95")
            self.gtweak.plank_config(dirLy='win95')
            self.plank.set_active(False)
            self.xfdashboard.set_active(False)

    def on_btn_ly_win7_clicked(self, widget):
            self.gtweak.dockbarx_config(
                launcher="[thunar;/usr/share/applications/thunar.desktop,Web Browser;/usr/share/applications/exo-web-browser.desktop,libreoffice-writer;/usr/share/applications/libreoffice-writer.desktop,exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop]",
                theme="Gaia",
                the_me="Gaia"
            )
            self.gtweak.pulseaudio_config(size="0.6")
            self.gtweak.change_layout(layout="win7")
            self.gtweak.plank_config(dirLy='win7')
            self.xfdashboard.set_active(False)
            self.plank.set_active(False)

    def on_btn_ly_ubuntu_clicked(self, widget):
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.dockbarx_config(
                launcher="[thunar;/usr/share/applications/thunar.desktop,Web Browser;/usr/share/applications/exo-web-browser.desktop,Mail Reader;/usr/share/applications/exo-mail-reader.desktop,libreoffice-writer;/usr/share/applications/libreoffice-writer.desktop,exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop,Test;/usr/share/applications/TestFalse]",
                theme="Unite Faenza",
                the_me="Unite_Faenza")
            self.gtweak.change_layout(layout="ubuntu", )
            self.gtweak.plank_config(dirLy='ubuntu')
            self.plank.set_active(False)
            self.xfdashboard.set_active(True)

    def on_btn_ly_mate_clicked(self, widget):
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.change_layout(layout="mate")
            self.gtweak.plank_config(dirLy='mate')
            self.xfdashboard.set_active(False)
            self.plank.set_active(False)

    def on_btn_ly_xubuntu_clicked(self, widget):
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.change_layout(layout="xubuntu")
            self.gtweak.plank_config(dirLy='xubuntu')
            self.plank.set_active(True)
            self.xfdashboard.set_active(False)

    def on_btn_ly_budgie_clicked(self, widget):
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.dockbarx_config(
                launcher="[thunar;/usr/share/applications/thunar.desktop,firefox;/usr/share/applications/firefox.desktop,libreoffice-writer;/usr/share/applications/libreoffice-writer.desktop,exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop]",
                theme="Deep",
                the_me="Deep")
            self.gtweak.change_layout(layout="budgie")
            self.gtweak.plank_config(dirLy='budgie')
            self.plank.set_active(False)
            self.xfdashboard.set_active(False)

    # @ Onglet : "Window theme" #################################
    # @ Bouton additonnel pointant vers les outils de parametrage xfce natifs + compact / hdpi

    @staticmethod
    def on_btn_widows_decor_clicked(widget):
        subprocess.run("xfwm4-settings")

    @staticmethod
    def on_btn_all_theme_clicked(widget):
        subprocess.run("xfce4-appearance-settings")

    def on_toggle_adapta_compact_toggled(self, widget):
        theme = self.theme_name.get_label()

        if widget.get_active():
            self.gtweak.theme_var(var_adapta='-Eta')
            if '-Eta' not in theme:
                theme = theme + '-Eta'
                self.theme_name.set_label(theme)
        else:
            self.gtweak.theme_var(var_adapta="")
            theme = theme.replace('-Eta', '')
            self.theme_name.set_label(theme)

    def on_toggle_arc_hdpi_toggled(self, widget):
        theme = self.theme_name.get_label()

        if widget.get_active():
            self.gtweak.theme_var(var_arc='-hdpi')
            if '-hdpi' not in theme:
                theme = theme + '-hdpi'
                self.theme_name.set_label(theme)
        else:
            self.gtweak.theme_var(var_arc="")
            theme = theme.replace('-hdpi', '')
            self.theme_name.set_label(theme)

    def on_toggle_arc_xhdpi_toggled(self, widget):
        theme = self.theme_name.get_label()

        if widget.get_active():
            self.gtweak.theme_var(var_arc='-xhdpi')
            if '-xhdpi' not in theme:
                theme = theme + '-xhpdi'
                self.theme_name.set_label(theme)
        else:
            self.gtweak.theme_var(var_arc="")
            theme = theme.replace('-xhdpi', '')
            self.theme_name.set_label(theme)

    # @ Check theme / bar_theme  install / rmv

    def theme_status(self):
        check_theme = self.theme_name.get_label()
        # FIXIT : Adapta deeppurple miss !
        if os.path.exists('/usr/share/themes/' + check_theme) or os.path.exists(home + '/.themes/' + check_theme):
            self.install_bar_theme.hide()
            self.apply_bar_theme.show()

        else:
            self.apply_bar_theme.hide()
            self.install_bar_theme.show()


    def on_btn_theme_install_clicked(self, widget):
        #FIXIT Path ( pq pas en .local/user ?, sans bash ni mdp...)
       
        theme = self.theme_name.get_label()

        subprocess.check_call("cd ~/.themes ; tar -xf " + sdir + "/theme/themes.tar.xz " + theme, shell=True)        

        if ('dark' in theme or
            'Dark' in theme or
            'Nokto' in theme):

            t = self.gtweak.dark_light(theme)
            themeVar = t[0]
            print(theme + themeVar)
            if 'missing' not in themeVar:
                try:
                    subprocess.check_call("cd ~/.themes ; tar -xf " + sdir + "/theme/themes.tar.xz " + themeVar, shell=True)
                except Exception as e:
                    print(e)
            

        else:
            t = self.gtweak.light_dark(theme)
            themeVar = t[0]
            print(theme + themeVar)

            if 'missing' not in themeVar:
                try:
                    subprocess.check_call("cd ~/.themes ; tar -xf " + sdir + "/theme/themes.tar.xz " + themeVar , shell=True)
                    
                except Exception as e:
                    print(e)
            
        self.install_bar_theme.hide()
        self.apply_bar_theme.show()

    def on_rm_theme_clicked(self, widget):
        theme = self.theme_name.get_label()
        print(theme)
        dialog = Gtk.MessageDialog(
            parent=None,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            text="The " + theme + " theme will be remove",
        )
        dialog.format_secondary_text(
            "(only if in ~/.themes/)"
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            subprocess.Popen(
                "rm -r ~/.themes/" + theme, shell=True)
            self.apply_bar_theme.hide()
            self.install_bar_theme.show()
        elif response == Gtk.ResponseType.CANCEL:
            print("rm canceled")

        dialog.destroy()


    # @ theme # Button : Apply selected theme
    def on_btn_apply_clicked(self, widget):
        if self.chk_folder_color.get_active():
            self.gtweak.change_theme(change_folder=True)
        else:
            self.gtweak.change_theme(change_folder=False)

    # @ theme # PopOver windows decorator
    # def on_btn_wd_clicked(self, widget):
    #     self.popover_wd.show_all()
    #     self.popover_wd.popup()

    # @ Preparation de la Modification des themes en fonction de la  selection (radio btn)
        # What ? Obliger de faire une fonction par objet glade ...?
        # TODO Add plano matcha...

    def on_radio_greybird_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/greybird.png")
            self.gtweak.select_theme(
                theme='Greybird',
                windows_decor='Greybird'
            )
            self.theme_name.set_label('Greybird')
            self.theme_status()
            self.theme_status()

    def on_radio_adapta_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir + "/img/adapta.png")
            self.gtweak.select_theme(
                theme='Adapta',
                windows_decor='Adapta',
                folder_color='cyan'
            )
            self.theme_status()
            self.theme_name.set_label('Adapta')

    def on_radio_adapta_bluegrey_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-bluegrey.png")
            self.gtweak.select_theme(theme='Adapta-BlueGrey', windows_decor='Adapta',
                                     folder_color='bluegrey'
                                     )
            self.theme_status()
            self.theme_name.set_label('Adapta-BlueGrey')

    def on_radio_adapta_bluegrey_nokto_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-bluegrey-nokto.png")
            self.gtweak.select_theme(
                theme='Adapta-BlueGrey-Nokto',
                windows_decor='Adapta',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='bluegrey')
            self.theme_status()
            self.theme_name.set_label('Adapta-BlueGrey-Nokto')

    def on_radio_adapta_pink_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-pink.png")
            self.gtweak.select_theme(theme='Adapta-Pink', windows_decor='Adapta',
                                     folder_color='red'
                                     )
            self.theme_name.set_label('Adapta-Pink')
            self.theme_status()

    def on_radio_adapta_pink_nokto_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-pink-nokto.png")
            self.gtweak.select_theme(
                theme='Adapta-Pink-Nokto',
                windows_decor='Adapta',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='red'
            )
            self.theme_name.set_label('Adapta-Pink-Nokto')
            self.theme_status()

    def on_radio_adapta_deeppurple_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-deeppurple.png")
            self.gtweak.select_theme(theme='Adapta-DeepPurple', windows_decor='Adapta',
                                     folder_color='violet'
                                     )
            self.theme_name.set_label('Adapta-DeepPurple')
            self.theme_status()

    def on_radio_adapta_deeppurple_nokto_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(
                sdir + "/img/adapta-deeppurple-nokto.png")
            self.gtweak.select_theme(
                theme='Adapta-DeepPurple-Nokto',
                windows_decor='Adapta',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='violet'
            )
            self.theme_name.set_label('Adapta-DeepPurple-Nokto')
            self.theme_status()

    def on_radio_adapta_green_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir + "/img/adapta-green.png")
            self.gtweak.select_theme(theme='Adapta-Green', windows_decor='Adapta',
                                     folder_color='green'
                                     )
            self.theme_name.set_label('Adapta-Green')
            self.theme_status()

    def on_radio_adapta_green_nokto_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-green-nokto.png")
            self.gtweak.select_theme(
                theme='Adapta-Green-Nokto',
                windows_decor='Adapta',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='green'
            )
            self.theme_name.set_label('Adapta-Green-Nokto')
            self.theme_status()

    def on_radio_adapta_nokto_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir + "/img/adapta-nokto.png")
            self.gtweak.select_theme(
                theme='Adapta-Nokto',
                windows_decor='Adapta',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='cyan'
            )
            self.theme_name.set_label('Adapta-Nokto')
            self.theme_status()

    def on_radio_matcha_aliz_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-aliz.png")
            self.gtweak.select_theme(
                theme='Matcha-aliz',
                windows_decor='Matcha-aliz',
            )
            self.theme_name.set_label('Matcha-aliz')
            self.theme_status()

    def on_radio_matcha_sea_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-sea.png")
            self.gtweak.select_theme(
                theme='Matcha-sea',
                windows_decor='Matcha-sea',
            )
            self.theme_name.set_label('Matcha-sea')
            self.theme_status()

    def on_radio_matcha_azul_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-azul.png")
            self.gtweak.select_theme(
                theme='Matcha-azul',
                windows_decor='Matcha-azul',
            )
            self.theme_name.set_label('Matcha-azul')
            self.theme_status()

    def on_radio_matcha_dark_sea_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(
                sdir + "/img/matcha-dark-sea.png")
            self.gtweak.select_theme(
                theme='Matcha-dark-sea',
                windows_decor='Matcha-dark-sea',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )
            self.theme_name.set_label('Matcha-dark-sea')
            self.theme_status()

    def on_radio_matcha_dark_aliz_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(
                sdir + "/img/matcha-dark-aliz.png")
            self.gtweak.select_theme(
                theme='Matcha-dark-aliz',
                windows_decor='Matcha-dark-aliz',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )
            self.theme_name.set_label('Matcha-dark-aliz')
            self.theme_status()

    def on_radio_matcha_dark_azul_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(
                sdir + "/img/matcha-dark-azul.png")
            self.gtweak.select_theme(
                theme='Matcha-dark-azul',
                windows_decor='Matcha-dark-azul',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )
            self.theme_name.set_label('Matcha-dark-azul')
            self.theme_status()

    def on_radio_arc_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc.png")
            self.gtweak.select_theme(
                theme='Arc',
                windows_decor='Arc',
            )
            self.theme_name.set_label('Arc')
            self.theme_status()
    
    def on_radio_arc_slate_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-dark-slate.png")
            self.gtweak.select_theme(
                theme='Arc-Dark-SLATE',
                windows_decor='Arc-Dark-SLATE',
            )
            self.theme_name.set_label('Arc-Dark-SLATE')
            self.theme_status()

    def on_radio_arc_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-dark.png")
            self.theme_name.set_label("Arc-Dark")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_clearlooks_toggled(self, widget):
        if widget.get_active():
            self.theme_name.set_label("Clearlooks")
            themename = self.theme_name.get_label()
            self.theme_status()

            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Light',
                plank_theme='geox-light'
            )

    def on_radio_qogir_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir.png")
            self.theme_name.set_label("Qogir")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_qogir_light_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-light.png")
            self.theme_name.set_label("Qogir-light")
            themename = self.theme_name.get_label()
            self.theme_status()

            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_qogir_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-dark.png")
            self.theme_name.set_label("Qogir-dark")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_qogir_manjaro_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-manjaro.png")
            self.theme_name.set_label("Qogir-manjaro-win")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='teal'
            )

    def on_radio_qogir_manjaro_light_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-manjaro-light.png")
            self.theme_name.set_label("Qogir-manjaro-win-light")
            themename = self.theme_name.get_label()
            self.theme_status()

            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='teal'
            )

    def on_radio_qogir_manjaro_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-manjaro-dark.png")
            self.theme_name.set_label("Qogir-manjaro-win-dark")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='teal'

            )

    def on_radio_qogir_ubuntu_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-ubuntu.png")
            self.theme_name.set_label("Qogir-ubuntu-win")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='orange'
            )

    def on_radio_qogir_ubuntu_light_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-ubuntu-light.png")
            self.theme_name.set_label("Qogir-ubuntu-win-light")
            themename = self.theme_name.get_label()
            self.theme_status()

            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='orange'
            )

    def on_radio_qogir_ubuntu_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-ubuntu-dark.png")
            self.theme_name.set_label("Qogir-ubuntu-win-dark")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='orange'
            )

    def on_radio_materia_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/materia.png")
            self.theme_name.set_label("Materia")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                plank_theme='geox-light'

            )

    def on_radio_materia_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/materia-dark.png")
            self.theme_name.set_label("Materia-dark")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_materia_light_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/materia-light.png")
            self.theme_name.set_label("Materia-light")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus',
                plank_theme='geox-light'
            )

    def on_radio_macos_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/macos.png")
            self.theme_name.set_label("McOS-MJV-XFCE-Edition-2.3")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Light',
                plank_theme="geox-light"

            )

    # !Pas d'affichage
    def on_radio_prodark_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/pro-dark-xfce.png")
            self.theme_name.set_label("PRO-dark-XFCE-4.14")
            self.theme_status()
            self.gtweak.select_theme(
                theme='PRO-dark-XFCE-4.14',
                windows_decor='PRO-dark-XFCE-4.14',
                folder_color='bluegrey'
            )

    def on_radio_macos_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/macos-dark.png")
            self.theme_name.set_label("McOS-MJV-Dark-XFCE-Edition-2.3")
            self.theme_status()
            self.gtweak.select_theme(
                theme='McOS-MJV-Dark-XFCE-Edition-2.3',
                windows_decor='McOS-MJV-Dark-XFCE-Edition-2.3',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_adwaita_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/adwaita.png")
            self.theme_name.set_label("Adwaita")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_adwaita_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/adwaita-dark.png")
            self.theme_name.set_label("Adwaita-dark")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_numix_toggled(self, widget):
        #Fixit : hide icon in btn (peaufinage des fenetre?>> si dark, ceux des menu invisible, et inversement)
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/numix.png")
            self.theme_name.set_label("Numix")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='orange',
                icons_name='Papirus-Dark'

            )

    def on_radio_mint_toggled(self, widget):
        if widget.get_active():
            self.theme_name.set_label("Mint-Y")
            self.preview_mint.set_from_file(sdir + "/img/mint-y.png")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='green'
            )

    def on_radio_mint_grey_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-grey.png")
            self.theme_name.set_label("Mint-Y-Grey")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='grey'
            )

    def on_radio_mint_red_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-red.png")
            self.theme_name.set_label("Mint-Y-Red")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='red'
            )

    def on_radio_mint_purple_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-purple.png")
            self.theme_name.set_label("Mint-Y-Purple")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='violet'
            )

    def on_radio_mint_aqua_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-aqua.png")
            self.theme_name.set_label("Mint-Y-Aqua")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='blue'
            )

    def on_radio_mint_brown_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-brown.png")
            self.theme_name.set_label("Mint-Y-Brown")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='brown'
            )

    def on_radio_mint_teal_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-teal.png")
            self.theme_name.set_label("Mint-Y-Teal")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='teal'
            )

    def on_radio_mint_darker_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-darker.png")
            self.theme_name.set_label("Mint-Y-Darker")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor='Mint-Y-Dark',
                folder_color='green'
            )

    def on_radio_mint_darker_grey_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-darker-grey.png")
            self.theme_name.set_label("Mint-Y-Darker-Grey")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor="Mint-Y-Dark-Grey",
                folder_color='grey'
            )

    def on_radio_mint_darker_red_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-darker-red.png")
            self.theme_name.set_label("Mint-Y-Darker-Red")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor="Mint-Y-Dark-Red",
                folder_color='red'
            )

    def on_radio_mint_darker_purple_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-darker-purple.png")
            self.theme_name.set_label("Mint-Y-Darker-Purple")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor="Mint-Y-Dark-Purple",
                folder_color='violet'
            )

    def on_radio_mint_darker_aqua_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-darker-aqua.png")
            self.theme_name.set_label("Mint-Y-Darker-Aqua")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor="Mint-Y-Dark-Aqua",
                folder_color='blue'
            )

    def on_radio_mint_darker_brown_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-darker-brown.png")
            self.theme_name.set_label("Mint-Y-Darker-Brown")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor="Mint-Y-Dark-Brown",
                folder_color='brown'
            )

    def on_radio_mint_darker_teal_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-darker-teal.png")
            self.theme_name.set_label("Mint-Y-Darker-Teal")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor="Mint-Y-Dark-Teal",
                folder_color='teal'
            )

    def on_radio_mint_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-dark.png")
            self.theme_name.set_label("Mint-Y-Dark")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='green'
            )

    def on_radio_mint_dark_grey_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-dark-grey.png")
            self.theme_name.set_label("Mint-Y-Dark-Grey")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='grey'
            )

    def on_radio_mint_dark_red_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-dark-red.png")
            self.theme_name.set_label("Mint-Y-Dark-Red")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='red'
            )

    def on_radio_mint_dark_purple_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-dark-purple.png")
            self.theme_name.set_label("Mint-Y-Dark-Purple")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='violet'
            )

    def on_radio_mint_dark_aqua_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-dark-aqua.png")
            self.theme_name.set_label("Mint-Y-Dark-Aqua")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='blue'
            )

    def on_radio_mint_dark_brown_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(
                sdir + "/img/mint-y-dark-brown.png")
            self.theme_name.set_label("Mint-Y-Dark-Brown")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='brown'
            )

    def on_radio_mint_dark_teal_toggled(self, widget):
        if widget.get_active():
            self.preview_mint.set_from_file(sdir + "/img/mint-y-dark-teal.png")
            self.theme_name.set_label("Mint-Y-Dark-Teal")
            self.theme_status()
            themename = self.theme_name.get_label()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='teal'
            )

    def on_radio_prof_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/prof.png")
            self.theme_name.set_label("Prof--XFCE-2.1")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                )

    def on_radio_nordic_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/nordic.png")
            self.theme_name.set_label("Nordic")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark'
                )
    def on_radio_nordic_polar_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/nordic-polar.png")
            self.theme_name.set_label("Nordic-Polar")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                )


    def on_radio_Cloudy_SoftBlue_Light_toggled(self, widget):
        if widget.get_active():
            self.preview_various.set_from_file(sdir + "/img/cloudy-softblue-light.png")
            self.theme_name.set_label("Cloudy-SoftBlue-Light")
            themename = self.theme_name.get_label()
            self.theme_status()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                )

    
                
    # @ pane : ICON color _________________________________________

    def on_folder_toggled(self, widget):
        if widget.get_active():
            folder_color = Gtk.Buildable.get_name(widget)
            self.gtweak.on_folderc(folder_color)


    # @ pane : "OTHER" _____________________________

    # @ Buttons  of "Other" pane 

    @staticmethod
    def on_btn_simpleclic_thunar_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c thunar -p /misc-single-click -s "true" ''', shell=True)
        else:
            subprocess.Popen(
                '''xfconf-query -c thunar -p /misc-single-click -s "false" ''', shell=True)

    @staticmethod
    def on_btn_folder_file_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c thunar -p /misc-folders-first -s "true" ''', shell=True)
        else:
            subprocess.Popen(
                '''xfconf-query -c thunar -p /misc-folders-first -s "false" ''', shell=True)

    @staticmethod
    def on_btn_txt_next_icons_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c thunar -p /misc-text-beside-icons -s "true" ''', shell=True
            )
        else:
            subprocess.Popen(
                '''xfconf-query -c thunar -p /misc-text-beside-icons -s "false" ''', shell=True
            )

    @staticmethod
    def on_btn_simpleclic_desktop_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/single-click -s "true" ''', shell=True
            )
        else:
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/single-click -s "false" ''', shell=True
            )

    @staticmethod
    def on_btn_trash_desktop_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-trash -s "true" ''', shell=True
            )
        else:
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-trash -s "false" ''', shell=True
            )

    @staticmethod
    def on_btn_home_desktop_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-home -s "true" ''', shell=True
            )
        else:
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-home -s "false" ''', shell=True
            )

    @staticmethod
    def on_btn_removable_desktop_toggled(widget):
        if widget.get_active():
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-removable -s "true" ''', shell=True
            )
        else:
            subprocess.Popen(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-removable -s "false" ''', shell=True
            )

    @staticmethod
    def on_btn_xfwm4_tweaks_settings_clicked(widget):
        subprocess.Popen("xfwm4_tweaks_settings", shell=True)

    @staticmethod
    def on_btn_thunar_settings_clicked(widget):
        subprocess.Popen("thunar-settings", shell=True)

    @staticmethod
    def on_btn_xfce_settings_clicked(widget):
        subprocess.Popen("xfce4-settings-manager", shell=True)

    @staticmethod
    def on_btn_lightdm_settings_clicked(widget):
        subprocess.Popen("lightdm-gtk-greeter-settings-pkexec", shell=True)

    @staticmethod
    def on_btn_desktop_settings_clicked(widget):
        subprocess.Popen("xfdesktop-settings", shell=True)

    @staticmethod
    def on_btn_panel_settings_clicked(widget):
        subprocess.Popen("xfce4-panel --preferences", shell=True)

    @staticmethod
    def on_btn_notification_settings_clicked(widget):
        subprocess.Popen("xfce4-notifyd-config", shell=True)

    # @ Parametrage xfce ; volet "Other"

    def state_settings(self):
        """ Verifie les parametrage de xfce dans xfconf pour
        que les check_button refletent bien la configuration actuelle """
        if subprocess.getoutput(
                '''xfconf-query -c thunar -p /misc-single-click''') == "true":
            self.btn_simpleclic_thunar.handler_block_by_func(
                self.on_btn_simpleclic_thunar_toggled)
            self.btn_simpleclic_thunar.set_active(True)
            self.btn_simpleclic_thunar.handler_unblock_by_func(
                self.on_btn_simpleclic_thunar_toggled)

        if subprocess.getoutput(
                '''xfconf-query -c thunar -p /misc-folders-first''') == "true":
            self.btn_folder_file.handler_block_by_func(
                self.on_btn_folder_file_toggled)
            self.btn_folder_file.set_active(True)
            self.btn_folder_file.handler_unblock_by_func(
                self.on_btn_folder_file_toggled)

        if subprocess.getoutput(
                '''xfconf-query -c thunar -p /misc-text-beside-icons'''
        ) == "true":
            self.btn_txt_next_icons.handler_block_by_func(
                self.on_btn_txt_next_icons_toggled)
            self.btn_txt_next_icons.set_active(True)
            self.btn_txt_next_icons.handler_unblock_by_func(
                self.on_btn_txt_next_icons_toggled)

        if subprocess.getoutput(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/single-click'''
        ) == "true":
            self.btn_simpleclic_desktop.handler_block_by_func(
                self.on_btn_simpleclic_desktop_toggled)
            self.btn_simpleclic_desktop.set_active(True)
            self.btn_simpleclic_desktop.handler_unblock_by_func(
                self.on_btn_simpleclic_desktop_toggled)

        if subprocess.getoutput(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-trash'''
        ) == "true":
            self.btn_trash_desktop.handler_block_by_func(
                self.on_btn_trash_desktop_toggled)
            self.btn_trash_desktop.set_active(True)
            self.btn_trash_desktop.handler_unblock_by_func(
                self.on_btn_trash_desktop_toggled)

        if subprocess.getoutput(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-home'''
        ) == "true":
            self.btn_home_desktop.handler_block_by_func(
                self.on_btn_home_desktop_toggled)
            self.btn_home_desktop.set_active(True)
            self.btn_home_desktop.handler_unblock_by_func(
                self.on_btn_home_desktop_toggled)

        if subprocess.getoutput(
                '''xfconf-query -c xfce4-desktop -p /desktop-icons/file-icons/show-removable'''
        ) == "true":
            self.btn_removable_desktop.handler_block_by_func(
                self.on_btn_removable_desktop_toggled)
            self.btn_removable_desktop.set_active(True)
            self.btn_removable_desktop.handler_unblock_by_func(
                self.on_btn_removable_desktop_toggled)

####

if __name__ == "__main__":
    main = Geox()
    Gtk.main()
