#!/usr/bin/env bash

### Variables

HOSTNAME=pi@nalacam.local

# Change these directories
SOURCE_DIR=../
REMOTE_DIR=/home/pi/remote-dog-treat-dispenser

### Constants

GREEN=`tput setaf 2`
YELLOW=`tput setaf 3`
CYAN=`tput setaf 6`
RESET=`tput sgr0`

show_help() {
  echo "Sync repository to remote pi every 5s. Script must be run from the containing directory."
  echo "Use --once flag to only run rsync once."
}

usage="$(basename "$0") [-h] [-o] Sync repository to remote pi. Script must be run from the containing directory.

Arguments:
    -o, --once   Only run rsync once"

run_rsync() {
    echo "${GREEN}$(date)${RESET}"
    rsync -avz $SOURCE_DIR $HOSTNAME:$REMOTE_DIR \
        --exclude "env/" \
        --exclude ".git/" \
        --exclude "*__pycache__*" \
        --exclude "*.pyc" \
        --exclude "*.egg-info/"
    echo ""
}

while :; do
    case $1 in
        -h|-\?|--help)
            echo "$usage"
            exit
            ;;
        -o|--once) flag_once="SET"
        ;;
        *) break
    esac
    shift
done

if [ "$flag_once" ]; then
  run_rsync

else
  while true; do
    run_rsync
    sleep 2
  done
fi
