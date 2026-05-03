import sys
import os

# Add the current directory to sys.path so we can import main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from mangum import Mangum
from main import app

handler = Mangum(app)
