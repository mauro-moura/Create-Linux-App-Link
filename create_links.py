
import os

from glob import glob

HOME_FOLDER = os.path.expanduser('~')
base_folder = f'{HOME_FOLDER}/Apps/*/'
print(f"Inicializando o Aplicativo, sua pasta é {base_folder}")

apps_list = glob(base_folder)

for i in range(len(apps_list)):

    app_name = apps_list[i].split('/')[-2]
    app_exec = sorted(glob(f"{apps_list[i]}/{app_name}*"))[0]

    print(f"Adicionado App {app_name}")

    file_str = f'''
[Desktop Entry]
Name={app_name}
Comment=
Exec={app_exec}
Icon={apps_list[i]}{app_name}.ico
Terminal=false
Type=Application
StartupNotify=true
    '''

    out_folder = f'{HOME_FOLDER}/.local/share/applications/{app_name}.desktop'

    with open(out_folder, 'w') as f:
        f.write(file_str)

print("Concluído")
