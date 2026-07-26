import logging
import os
from datetime import datetime

# 1. Generate the unique filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Build the final file path (Join: current directory -> 'logs' folder -> filename)
LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. Create only the parent directory ('logs') if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

# 4. Set up the logger configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started.")
    print("Log file generated successfully!")
