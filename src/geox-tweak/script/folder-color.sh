#!/bin/bash

NewFolderColor=$1
Theme=$(xfconf-query -c xsettings -p /Net/IconThemeName)
Icons=$(grep icons $PWD/activ.conf | cut -d"=" -f2 )

gksu "papirus-folders -t $Theme -C $NewFolderColor" ;
	sed -i "s/^folder =.*/folder = $NewFolderColor/" $PWD/activ.conf

exit


