import runpod
from handler import handler

print("===================================")
print("RUNPOD WORKER STARTED SUCCESSFULLY")
print("===================================")

runpod.serverless.start({
    "handler": handler
})

# import runpod
# from handler import handler

# runpod.serverless.start({
#     "handler": handler
# })
