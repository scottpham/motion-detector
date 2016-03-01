#!/usr/bin/env bash

#clear messages
sudo logrotate -f /etc/logrotate.d/rsyslog
sudo logrotate -f /etc/logrotate.conf
