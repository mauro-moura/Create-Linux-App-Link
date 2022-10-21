
from glob import glob

HOME_FOLDER = '/home/mauro'
base_folder = f'{HOME_FOLDER}/Apps/*/'

apps_list = glob(base_folder)

for i in range(len(apps_list)):

    app_name = apps_list[i].split('/')[-2]
    app_exec = sorted(glob(f"{apps_list[i]}/{app_name}*"))[0]

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

