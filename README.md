##################
Author : QaldeK - aldek@vivaldi.net
Version : 0.3 (beta)
License : GPL
Depends: python3, synapse, xfdashboard, plank, xfce4-notes, conky-all, xfce4-dockbarx-plugin, papirus-icon-theme,'python3' 'python3-gi' 'xfce4-datetime-plugin' 'xfce4-battery-plugin' 'gconf2' 'gir1.2-gtk-3.0' 'gtk2-engines-murrine' 'gtk2-engines-pixbuf
Git : https://github.com/QaldeK/geox-tweak
#################


# Description: 

Geox-Tweak-Xfce is a tool for customize Xfce appearance. It is an alternative to the configuration tools of xfce desktops, which are scattered, and require several manipulations to obtain a consistent theme.
Geox-Tweak is easy to use, and allows to change the gtk themes, the window decoration and the icons theme (including libreoffice buttons color) in a coherent way and in one click. No more dark icons on a dark theme, which make them invisible. 

Several themes are included, among which: Arc, Mint-Y, Adapta, Qogir, Matcha, McOS-MJV, Pro-dark-xfce ...

It also makes it easy to change the organization of xfce panels, making it possible to make your desktop look like Windows 10, 95, or gnome2, xubuntu, unity, mxlinux... Until now, only Zorin OS lite offered a tool allowing this, without spending too much time setting everything manually.

It also makes it possible and easy to change the color of the folder icons, thanks to the use of the "papirus-folder" script.

GeoX-TweaK installs with a set of software to improve the appearance of Xfce:
  - [Plank](https://github.com/ricotz/plank) is an application launch bar similar to that of MacOS 
- [Dockbarx](https://github.com/twa022/xfce4-dockbarx-plugin) is another launch bar, which integrates with the Xfce panel, and which works a bit like that of Windows
- [Xfdashboard](https://docs.xfce.org/apps/xfdashboard/start) offers Xfce the possibility of operating as Gnome, by displaying an overview of all the windows open when you go to the top left corner of the screen. It also allows you to search for applications.
- [Synapse](https://launchpad.net/synapse-project) is a software that allows you to quickly launch software or documents using the keyboard.

It is by installing and configuring these tools that GeoX-TweaK-Xfce allows you to transform your xfce desktop to make it look like what you want. 

GTX also install papirus-icon-theme if it's not, and work with it. This beautiful and complete icon theme is used by GTX to make the color of icons and themes consistent, including libreoffice.

Finally, GTX comes with gtx-indicators: a small software that fits in the notification bar and that allows you to quickly switch from a light theme to a dark theme, and vice versa.

# Installation

GTX has been tested on the following Linux distributions: Linux Mint Xfce 19.03, Xubuntu 18.04; MX Linux 19.01. It should install and properly install third-party software on which it depends simply by typing in a terminal:


 	wget -O- https://raw.githubusercontent.com/QaldeK/geox-tweak-xfce/master/dl_and_install.sh# | sh


Uninstall :
 
	wget -O- https://raw.githubusercontent.com/QaldeK/geox-tweak-xfce/master/uninstall# | bash



An another way is to download manually the archive on this git, unzip, and 1) launch "install_geox", or 2) open a terminal where the archive had unzip, and tape "./install-script"


This potentially works for all Debian-based distributions. If nevertheless certain third-party software cannot be installed by the installation script, Geox-Tweak-Xfce will indicate the software missing, and you can try to install it manually to take advantage of all the layouts.

For manjaro, it seems difficult to install xfce4-dockbarx-plugin. Consequently, some layouts (Win10; Ubuntu; Budgie ...) do not work.




# Screenshots

![Alt text](geox-tweak/img/screenshots5.png?raw=true "Desktop Layout")

![Alt text](geox-tweak/img/screenshots6.png?raw=true "Windows theme")

![Alt text](geox-tweak/img/screenshots7.png?raw=true "Folders icons")

![Alt text](geox-tweak/img/screenshots8.png?raw=true "Other")

![Alt text](geox-tweak/img/screenshots-gtxi.png?raw=true "Indicator")


