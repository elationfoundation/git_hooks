#!/bin/bash
# THIS FILE IS AUTO GENERATED!

while getopts f: flag
do
    case "$flag" in
	(f) files="OPTARG";;
    (*) usage;;
    esac
done
shift $(expr $OPTIND - 1)

echo $files


if [ -x temp.sh ]
    then
      ./temp.sh $files
    else
      echo 'Test does not exist'
fi

exit 0
