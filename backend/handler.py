import runpod
import os

def handler(job):
    """
    RunPod Serverless handler
    """

    job_input = job.get("input", {})

    source_image = job_input.get("source_image")
    target_image = job_input.get("target_image")

    if not source_image:
        return {
            "status": "error",
            "message": "Missing source_image"
        }

    if not target_image:
        return {
            "status": "error",
            "message": "Missing target_image"
        }

    # FaceFusion processing will be added here later.

    return {
        "status": "success",
        "message": "Images received successfully.",
        "source_image": source_image,
        "target_image": target_image
    }
