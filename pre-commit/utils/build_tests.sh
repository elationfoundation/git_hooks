#!/bin/bash

# It is assumed that the makefile is in the root folder of the repo.
directory=".git/hooks/"
test_runner="run_tests.sh"
script_path=
while getopts t:d:v:s: flag
do
    case "$flag" in
	(t) test_runner="$OPTARG";;
	(d) directory="$OPTARG";;
    (v) vflag=1;;
    (s) script_path="$OPTARG";;
    (*) usage;;
    esac
done
shift $(expr $OPTIND - 1)

echo $directory
echo $test_runner
echo $script_path

if [ ! -x $directory/$test_runner ]
	then
	cat >> $directory/$test_runner << EOL
#!/bin/bash
# THIS FILE IS AUTO GENERATED!

while getopts f: flag
do
    case "\$flag" in
	(f) files="OPTARG";;
    (*) usage;;
    esac
done
shift \$(expr \$OPTIND - 1)

echo \$files

exit 0
EOL
	  sudo chmod a+x $directory/$test_runner
fi

#get test files name without extension
script="${script_path##*/}"

mv $script_path $directory/$script
sudo chmod a+x $directory/$script

#delete the exit line
sed -i '$ d' $directory/$test_runner

cat >> $directory/$test_runner << EOL

if [ -x $script ]
    then
      ./$script \$files
    else
      echo 'Test does not exist'
fi

exit 0
EOL

