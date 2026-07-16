import schedule
import time
from pathlib import Path
from classifier.app import classifyImage

def job():
    print(f"{time.localtime()} Running classifier on latest image")
    classifyImage(Path("/workspace/img/snapshots/latest.jpg"))

schedule.every.minute.do(job)

if __name__ == "__main__":
    schedule.run_pending()
    time.sleep(1)