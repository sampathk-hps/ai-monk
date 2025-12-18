# ai-monk

1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

2. Initialize each project with uv
cd /your_project_folder
uv init --no-readme

Instead of pip install -r requirements.txt, use:

uv sync - Install dependencies

uv add package-name - Add new package

uv remove package-name - Remove package

uv run python script.py - Run with uv environment

uv run python -m folder_name.file_name - Run with uv environment as a module
