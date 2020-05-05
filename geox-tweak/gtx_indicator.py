#!/usr/bin/python3

from gi.repository import AppIndicator3 as appindicator
from gi.repository import Gtk
import gi
import subprocess
from geox_tweak_xfce import GeoxTweak 
import configparser  # traiter les fichiers de configuration
import os
from os.path import expanduser
from gi.repository import GLib


gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

home = expanduser("~")  # path home de l'user
sdir = os.path.dirname(os.path.abspath(__file__))  # path du script py
paneldir = home + '/.config/geox-tweak-xfce/panel/'
config = configparser.ConfigParser()
gtconf = home + '/.config/geox-tweak-xfce/geox-tweak.conf'

gtweak = GeoxTweak()

config.read(gtconf)


class Gtx_indicator:

    def __init__(self):

        self.indicator = appindicator.Indicator.new(
            'Geox-Tweak-Indicator', 'ao-app-tray',
            appindicator.IndicatorCategory.APPLICATION_STATUS
            )
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.menu())


    def menu(self):

        menu = Gtk.Menu()

        GLib.timeout_add(10000, self.state_darkmode)

        self.item_dark_mode = Gtk.CheckMenuItem.new_with_label(
            'Dark Theme')

        self.item_dark_mode.connect(
            'toggled', self.toggle_dark_mode_cb)

        menu.append(self.item_dark_mode)
      
        # Add Conky option submenu 
        conky_menu_item = Gtk.MenuItem.new_with_label(
            "Show on desktop (Conky)")
        conky_menu = Gtk.Menu()
        conky_item_date = Gtk.CheckMenuItem.new_with_label('Date & Time')
        conky_item_info = Gtk.CheckMenuItem.new_with_label('Info')
        conky_item_shortcut = Gtk.CheckMenuItem.new_with_label('Keyboard Shortcuts')
        conky_item_shortcut.connect('activate', self.conky_cb_shortcut)
        conky_menu.append(conky_item_date)
        conky_menu.append(conky_item_info)
        # conky_menu.append(conky_item_shortcut)
        conky_menu_item.set_submenu(conky_menu)

        #set activ CheckMenuItem if conky is activ
        ckactiv = subprocess.getoutput('''pgrep -xa conky | cut -d' ' -f4-''')
        print(ckactiv)
        if "info" in ckactiv:
            conky_item_info.set_active(True)

        if "time-date" in ckactiv:
            conky_item_date.set_active(True)

        #connect AFTER set activ
        conky_item_date.connect('activate', self.conky_cb_date)
        conky_item_info.connect('activate', self.conky_cb_info)
        
        menu.append(conky_menu_item)


        # Add Geox-tweak-xfce launcher item
        geox_item = Gtk.MenuItem.new_with_label('GeoX Tweak Xfce')
        geox_item.connect('activate', self.geox_cb)
        menu.append(geox_item)

        # Add quit action
        quit_item = Gtk.MenuItem.new_with_label("Quit")
        quit_item.connect('activate', Gtk.main_quit)
        menu.append(quit_item)

        menu.show_all()
        return menu


    def toggle_day_night_cb(widget, data=None):
        """Callback when a request to item day/night automatic mode was made """
        pass


    def state_darkmode(self):
        config.read(gtconf)
        if config.get('Style', 'dark_theme') == 'yes':
            self.item_dark_mode.set_active(True)
        else:
            self.item_dark_mode.set_active(False)

        return True

    def toggle_dark_mode_cb(self, widget, data=None):
        """Callback when a request to item dark mode was made """
        config.read(gtconf)

        if widget.get_active():
            if config.get('Style', 'dark_theme') == 'no':
                gtweak.dark_mode()
        else:
            gtweak.light_mode()


    def layout_cb(widget, layout):
        """Callback that handles activation of theme setting change"""
        print(layout)
        # geox = Geox()

        if layout == 'Geox':
            gtweak.plank_config(
                pinned="true",
                offset="100",
                position="bottom",
                theme=gtweak.plank_theme  # theme doit etre precisé sinon argument manquant 
            )
            # gtweak.plank.set_active(True)
            gtweak.pulseaudio_config(size="0.6")
            gtweak.dockbarx_config(
                launcher="[]", theme="Unite Faenza", the_me="Unite_Faenza")
            gtweak.change_layout(layout="geox")
            # gtweak.xfdashboard.set_active(True)

        elif layout == ' Ubuntu':
            gtweak.on_radio_ubuntu_toggled(widget)


    def geox_cb (self, widget):
        arg = "geox-tweak"
        subprocess.Popen(arg, shell=True)

             
    def conky_cb_date(self, widget):
        conky = '''geox-time-date-white" &'''
        print(conky)
        if widget.get_active():
            gtweak.conky_add(conky)
        else:
            print(conky + 'else')
            gtweak.conky_remove(conky)

            
    def conky_cb_info(self, widget):
        conky = '''geox-info-white" &'''
        print(conky)
        if widget.get_active():
            gtweak.conky_add(conky)
        else:
            print(conky)
            gtweak.conky_remove(conky)

           
    def conky_cb_shortcut(self, widget):
        conky = '''geox-time-date-white" &'''
        print(conky)
        if widget.get_active():
            gtweak.conky_add(conky)
        else:
            print(conky)
            gtweak.conky_remove(conky)

       
###########
if __name__ == "__main__":
    main = Gtx_indicator()
    Gtk.main()
