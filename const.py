from datetime import datetime

# info
DEVELOPMENT = True
__version__ = 0.1
PROJECT_NAME='OPED-Getter'

# File Name
now=datetime.now().strftime('%Y%m%d_%H%M%S')
LOG_FILE_NAME="./log/"+now+".log"
DB_FILE="db.json"
