# orchestrator/pipeline_controller.py

import requests
import time

JENKINS_URL = "http://localhost:8081"
JOB_NAME = "microservice-pipeline"
TOKEN = "your_token"

class PipelineController:

    def __init__(self):
        self.session = requests.Session()

    def trigger_pipeline(self):
        print("🚀 Triggering Jenkins pipeline...")

        url = f"{JENKINS_URL}/job/{JOB_NAME}/build?token={TOKEN}"
        response = self.session.post(url)

        if response.status_code == 201:
            print("✅ Pipeline started successfully")
        else:
            print("❌ Failed to start pipeline")

    def monitor_pipeline(self):
        print("📊 Monitoring pipeline status...")

        for i in range(5):
            print(f"Checking status... attempt {i+1}")
            time.sleep(5)

        print("ℹ️ Pipeline monitoring completed")


if __name__ == "__main__":
    orchestrator = PipelineController()
    orchestrator.trigger_pipeline()
    orchestrator.monitor_pipeline()