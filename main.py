import os


def exist_folder(parent_dir: str, dir_list: list[str]):
    has = False
    for i in dir_list:
        if os.path.isdir(os.path.join(parent_dir, i)):
            has = True
            break
    return has


def loop_folder(parent_dir: str, res_list: list[str]):
    sub_dir = os.listdir(parent_dir)
    if not exist_folder(parent_dir, sub_dir):
        res_list.append(parent_dir)
        return
    for i in sub_dir:
        new_dir = os.path.join(parent_dir, i)
        if os.path.isfile(new_dir):
            continue
        if not exist_folder(new_dir, os.listdir(new_dir)):
            res_list.append(new_dir)
            continue
        loop_folder(new_dir, res_list)


def main():
    parent_dir = 'a1'
    res_list = []
    loop_folder(parent_dir, res_list)
    print(res_list)


def main_inno(parent_dir: str):

    res_list: list[str] = []
    loop_folder(parent_dir, res_list)
    print(res_list)

    inno_list: list[str] = []
    for i in res_list:
        end = i.replace(parent_dir, '', 1)
        val = f'Source: "{i}\*"; DestDir: "{{app}}{end}"; Flags: ignoreversion recursesubdirs'
        inno_list.append(val)

    for i in inno_list:
        print(i)


if __name__ == '__main__':
    # main()
    parent_dir = r'C:\Users\Administrator\Desktop\okjx'
    main_inno(parent_dir)
