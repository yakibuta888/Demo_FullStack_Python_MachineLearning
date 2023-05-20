#!/bin/bash
USERNAME=${USER_NAME}
USERID=${USER_ID}
GROUPID=${GROUP_ID}
echo "Create User = $USERID. Group = $GROUPID"
groupadd -g $GROUPID $USERNAME
useradd -m -s /bin/bash -u $USERID -g $GROUPID $USERNAME
exec /usr/sbin/gosu $USERNAME "$@"
