#!/user/bin/bash

##########################################
# Autho:         zhaowenlong             #
# Create_Date:   2022-01-02 04:25:38     #
# Version:       v1.0                    #
# Mail:          zwl1087@163.com         #
##########################################


read -p "please input a username: " username

id $username &> /dev/null
if  [ $? -ne 0 ];then
	echo " no such user : $username"

fi

read -p "Are you sure remove this user ? [y/n] " action

case $action in
	y|Y|yes|Yes)
		userdel -r $username
		echo "$username is deleted. "
		;;
	*)
		echo " make sure input error "
esac
