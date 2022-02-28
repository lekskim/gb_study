import os


def project_add(place, folder_struct):
    for f_dir, sec_dir in folder_struct.items():
        folder_add = os.path.join(place, f_dir)
        if not os.path.exists(folder_add):
            os.mkdir(folder_add)
        if len(sec_dir) > 0:
            for files in sec_dir:
                project_add(folder_add, files)


folder = {"my_project": [{"settings": [], "mainapp": [], "adminapp": [], "authapp": []}]}
project_add(os.getcwd(), folder)
