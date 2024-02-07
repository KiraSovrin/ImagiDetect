# run.py
import subprocess

subprocess.run(["venv\\Scripts\\activate", "&&", "python",
                "imagidetect\\main.py"], shell=True)
