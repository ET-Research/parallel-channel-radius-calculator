# Sample .bashrc for SuSE Linux
# Copyright (c) SuSE GmbH Nuernberg

# There are 3 different types of shells in bash: the login shell, normal shell
# and interactive shell. Login shells read ~/.profile and interactive shells
# read ~/.bashrc; in our setup, /etc/profile sources ~/.bashrc - thus all
# settings made here will also take effect in a login shell.
#
# NOTE: It is recommended to make language settings in ~/.profile rather than
# here, since multilingual X sessions would not work properly if LANG is over-
# ridden in every subshell.

# Some applications read the EDITOR variable to determine your favourite text
# editor. So uncomment the line below and enter the editor of your choice :-)
#export EDITOR=/usr/bin/vim
#export EDITOR=/usr/bin/mcedit
# export PATH=$HOME/coot/bin:$PATH
# For some news readers it makes sense to specify the NEWSSERVER variable here
#export NEWSSERVER=your.news.server

# If you want to use a Palm device with Linux, uncomment the two lines below.
# For some (older) Palm Pilots, you might need to set a lower baud rate
# e.g. 57600 or 38400; lowest is 9600 (very slow!)
#
#export PILOTPORT=/dev/pilot
#export PILOTRATE=115200


## Want to switch to Python3
##---------------------------------------------------
## bash -l
## cd /Scr/scr-test-steven/install/loopy/bin/
## source activate py3k # in order to activate python 3
## source deactivate  # if you want to deactivate python 3
##---------------------------------------------------


#================================================================================
# ALIAS
#================================================================================
source /home/steven/.alias.sh
source /home/steven/steven.sh

export http_proxy="http://130.126.120.41:3128"
