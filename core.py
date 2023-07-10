from utilities import wait_for_key_press as wait, add_item_to_menus, remove_item_from_menus, update_item_title_from_menus, get_UUID as UUID
from consolemenu import *
from consolemenu.items import *

menus: list[ConsoleMenu] = []

def mnu_add_to_list(menu: ConsoleMenu) -> None:
    if menu:
        menus.append(menu)

def wait_key() -> None:
    wait("\n>> Press a key to continue...")

def pp_get_mnu_edit_jobs() -> list[dict]:
    return  [
                {"title": "Job A", "type": "func", "exec": "core.pp_edit_job", "args": ["Job A"]},
                {"title": "Job B", "type": "func", "exec": "core.pp_edit_job", "args": ["Job B"]},
                {"title": "Job C", "type": "func", "exec": "core.pp_edit_job", "args": ["Job C"]},
            ]

def pp_get_mnu_delete_jobs() -> list[dict]:
    return  [
                {"title": "Job A", "type": "func", "exec": "core.pp_del_job", "args": ["Job A"]},
                {"title": "Job B", "type": "func", "exec": "core.pp_del_job", "args": ["Job B"]},
                {"title": "Job C", "type": "func", "exec": "core.pp_del_job", "args": ["Job C"]},
            ]

def pp_get_mnu_run_jobs() -> list[dict]:
    return  [
                {"title": "Job A", "type": "func", "exec": "core.pp_run_job", "args": ["Job A"]},
                {"title": "Job B", "type": "func", "exec": "core.pp_run_job", "args": ["Job B"]},
                {"title": "Job C", "type": "func", "exec": "core.pp_run_job", "args": ["Job C"]},
            ]

def pp_edit_job(name: str) -> None:
    try:
        new_name: str = "Job " + UUID()
        update_item_title_from_menus(menus, name, new_name)
        ...
        print(f"{name} renamed as {new_name}.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")
    finally:
        wait_key()

def pp_del_job(name: str) -> None:
    print(name + " deleted.")
    remove_item_from_menus(menus, name)
    wait_key()

def pp_run_job(name: str) -> None:
    print(name + " running.")
    wait_key()

def pp_create_job() -> None:
    new_item_name: str = "Job " + UUID()
    print(f"{new_item_name} created.")
    run_item: FunctionItem = FunctionItem(new_item_name, pp_run_job, [new_item_name])
    edit_item: FunctionItem = FunctionItem(new_item_name, pp_edit_job, [new_item_name])
    del_item: FunctionItem = FunctionItem(new_item_name, pp_del_job, [new_item_name])
    add_item_to_menus(menus = menus, item = run_item, exclude_by_names = ['Edit', 'Delete', 'main'])
    add_item_to_menus(menus, edit_item, ['Edit'], True)
    add_item_to_menus(menus = menus, item = del_item, exclude_by_names = ['edit job', 'run job', 'main menu'], exclude_by_name_sub_str = False)
    wait_key()
    
