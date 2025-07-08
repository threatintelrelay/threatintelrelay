#!/bin/bash
# dev-domains.sh
# Usage: sudo ./dev-domains.sh add|remove

set -e

DOMAINS="api.localdev.me airflow.localdev.me auth.localdev.me"
HOSTS_LINE="127.0.0.1  $DOMAINS"
HOSTS_FILE="/etc/hosts"

function add_domains() {
  if grep -q "$DOMAINS" $HOSTS_FILE; then
    echo "Domains already present in $HOSTS_FILE"
  else
    echo "$HOSTS_LINE" | sudo tee -a $HOSTS_FILE
    echo "Added: $DOMAINS"
  fi
}

function remove_domains() {
  sudo sed -i.bak "/$DOMAINS/d" $HOSTS_FILE
  echo "Removed: $DOMAINS"
}

case "$1" in
  add)
    add_domains
    ;;
  remove)
    remove_domains
    ;;
  *)
    echo "Usage: sudo $0 add|remove"
    exit 1
    ;;
esac
