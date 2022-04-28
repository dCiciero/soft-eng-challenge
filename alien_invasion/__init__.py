from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import os

print(f"Here's our value: {os.getenv('SHIP_CREW')}")