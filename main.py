from fastapi import FastAPI
import psutil
import subprocess
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/logs")
def read_logs():
    with open("logs.txt", "r") as file:
        return file.read()


def get_temperature():
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
        return float(temp.split("=")[1].split("'")[0])
    except Exception as e:
        return str(e)


@app.get("/status")
async def read_status():
    cpu_temp = get_temperature()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    return {
        "cpu_temp": cpu_temp,
        "cpu_usage": cpu_usage,
        "memory": memory,
        "disk_usage": disk_usage,
    }


