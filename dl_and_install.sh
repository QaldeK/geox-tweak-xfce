#!/bin/sh

gh_repo="geox-tweak-xfce"
temp_dir="$(mktemp -d)"


echo "=> Getting the latest version from GitHub ..."
wget -O "/tmp/$gh_repo.tar.gz" \
https://github.com/QaldeK/geox-tweak-xfce/archive/master.tar.gz

echo "=> Unpacking archive ..."
tar -xzf "/tmp/$gh_repo.tar.gz" -C "$temp_dir"

echo "=> Launch install-script"
cd $temp_dir
cd geox-tweak-xfce-master
./install-script

# echo "=> Clearing cache ..."
# rm -rf "/tmp/$temp_dir