#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/littleBobbyTables/")
sys.path.insert(0,"/var/www/littleBobbyTables/littleBobbyTables/")

import logging
logging.basicConfig(stream=sys.stderr)

from littleBobbyTables import app as application
