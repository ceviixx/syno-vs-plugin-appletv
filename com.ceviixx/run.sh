#!/bin/sh

BASEDIR=$(dirname $0)
ARGV=""

escape()
{
	local ARG=$(echo $@ | sed "s/'/'\\\\''/g")
	echo \'$ARG\'
}

i=1
while [ $i -le $# ]; do
	eval ARG=\$\(escape \${$i}\)
	ARGV="$ARGV $ARG"
	i=`expr $i + 1`
done

#echo $ARGV;

#eval "/usr/bin/env python3 "\
#	"$BASEDIR/search.py $ARGV"

#eval "/usr/bin/env php "\
#	"$BASEDIR/search.php $ARGV"



eval "/usr/bin/env python3 "\
	"$BASEDIR/search.py $ARGV"