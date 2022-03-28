#!/usr/bin/bash
##########################################
# Autho:         zhaowenlong             #
# Create_Date:   2022-01-02 05:54:23     #
# Version:       v1.0                    #
# Mail:          zwl1087@163.com         #
##########################################

function menu(){

        cat <<-EOF
        +--------------------------------------------------+
        +           h. help                                +
        +           f. disk parttion                       +
        +           d. filesystem mount                    +
        +           m. memery                              +
        +           u. system load                         +
        +           q. quit                                +
        +--------------------------------------------------+
        # shellcheck disable=SC1040
        EOF
}

menu

while [ true ]; do

  echo -en "\e[1;32m please choose your options\e[0m "
  read options

  case $options in
          h)
                  clear
                  echo -e "\e[1;45mShow MENU As This: \e[0m"
                  menu
                  ;;
          f)
                  echo -e "\e[1;45m get filesystem partition: \e[0m START"
                  fdisk -l
                  echo -e "\e[1;45m filesystem partition: \e[0m END"
                  ;;
          d)
                  echo -e "\e[1;45m get disk info: \e[0m END"
                  df -Th
                  echo -e "\e[1;45m get disk info: \e[0m END"
                  ;;
          m)
                  echo " get memory mow "
                  free -m
                  ;;
          u)
                  echo " analysis system load now "
                  uptime
                  ;;
          q)
                  echo " i will exit"
                  ;;
          *)
                  echo -e  "\e[1;31m ERROR: no such options: $options ; please Check you options, Bye\e[0m "
                  exit
  esac
done