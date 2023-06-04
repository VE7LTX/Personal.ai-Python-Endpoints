"""
Activity Logger

Author: Matthew Schafer
Date: April 17, 2023
Description: A script to log user activity and upload it to Personal.ai.

Dependencies:
- keyboard
- win32gui
- win32process
- re
- psutil
- requests
- datetime
- threading
- time
- traceback
- atexit
"""

import keyboard
import win32gui
import win32process
import re
import psutil
import requests
from datetime import datetime
import threading
import time
import traceback
import atexit


api_key = input("Please enter your API key: ")
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}
print("Thank you, You entered:", api_key)


class ActivityLogger:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.logs = []
        self.buffer = ""
        self.buffer_size = 100

    def on_keyboard_event(self, event):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        if event.name.isprintable():
            self.buffer += event.name
        else:
            self.buffer += f"[{event.name}]"

        if len(self.buffer) >= self.buffer_size:
            log = (current_time, "KEYSTROKE", self.buffer)
            self.logs.append(log)
            self.buffer = ""

        return True

    def on_app_activity_event(self, event):
        process_id = event["process_id"]
        process_name = event["process_name"]
        window_text = event["window_text"]
        current_time = datetime.now()
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        self.log_and_upload_activity(process_id, process_name, window_text)
        print(f"{current_time_str} {process_name} {window_text}")

    def log_and_upload_activity(self, process_id, process_name, window_text):
        browser_tab = self.get_browser_tab(process_id, process_name, window_text)
        current_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if browser_tab:
            log = (current_time_str, process_name, window_text, browser_tab)
        else:
            log = (current_time_str, process_name, window_text)

        self.logs.append(log)
        self.upload_logs()

    def get_browser_tab(self, process_id, process_name, window_text):
        process = psutil.Process(process_id)

        if process_name.endswith("chrome.exe"):
            browser_name = "Google Chrome"
        elif process_name.endswith("firefox.exe"):
            browser_name = "Mozilla Firefox"
        elif process_name.endswith("brave.exe"):
            browser_name = "Brave"
        elif process_name.endswith("msedge.exe"):
            browser_name = "Microsoft Edge"
        else:
            return None

        match = re.search(f" - {browser_name}$", window_text)
        if match:
            tab_title = re.sub(f" - {browser_name}$", "", window_text)
            return tab_title

        return None
    
    def upload_logs(self):
        if not self.logs:
            return

        for log in self.logs:
            try:
                log_sequence = f"{log[0]} {log[1]} {log[2]}"
                response = self.upload_log_memory(log_sequence, self.base_url, self.headers)
                if response.status_code == 200:
                    print(f"\nLog memory object uploaded: {log_sequence}")
                else:
                    print(f"Failed to upload log memory object. Status code: {response.status_code}")
                    print(f"Response content: {response.content}")
            except Exception as e:
                print(f"Error in upload_logs: {str(e)}")
                print(traceback.format_exc())

        self.logs = []
        
    def upload_log_memory(self, log_sequence, base_url, headers):
        memory_url = base_url
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        memory_object = {
            "Text": "Log Incoming From VE7LTX.CC Logging App:  " + log_sequence,
            "StartTime": current_time,
            "SourceApp": "VE7LTX.CC Computer Logging Python App",
            "Type": "activity_log"  # Update the "Type" property to "activity_log"
        }

        print(f"Uploading log to: {memory_url}")
        print(f"Using headers: {headers}")
        print(f"Memory object: {memory_object}")

        response = requests.post(memory_url, json=memory_object, headers=headers)
        return response
    
    def get_active_window_info(self):
        window_handle = win32gui.GetForegroundWindow()
        window_text = win32gui.GetWindowText(window_handle)
        _, process_id = win32process.GetWindowThreadProcessId(window_handle)
        process = psutil.Process(process_id)
        process_name = process.name()
        return {"process_id": process_id, "process_name": process_name, "window_text": window_text}

    def run(self):
        keyboard.on_press(self.on_keyboard_event)

        def check_active_window():
            last_active_window = None
            while True:
                active_window = self.get_active_window_info()
                if last_active_window != active_window:
                    self.on_app_activity_event(active_window)
                    last_active_window = active_window
                time.sleep(1)

        window_checker_thread = threading.Thread(target=check_active_window)
        window_checker_thread.start()

        atexit.register(self.on_exit)

        while True:
            time.sleep(60)

    def on_exit(self):
        if len(self.buffer) > 0:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            log = (current_time, "KEYSTROKE", self.buffer)
            self.logs.append(log)

        def cleanup():
            print("Cleaning up and uploading logs...")
            self.upload_logs()

        atexit.register(cleanup)

        while True:
            time.sleep(60)
            

if __name__ == "__main__":
    API_ENDPOINT = "https://api.personal.ai/v1/memory"


    logger = ActivityLogger(API_ENDPOINT, HEADERS)

    logger.run()