#!/usr/bin/env bash

#clear messages
logrotate -f /etc/logrotate.d/rsyslog
logrotate -f /etc/logrotate.conf

#clear nohup
> /nohup.out
