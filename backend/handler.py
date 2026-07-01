import subprocess
import requests
import base64

print("HANDLER.PY LOADED")


def download_image(url, save_path):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(response.content)

    return save_path


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def face_swap(source_path, target_path, output_path):
    command = [
        "python",
        "/app/facefusion/facefusion.py",
        "headless-run",
        "--source-paths", source_path,
        "--target-path", target_path,
        "--output-path", output_path,
        "--processors", "face_swapper"
    ]

    print("===================================")
    print("RUNNING FACEFUSION")
    print(command)
    print("===================================")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=600
    )

    print("========== EXIT CODE ==========")
    print(result.returncode)

    print("========== STDOUT ==========")
    print(result.stdout)

    print("========== STDERR ==========")
    print(result.stderr)

    if result.returncode != 0:
        raise Exception(
            f"Exit Code: {result.returncode}\n\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}"
        )

    return output_path


def handler(event):
    print("===================================")
    print("HANDLER FUNCTION CALLED")
    print(event)
    print("===================================")

    try:
        input_data = event.get("input", {})

        source_url = input_data.get("source_image")
        target_url = input_data.get("target_image")

        if not source_url or not target_url:
            return {
                "success": False,
                "error": "source_image and target_image are required."
            }

        source_path = "/tmp/source.jpg"
        target_path = "/tmp/target.jpg"
        output_path = "/tmp/output.jpg"

        print("Downloading source image...")
        download_image(source_url, source_path)

        print("Downloading target image...")
        download_image(target_url, target_path)

        result_path = face_swap(
            source_path,
            target_path,
            output_path
        )

        print("Encoding output image...")

        image_base64 = encode_image(result_path)

        return {
            "success": True,
            "output_base64": image_base64
        }

    except Exception as e:
        print("========== EXCEPTION ==========")
        print(str(e))

        return {
            "success": False,
            "error": str(e)
        }


# import subprocess
# import requests
# import base64


# def download_image(url, save_path):
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }

#     response = requests.get(url, headers=headers)
#     response.raise_for_status()

#     with open(save_path, "wb") as f:
#         f.write(response.content)

#     return save_path


# def encode_image(path):
#     with open(path, "rb") as f:
#         return base64.b64encode(f.read()).decode("utf-8")

# # Start here

# def face_swap(source_path, target_path, output_path):
#     command = [
#         "python",
#         "/app/facefusion/facefusion.py",
#         # "facefusion/facefusion.py",
#         "headless-run",
#         "--source-paths", source_path,
#         "--target-path", target_path,
#         "--output-path", output_path,
#         "--processors", "face_swapper"
#     ]

#     result = subprocess.run(
#         command,
#         capture_output=True,
#         text=True,
#         timeout=600
#     )

#     print("STDOUT:")
#     print(result.stdout)

#     print("STDERR:")
#     print(result.stderr)

# if result.returncode != 0:
#     raise Exception(
#         f"Exit Code: {result.returncode}\n\n"
#         f"STDOUT:\n{result.stdout}\n\n"
#         f"STDERR:\n{result.stderr}"
#     )

#     # if result.returncode != 0:
#     #     raise Exception(result.stderr)

#     return output_path
# # def face_swap(source_path, target_path, output_path):
# #  command = [
# #     "python",
# #     "facefusion/facefusion.py",
# #     "headless-run",
# #     "-s", source_path,
# #     "-t", target_path,
# #     "-o", output_path
# # ]

# #     result = subprocess.run(
# #         command,
# #         capture_output=True,
# #         text=True,
# #         timeout=600
# #     )

# #     if result.returncode != 0:
# #         raise Exception(result.stderr)

# #     return output_path
# # Here

# def handler(event):
#     try:
#         input_data = event.get("input", {})

#         source_url = input_data.get("source_image")
#         target_url = input_data.get("target_image")

#         if not source_url or not target_url:
#             return {
#                 "success": False,
#                 "error": "source_image and target_image are required."
#             }

#         source_path = "/tmp/source.jpg"
#         target_path = "/tmp/target.jpg"
#         output_path = "/tmp/output.jpg"

#         download_image(source_url, source_path)
#         download_image(target_url, target_path)

#         result_path = face_swap(
#             source_path,
#             target_path,
#             output_path
#         )

#         image_base64 = encode_image(result_path)

#         return {
#             "success": True,
#             "output_base64": image_base64
#         }

#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e)
#         }