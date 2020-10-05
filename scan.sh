#!/usr/bin/bash

outFile=/tmp/"$$"-listIPs
[[ -f $outFile ]] && rm -r $outFile

listIPs=()

isOnline()
{
	ping -c 1 $1 >/dev/null
	[ $? -eq 0 ] && echo "$1" >> $outFile
}

subnet=$1

for i in $subnet.{1..254}
do
	isOnline "$i" & disown
done

[[ ! -f $outFile ]] && echo "No ping responses on subnet $subnet" && exit
cat $outFile | sort
[[ -f $outFile ]] && rm -r $outFile
