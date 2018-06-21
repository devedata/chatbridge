#!/bin/bash

# must stop rocketchat-server
sudo service snap.rocketchat-server.rocketchat-server stop
# do new backup
sudo snap run rocketchat-server.backupdb
# copy backup to backups folder
sudo cp /var/snap/rocketchat-server/current/backup.tgz /root/rocketchat_backups/backup_$(date "+%Y.%m.%d-%H.%M.%S").tgz
# start rocketchat-server
sudo service snap.rocketchat-server.rocketchat-server start


