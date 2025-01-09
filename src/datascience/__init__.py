import logging
import os
import sys

log_dir="log"
log_file="logging.log"
log_path=os.path.join(log_dir,log_file)

formater="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=formater,

    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("Dats Science")








