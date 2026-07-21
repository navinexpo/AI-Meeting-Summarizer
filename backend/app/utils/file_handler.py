import os
import shutil
from fastapi import UploadFile

class FileHandler:
    @staticmethod
    def save_temp_file(upload_file: UploadFile, target_dir: str) -> str:
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, upload_file.filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
            
        return file_path
# OS Path module is used to handle file paths and directories, while the shutil module is used to copy the uploaded file to the target directory. The save_temp_file method takes an UploadFile object and a target directory path as input, saves the uploaded file to the specified directory, and returns the path of the saved file.
    @staticmethod
    def delete_file(file_path: str):
        if os.path.exists(file_path):
            os.remove(file_path)