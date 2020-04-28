#!/usr/bin/env python3

from geox_tweak_xfce import GeoxTweak
import subprocess  # os et subprocess : executer des commandes et script bash
from os.path import expanduser
import os.path
from os import path
import os
import configparser  # traiter les fichiers de configuration
import gi  # nécessaire pour utiliser le fichier glade
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # nécessaire pour utiliser le fichier glade/ GObject?

home = expanduser("~")  # path home de l'user
sdir = os.path.dirname(os.path.abspath(__file__))  # path du script py
paneldir = home + '/.config/geox-tweak-xfce/panel/'
config = configparser.ConfigParser()
gtconf = home + '/.config/geox-tweak-xfce/geox-tweak.conf'


class Geox:
    def on_main_window_destroy(self, data=None):
        Gtk.main_quit()

# @ INIT
    def __init__(self):
        """ Initialisation : chargement du gtk builder 
        lisant le fichier glade ..."""

        self.builder = Gtk.Builder()
        glade_file = os.path.join(sdir, "geox_0.2.glade")
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        go = self.builder.get_object
        self.gtweak = GeoxTweak()

        # bouton pref
        self.btn_plank_pref = go("btn_plank_pref")
        self.btn_xfdashboard_pref = go("btn_xfdashboard_pref")
        self.btn_conky_pref = go("btn_conky_pref")
        self.btn_notes_pref = go("btn_notes_pref")
        self.btn_ddterm_pref = go("btn_ddterm_pref")

        # Toogle Tools
        self.plank = go("plank")
        self.xfdashboard = go("xfdashboard")
        self.synapse = go("synapse")
        self.conky = go("conky")
        self.ddterm = go("ddterm")
        self.notes = go("notes")
        self.gtxi = go("gtxi")

        # Toggle Help TODO A traduire avant d'activer ?
        self.btn_plank_help = go("btn_plank_help")
        self.btn_xfdashboard_help = go("btn_xfdashboard_help")
        self.btn_synapse_help = go("btn_synapse_help")
        self.btn_conky_help = go("btn_conky_help")
        self.btn_notes_help = go("btn_notes_help")

        self.help_txt_zone = go("help_txt_zone")
        self.defaut_help()

        self.warning_app_miss = go("warning_app_miss")
        self.warning_app_miss.hide()


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
        self.preview_arc = go("preview_arc")
        self.preview_arc.set_from_file(sdir + "/img/arc.png")
        self.preview_adwaita = go("preview_adwaita")
        self.preview_adwaita.set_from_file(sdir + "/img/adwaita.png")
        self.preview_qogir = go("preview_qogir")
        self.preview_qogir.set_from_file(sdir + "/img/qogir.png")
        self.preview_macos = go("preview_macos")
        self.preview_macos.set_from_file(sdir + "/img/macos.png")
        self.preview_materia = go("preview_materia")
        self.preview_materia.set_from_file(sdir + "/img/materia.png")
        self.preview_greybird = go("preview_greybird")
        self.preview_greybird.set_from_file(sdir + "/img/greybird.png")
        self.preview_numix = go("preview_numix")
        self.preview_numix.set_from_file(sdir + "/img/numix.png")
        self.preview_clearlooks = go("preview_clearlooks")
        self.preview_clearlooks.set_from_file(sdir + "/img/clearlooks.png")
        self.preview_prodark = go("preview_prodark")
        self.preview_prodark.set_from_file(sdir + "/img/pro-dark-xfce.png")
        self.preview_matcha = go("preview_matcha")
        self.preview_matcha.set_from_file(sdir + "/img/matcha-sea.png")

        self.bar_theme = go("bar_theme")
        self.bar_theme.hide()

        # Icon color
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

        # Configuration xfce actuelle
        self.state_settings()
        # Application tierce installé > .conf
        self.status_plank = ""
        self.status_synapse = ""
        self.status_xfdashboard = ""
        self.status_conky = ""
        self.status_dockbarx = ""

        # /!\ Positionner apres la declaration des btn rapportées aux états
        # testés ;
        self.state_app(self)
        self.state_gtxi()

        # ID des label du fichier de configuration geox-tweak.conf (> modifié par "config.")
        self.var_theme = ""
        self.theme = ""
        self.windows_decor = ""
        self.icons = ""
        self.layout = ""
        self.libreoffice_icons = ""
        # TODO : Renommer (confusion) assigné glade...
        self.theme_name = go("theme_name")

        self.chk_folder_color = go("chk_folder_color")


        # @ affichage de la fenetre
        self.window = go("main_window")
        self.window.show()
        
        self.firstrun_warning()     # Verifie si FirstRun et dépendances



        config.read(gtconf)
        plank_theme = config.get("Style", "plank_theme")
        self.plank_theme = plank_theme

    @staticmethod
    def on_btn_quit_clicked(widget):
        Gtk.main_quit()

    def defaut_help(self):
        defaut = ""
        self.help_txt_zone.get_buffer().set_text(defaut)


    def firstrun_warning(self):
        """ Verifie si c'est le premier lancement de geox-tweak-xfce
        Si oui, lance  le script firstrun.
        Et verifie l'installation des logiciels tiers (synapse, xfdashboard, plank, dockbarx)
        et des dépendances (python..., gconftool, etc. """

        # TODO : verif logiciel par logiciel ; griser les layout impossible et proposer installation
        # if config.get('AppInstall', 'synapse') != "ok"
        #     arg3 ="bash " "

        # Verifier le fichier de configuration
        args = '''if [ ! -e $HOME/.config/geox-tweak-xfce/geox-tweak.conf ]
        then mkdir $HOME/.config/geox-tweak-xfce/ ;
        cp -f /usr/share/geox-tweak/geox-tweak.conf $HOME/.config/geox-tweak-xfce/geox-tweak.conf ;
        fi '''
        subprocess.run(args, shell=True)

        config.read(gtconf)     # Lire la configuration tel que loggué
        
        if config.get('AppInstall', 'FirstRun') != "no":

            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.WARNING,
                                       Gtk.ButtonsType.OK_CANCEL, "Some packages are required by geox-tweak-xfce, procced to installation ?")
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                self.firstrun()

            dialog.destroy()

            # dialog.connect("destroy", Gtk.main_quit)
            # dialog.show_all()

    def firstrun(self):

        arg = '''sed -i 's/firstrun.*/firstrun = no/' $HOME/.config/geox-tweak-xfce/geox-tweak.conf'''
        subprocess.Popen(arg, shell=True)

        script = sdir + '/script/firstrun.sh'
        subprocess.run("xfce4-terminal -e " + script, shell=True)


    def status_app_dep(self):

        app_miss = []

        if subprocess.check_output('''dpkg-query -W -f='${Status}' plank 2>/dev/null | grep -c "ok installed"''', shell=True) == 1:
            self.status_plank = 'miss'
            app_miss += [' plank ']
        else:
            self.status_plank = 'ok'

        # if subprocess.check_output('''dpkg-query -W -f='${Status}' synapse 2>/dev/null | grep -c "ok installed"''', shell=True) == 1:
        #     self.status_synapse = 'miss'
        #     app_miss += [' synapse ']

        # else:
        #     self.status_synapse = 'ok'

        # if subprocess.check_output('''dpkg-query -W -f='${Status}' xfdashboard 2>/dev/null | grep -c "ok installed"''', shell=True) == 1:
        #     self.status_xfdashboard = 'miss'
        #     app_miss += ['xfdashboard']

        # else:
        #     self.status_xfdashboard = 'ok'

        # if subprocess.check_output('''dpkg-query -W -f='${Status}' conky-all 2>/dev/null | grep -c "ok installed"''', shell=True) == 1:
        #     self.status_conky = 'miss'
        #     app_miss += ['conky-all']

        # else:
        #     self.status_conky = 'ok'

        if subprocess.check_output('''dpkg-query -W -f='${Status}' xfce4-dockbarx-plugin 2>/dev/null | grep -c "ok installed"''', shell=True) == 1:
            self.status_dockbarx = 'miss'
            app_miss += [' xfce4-dockbarx-plugin ']

        else:
            self.status_dockbarx = 'ok'

        print("Some needed sofware are not installed: ")
        print(app_miss)
        
        #Si liste non-vide
        if (app_miss): 
            warning_txt = ('Some software necessary for the use of themes are not installed : ' 
                + str(app_miss) + '\nPlease click on "install it" or try to install them manually ')
                            

            self.txt_app_miss.set_label(warning_txt)
            self.warning_app_miss.show()


    def on_btn_install_miss_clicked(self):
        self.firstrun()


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

# @ TOOLS : Bouton Toggle des App tieres
    # TODO > dependances : app & conkytoggle.sh;)


    def on_gtxi_toggled(self, widget):
        if widget.get_active():
            subprocess.Popen('python3 /usr/share/geox-tweak/gtx_indicator.py', shell=True)
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
         le script conkytoggle.sh, et xfdashboard lancer en mode démo """

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
        """ Adapter le label en fonction de l'etat des logiciels"""

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

# @ theme installé et non installé 
    #TODO

    def installed_themes(self):
        """ check if themes are installed or not (geox-tweak.conf verification OR real check before change ??)  """

        themes = ('qogir', 'qogir-dark', 'materia', 'numix', 'arc',
                  'arc_red', 'arc_cherry', 'macos', 'macos_dark',
                  'prodark', 'adwaita', 'adwaita-dark', 'adapta'
                  'adapta_bluegrey', 'adapta_pink', 'adapta_deeppurple'
                  'adapta_green')
        for theme in themes:
            if config.get('ThemeInstall', theme) == 'no':
                pass  # TODO

# @ Panel layout  
    # TODO  autre configuration : theme xfdashboard ? &

    def on_radio_geox_toggled(self, widget):
        if widget.get_active():
            self.gtweak.plank_config(
                pinned="true",
                offset="100",
                position="bottom",
                theme=self.plank_theme  # theme doit etre precisé sinon argument manquant
            )
            self.gtweak.dockbarx_config(
                launcher="[]", theme="Unite Faenza", the_me="Unite_Faenza")
            self.gtweak.pulseaudio_config(size="0.6")
            self.gtweak.change_layout(layout="geox")
            self.xfdashboard.set_active(True)
            self.plank.set_active(True)

    def on_radio_mx_toggled(self, widget):
        if widget.get_active():
            self.gtweak.pulseaudio_config(size="0.6")
            self.gtweak.plank_config(
                "true", "100", "bottom", theme=self.plank_theme)
            self.gtweak.change_layout(layout="mxlinux")
            self.plank.set_active(False)
            self.xfdashboard.set_active(False)

    def on_radio_win95_toggled(self, widget):
        if widget.get_active():
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.change_layout(layout="win95")
            self.gtweak.plank_config(
                "true", "0", "top", theme=self.plank_theme)
            self.plank.set_active(False)
            self.xfdashboard.set_active(False)

    def on_radio_win7_toggled(self, widget):
        if widget.get_active():
            self.gtweak.dockbarx_config(
                launcher="[thunar;/usr/share/applications/Thunar.desktop,firefox;/usr/share/applications/firefox.desktop,libreoffice-writer;/usr/share/applications/libreoffice-writer.desktop,exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop]",
                theme="Gaia",
                the_me="Gaia"
            )
            self.gtweak.pulseaudio_config(size="0.6")
            self.gtweak.change_layout(layout="win7")
            self.gtweak.plank_config(
                "true", "0", "right", theme=self.plank_theme)
            self.xfdashboard.set_active(False)
            self.plank.set_active(False)

    def on_radio_ubuntu_toggled(self, widget):
        if widget.get_active():
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.dockbarx_config(
                launcher="[thunar;/usr/share/applications/Thunar.desktop,firefox;/usr/share/applications/firefox.desktop,libreoffice-writer;/usr/share/applications/libreoffice-writer.desktop,exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop]",
                theme="Unite Faenza",
                the_me="Unite_Faenza")
            self.gtweak.change_layout(layout="ubuntu", )
            self.gtweak.plank_config(
                "true", "100", "bottom", theme=self.plank_theme)
            self.plank.set_active(False)
            self.xfdashboard.set_active(True)

    def on_radio_mate_toggled(self, widget):
        if widget.get_active():
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.change_layout(layout="mate")
            self.gtweak.plank_config(
                "true", "0", "left", theme=self.plank_theme)
            self.xfdashboard.set_active(False)
            self.plank.set_active(False)

    def on_radio_xubuntu_toggled(self, widget):
        if widget.get_active():
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.change_layout(layout="xubuntu")
            self.gtweak.plank_config(
                "true", "0", "bottom", theme=self.plank_theme)
            self.plank.set_active(True)
            self.xfdashboard.set_active(False)

    def on_radio_budgie_toggled(self, widget):
        if widget.get_active():
            self.gtweak.pulseaudio_config(size="1")
            self.gtweak.dockbarx_config(
                launcher="[thunar;/usr/share/applications/Thunar.desktop,firefox;/usr/share/applications/firefox.desktop,libreoffice-writer;/usr/share/applications/libreoffice-writer.desktop,exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop]",
                theme="Deep",
                the_me="Deep")
            self.gtweak.change_layout(layout="budgie")
            self.gtweak.plank_config(
                "true", "100", "left", theme=self.plank_theme)
            self.plank.set_active(False)
            self.xfdashboard.set_active(False)

# @ Onglet : "Window theme" 
    # @ Bouton additonnel pointant vers les outils de parametrage xfce natifs
    @staticmethod
    def on_btn_widows_decor_clicked(widget):
        os.system("xfwm4-settings")

    @staticmethod
    def on_btn_all_theme_clicked(widget):
        os.system("xfce4-appearance-settings")

    def on_toggle_adapta_compact_toggled(self, widget):
        if widget.get_active():
            self.gtweak.theme_var(var_adapta='-Eta')
        else:
            self.gtweak.theme_var(var_adapta="")

    def on_toggle_arc_hdpi_toggled(self, widget):
        if widget.get_active():
            self.gtweak.theme_var(var_arc='-hdpi')
        else:
            self.gtweak.theme_var(var_arc="")

    def on_toggle_arc_xhdpi_toggled(self, widget):
        if widget.get_active():
            self.gtweak.theme_var(var_arc='-xhdpi')
        else:
            self.gtweak.theme_var(var_arc="")


    # @ theme # Button : Apply selected theme 
    def on_btn_apply_clicked(self, widget):
        if self.chk_folder_color.get_active():
            self.gtweak.change_theme(change_folder=True)
        else:
            self.gtweak.change_theme(change_folder=False)

    # # @ theme # PopOver windows decorator
    # def on_btn_wd_clicked(self, widget):
    #     self.popover_wd.show_all()
    #     self.popover_wd.popup()


    # @ Preparation de la Modification des themes en fonction de la selection (radio btn)
        # What ? Obliger de faire une fonction par objet glade ...?
        # TODO Add plano matcha...

    def on_radio_greybird_toggled(self, widget):
        if widget.get_active():
            self.gtweak.select_theme(
                theme='Greybird',
                windows_decor='Greybird'
            )
            self.bar_theme.show()
            self.theme_name.set_label('Greybird')

    def on_radio_adapta_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir + "/img/adapta.png")
            self.gtweak.select_theme(
                theme='Adapta',
                windows_decor='Adapta',
                folder_color='cyan'
            )
            self.bar_theme.show()
            self.theme_name.set_label('Adapta')

    def on_radio_adapta_bluegrey_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-bluegrey.png")
            self.gtweak.select_theme(theme='Adapta-BlueGrey', windows_decor='Adapta',
                                     folder_color='bluegrey'
                                     )
            self.bar_theme.show()
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
            self.bar_theme.show()
            self.theme_name.set_label('Adapta-BlueGrey-Nokto')

    def on_radio_adapta_pink_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-pink.png")
            self.gtweak.select_theme(theme='Adapta-Pink', windows_decor='Adapta',
                                     folder_color='red'
                                     )
            self.theme_name.set_label('Adapta-Pink')
            self.bar_theme.show()

    def on_radio_adapta_pink_nokto_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-pink-notko.png")
            self.gtweak.select_theme(
                theme='Adapta-Pink-Nokto',
                windows_decor='Adapta',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
                folder_color='red'
            )
            self.theme_name.set_label('Adapta-Pink-Nokto')
            self.bar_theme.show()

    def on_radio_adapta_deeppurple_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-deeppurple.png")
            self.gtweak.select_theme(theme='Adapta-DeepPurple', windows_decor='Adapta',
                                     folder_color='violet'
                                     )
            self.theme_name.set_label('Adapta-DeepPurple')
            self.bar_theme.show()

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
            self.bar_theme.show()

    def on_radio_adapta_green_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir + "/img/adapta-green.png")
            self.gtweak.select_theme(theme='Adapta-Green', windows_decor='Adapta',
                                     folder_color='green'
                                     )
            self.theme_name.set_label('Adapta-Green')
            self.bar_theme.show()

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
            self.bar_theme.show()

    # TODO ...MAIS pas ajouter comme choix pour le moment!!
    def on_radio_adapta_brown_toggled(self, widget):
        if widget.get_active():
            self.preview_adapta.set_from_file(sdir + "/img/adapta-brown.png")
            self.folder = "brown"
            self.windows_decor = "Adapta"
            self.icons = "Papirus"
            self.libreoffice_icons = "papirus"
            self.bar_theme.show()
            self.theme_name.set_label("Adapta-Brown")
            self.plank_theme = "geox-dark"
            self.theme = "Adapta-Brown"

    def on_radio_adapta_brown_nokto_toggled(self, widget):
        if widget.get_active():
            self.folder = "brown"
            self.windows_decor = "Adapta"
            self.preview_adapta.set_from_file(sdir +
                                              "/img/adapta-brown-nokto.png")
            self.icons = "papirus_dark"
            self.libreoffice_icons = "papirus_dark"
            self.bar_theme.show()
            self.theme_name.set_label("Adapta-Brown-Nokto")
            self.plank_theme = "geox-dark"
            self.theme = "Adapta-Brown-Nokto"

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
            self.bar_theme.show()


    def on_radio_matcha_aliz_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-aliz.png")
            self.gtweak.select_theme(
                theme='Matcha-aliz',
                windows_decor='Matcha-aliz',
            )
            self.theme_name.set_label('Matcha Aliz')
            self.bar_theme.show()

    def on_radio_matcha_sea_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-sea.png")
            self.gtweak.select_theme(
                theme='Matcha-sea',
                windows_decor='Matcha-sea',
            )
            self.theme_name.set_label('Matcha Sea')
            self.bar_theme.show()


    def on_radio_matcha_azul_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-azul.png")
            self.gtweak.select_theme(
                theme='Matcha-azul',
                windows_decor='Matcha-azul',
            )
            self.theme_name.set_label('Matcha Azul')
            self.bar_theme.show()


    def on_radio_matcha_dark_sea_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-dark-sea.png")
            self.gtweak.select_theme(
                theme='Matcha-dark-sea',
                windows_decor='Matcha-dark-sea',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )
            self.theme_name.set_label('Matcha Dark Sea')
            self.bar_theme.show()

    def on_radio_matcha_dark_aliz_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-dark-aliz.png")
            self.gtweak.select_theme(
                theme='Matcha-dark-aliz',
                windows_decor='Matcha-dark-aliz',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )
            self.theme_name.set_label('Matcha Dark Aliz')
            self.bar_theme.show()

    def on_radio_matcha_dark_azul_toggled(self, widget):
        if widget.get_active():
            self.preview_matcha.set_from_file(sdir + "/img/matcha-dark-azul.png")
            self.gtweak.select_theme(
                theme='Matcha-dark-azul',
                windows_decor='Matcha-dark-azul',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )
            self.theme_name.set_label('Matcha Dark Azul')
            self.bar_theme.show()

    def on_radio_arc_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc.png")
            self.gtweak.select_theme(
                theme='Arc',
                windows_decor='Arc',
            )
            self.theme_name.set_label('Arc')
            self.bar_theme.show()

    def on_radio_arc_red_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-red.png")
            self.theme_name.set_label("Arc-Red")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_arc_cherry_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-cherry.png")
            self.theme_name.set_label("Arc-Cherry")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_arc_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-dark.png")
            self.theme_name.set_label("Arc-Dark")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_arc_dark_red_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-red-dark.png")
            self.theme_name.set_label("Arc-Red-Dark")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )


    def on_radio_arc_dark_cherry_toggled(self, widget):
        if widget.get_active():
            self.preview_arc.set_from_file(sdir + "/img/arc-cherry-dark.png")
            self.theme_name.set_label("Arc-Cherry-Dark")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )


    def on_radio_clearlooks_toggled(self, widget):
        if widget.get_active():
            self.theme_name.set_label("Clearlooks")
            themename = self.theme_name.get_label()
            self.bar_theme.show()

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
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_qogir_light_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-light.png")
            self.theme_name.set_label("Qogir-light")
            themename = self.theme_name.get_label()
            self.bar_theme.show()

            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_qogir_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_qogir.set_from_file(sdir + "/img/qogir-dark.png")
            self.theme_name.set_label("Qogir-dark")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_materia_toggled(self, widget):
        if widget.get_active():
            self.preview_materia.set_from_file(sdir + "/img/materia.png")
            self.theme_name.set_label("Materia")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                plank_theme='geox-light'

            )

    def on_radio_materia_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_materia.set_from_file(sdir + "/img/materia-dark.png")
            self.theme_name.set_label("Materia-dark")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_materia_light_toggled(self, widget):
        if widget.get_active():
            self.preview_materia.set_from_file(sdir + "/img/materia-light.png")
            self.theme_name.set_label("Materia-light")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus',
                plank_theme='geox-light'
            )

    def on_radio_macos_toggled(self, widget):
        if widget.get_active():
            self.preview_macos.set_from_file(sdir + "/img/macos.png")
            self.theme_name.set_label("McOS-MJV-XFCE-Edition")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Light'
            )

    # !Pas d'affichage
    def on_radio_prodark_toggled(self, widget):
        if widget.get_active():
            self.theme_name.set_label("PRO-dark-XFCE")
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme='PRO-dark-XFCE-4.14',
                windows_decor='PRO-dark-XFCE-4.14',
                folder_color='bluegrey'
            )

    def on_radio_macos_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_macos.set_from_file(sdir + "/img/macos-dark.png")
            self.theme_name.set_label("MacOS Dark")
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme='McOS-MJV-Dark-XFCE-Edition-2.3',
                windows_decor='McOS-MJV-Dark-XFCE-Edition-2.3',
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_adwaita_toggled(self, widget):
        if widget.get_active():
            self.preview_adwaita.set_from_file(sdir + "/img/adwaita.png")
            self.theme_name.set_label("Adwaita")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
            )

    def on_radio_adwaita_dark_toggled(self, widget):
        if widget.get_active():
            self.preview_adwaita.set_from_file(sdir + "/img/adwaita-dark.png")
            self.theme_name.set_label("Adwaita-dark")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                icons_name='Papirus-Dark',
                libreoffice_icons='papirus-dark',
            )

    def on_radio_numix_toggled(self, widget):
        if widget.get_active():
            self.theme_name.set_label("Numix")
            themename = self.theme_name.get_label()
            self.bar_theme.show()
            self.gtweak.select_theme(
                theme=themename,
                windows_decor=themename,
                folder_color='orange'
            )
    # ICON color

    def on_folder_toggled(self, widget):
        if widget.get_active():
            folder_color = Gtk.Buildable.get_name(widget)
            self.gtweak.on_folderc(folder_color)

# @ pane : "OTHER" 

    # Buttons  of "Other" pane #####################

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


####

if __name__ == "__main__":
    main = Geox()
    Gtk.main()
