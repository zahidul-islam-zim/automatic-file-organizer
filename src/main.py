import os
import shutil

folder = os.path.expanduser("~/Downloads/")

niyom = {
    "Photos": [".jpg", ".jpeg", ".png", ".gif"],
    "PDF": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov", ".webm", ".avi"],
}

for file_name in os.listdir(folder):
    old_path = os.path.join(folder, file_name)

    if os.path.isfile(old_path):
        extension = os.path.splitext(file_name)[1].lower()

        for folder_name, ext_list in niyom.items():
            if extension in ext_list:
                target = os.path.join(folder, folder_name)
                os.makedirs(target, exist_ok=True)
                shutil.move(old_path, os.path.join(target, file_name))
                print(f"{file_name} → {folder_name}/")
                break