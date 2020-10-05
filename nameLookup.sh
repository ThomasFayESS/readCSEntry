listIPs=$1

for i in `cat $listIPs`; do
	a=$(nslookup $i | grep name | sed 's/.*name = //')
	echo "$i - $a"
done
