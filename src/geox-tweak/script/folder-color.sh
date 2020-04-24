#!/bin/bash

NewFolderColor=$1
Theme=$(xfconf-query -c xsettings -p /Net/IconThemeName)
Icons=$(grep icons $HOME/.config/geox-tweak-xfce/geox-tweak.conf | cut -d"=" -f2 )
 
xfce4-terminal -e "sudo papirus-folders -t $Theme -C $NewFolderColor "


