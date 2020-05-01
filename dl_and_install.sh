#!/bin/sh

gh_repo="geox-tweak-xfce"
temp_dir="$(mktemp -d)"

echo "___Getting the latest version from GitHub___"
wget -O "/tmp/$gh_repo.tar.gz" https://github.com/QaldeK/geox-tweak-xfce/archive/master.tar.gz
echo "___Unpacking archive___"
tar -xzf "/tmp/$gh_repo.tar.gz" -C "$temp_dir"

echo "___Launch install-script___"
cd $temp_dir
cd geox-tweak-xfce-master
./install-script

# echo "___Clearing cache___"
# rm -rf "/tmp/$temp_dir
