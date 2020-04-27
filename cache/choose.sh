#!/bin/zsh

# Zsh Theme Chooser by fox (fox91 at anche dot no)
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/txt/copying/ for more details.

THEMES_DIR="$ZSH/themes"
FAVLIST="${HOME}/.zsh_favlist"
source $ZSH/oh-my-zsh.sh

function noyes() {
    read "a?$1 (y/n) "
    if [[ $a == "N" || $a == "n" || $a = "" ]]; then
        return 0
    fi
    return 1
}

function theme_preview() {
    THEME=$1
    THEME_NAME=`echo $THEME | sed s/\.zsh-theme$//`
    print "\x1b[36;1m[+]\x1b[00m THEME NAME\x1b[91;1m => \x1b[00m$THEME_NAME $reset_color"
    echo
    source "$THEMES_DIR/$THEME"
    print -P "$PROMPT"
    echo
}

function banner() {
    echo
}

function usage() {
    echo "Usage: $0 [options] [theme]"
    echo
    echo "Options"
    echo "  -l   List available themes"
    echo "  -s   Show all themes"
    echo "  -h   Get this help message"
    exit 1
}

function list_themes() {
    for THEME in $(ls $THEMES_DIR); do
        THEME_NAME=`echo $THEME | sed s/\.zsh-theme$//`
        echo $THEME_NAME
    done
}

function insert_favlist() {
    if grep -q "$THEME_NAME" $FAVLIST 2> /dev/null ; then
        echo "Already in favlist"
    else
        echo $THEME_NAME >> $FAVLIST
        echo "Saved to favlist"
    fi

}

function theme_chooser() {
    for THEME in $(ls $THEMES_DIR); do
        echo
        theme_preview $THEME
        if [[ -z $1 ]]; then
                  echo "Click enter for continue, or CTRL + C for quit."
		  noyes "Do you like this theme ?" ||\
		  insert_favlist $THEME_NAME
            echo
        fi
    done
}

while getopts ":lhs" Option
do
  case $Option in
    l ) list_themes ;;
    s ) theme_chooser 0 ;;
    h ) usage ;;
    * ) usage ;; # Default.
  esac
done

if [[ -z $Option ]]; then
    if [[ -z $1 ]]; then
        theme_chooser
    else
        theme_preview $1".zsh-theme"
    fi
fi
