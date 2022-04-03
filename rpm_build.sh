#!/bin/bash
set -e

if [[ $# -eq 0 ]] ; then
    echo 'You must provide a package basename'
    exit 0
fi

SPEC=${1}
NAME=$(basename $SPEC | cut -d '.' -f 1)
cd /host
PATCHES=$(ls specs/${NAME}*.patch 2>/dev/null || echo "")
rpmdev-setuptree
for patch in $PATCHES
do
    cp -v $patch /root/rpmbuild/SOURCES/
done
dnf builddep -y ${SPEC}
spectool -g -R ${SPEC}
rpmbuild -ba ${SPEC}
[ -d "/root/rpmbuild/RPMS/x86_64" ] && cp /root/rpmbuild/RPMS/x86_64/${NAME}*.rpm RPM/
[ -d "/root/rpmbuild/RPMS/noarch" ] && cp /root/rpmbuild/RPMS/noarch/${NAME}*.rpm RPM/

chown -v --reference ${SPEC} RPM/${NAME}*.rpm
