import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from server.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
