from utilities import wait_for_key_press as wait, add_item_to_menus, remove_item_from_menus, update_item_title_from_menus, get_UUID as UUID
from consolemenu import *
from consolemenu.items import *

menus: list[ConsoleMenu] = []

def mnu_add_to_list(menu: ConsoleMenu) -> None:
    if menu:
        menus.append(menu)

def wait_key() -> None:
    wait("\n>> Press a key to continue...")

def pp_get_mnu_view_jobs() -> list[dict]:
    return  [
                {"title": "Job A", "type": "func", "exec": "core.pp_view_job", "args": ["Job A"]},
                {"title": "Job B", "type": "func", "exec": "core.pp_view_job", "args": ["Job B"]},
                {"title": "Job C", "type": "func", "exec": "core.pp_view_job", "args": ["Job C"]},
            ]

def pp_get_mnu_view_sources() -> list[dict]:
    return  [
                {"title": "Source A", "type": "func", "exec": "core.pp_view_source", "args": ["Source A"]},
                {"title": "Source B", "type": "func", "exec": "core.pp_view_source", "args": ["Source B"]},
                {"title": "Source C", "type": "func", "exec": "core.pp_view_source", "args": ["Source C"]},
            ]

def pp_get_mnu_view_targets() -> list[dict]:
    return  [
                {"title": "Terget A", "type": "func", "exec": "core.pp_view_target", "args": ["Terget A"]},
                {"title": "Terget B", "type": "func", "exec": "core.pp_view_target", "args": ["Terget B"]},
                {"title": "Terget C", "type": "func", "exec": "core.pp_view_target", "args": ["Terget C"]},
            ]

def pp_get_mnu_edit_jobs() -> list[dict]:
    return  [
                {"title": "Job A", "type": "func", "exec": "core.pp_edit_job", "args": ["Job A"]},
                {"title": "Job B", "type": "func", "exec": "core.pp_edit_job", "args": ["Job B"]},
                {"title": "Job C", "type": "func", "exec": "core.pp_edit_job", "args": ["Job C"]},
            ]

def pp_get_mnu_edit_sources() -> list[dict]:
    return  [
                {"title": "Source A", "type": "func", "exec": "core.pp_edit_source", "args": ["Source A"]},
                {"title": "Source B", "type": "func", "exec": "core.pp_edit_source", "args": ["Source B"]},
                {"title": "Source C", "type": "func", "exec": "core.pp_edit_source", "args": ["Source C"]},
            ]

def pp_get_mnu_edit_targets() -> list[dict]:
    return  [
                {"title": "Target A", "type": "func", "exec": "core.pp_edit_target", "args": ["Target A"]},
                {"title": "Target B", "type": "func", "exec": "core.pp_edit_target", "args": ["Target B"]},
                {"title": "Target C", "type": "func", "exec": "core.pp_edit_target", "args": ["Target C"]},
            ]

def pp_get_mnu_delete_jobs() -> list[dict]:
    return  [
                {"title": "Job A", "type": "func", "exec": "core.pp_del_job", "args": ["Job A"]},
                {"title": "Job B", "type": "func", "exec": "core.pp_del_job", "args": ["Job B"]},
                {"title": "Job C", "type": "func", "exec": "core.pp_del_job", "args": ["Job C"]},
            ]

def pp_get_mnu_delete_sources() -> list[dict]:
    return  [
                {"title": "Source A", "type": "func", "exec": "core.pp_del_source", "args": ["Source A"]},
                {"title": "Source B", "type": "func", "exec": "core.pp_del_source", "args": ["Source B"]},
                {"title": "Source C", "type": "func", "exec": "core.pp_del_source", "args": ["Source C"]},
            ]

def pp_get_mnu_delete_targets() -> list[dict]:
    return  [
                {"title": "Target A", "type": "func", "exec": "core.pp_del_target", "args": ["Target A"]},
                {"title": "Target B", "type": "func", "exec": "core.pp_del_target", "args": ["Target B"]},
                {"title": "Target C", "type": "func", "exec": "core.pp_del_target", "args": ["Target C"]},
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

def pp_edit_source(name: str) -> None:
    print(name + " edited.")
    wait_key()

def pp_edit_target(name: str) -> None:
    print(name + " edited.")
    wait_key()

def pp_del_job(name: str) -> None:
    print(name + " deleted.")
    remove_item_from_menus(menus, name)
    wait_key()

def pp_run_job(name: str) -> None:
    print(name + " running.")
    wait_key()

def pp_view_job(name: str) -> None:
    print(name + " view.")
    wait_key()

def pp_view_source(name: str) -> None:
    print(name + " view.")
    wait_key()

def pp_view_target(name: str) -> None:
    print(name + " view.")
    wait_key()

def pp_del_source(name: str) -> None:
    print(name + " deleted.")
    wait_key()

def pp_del_target(name: str) -> None:
    print(name + " deleted.")
    wait_key()

def pp_create_job() -> None:
    new_item_name: str = "Job " + UUID()
    print(f"{new_item_name} created.")
    run_item: FunctionItem = FunctionItem(new_item_name, pp_run_job, [new_item_name])
    edit_item: FunctionItem = FunctionItem(new_item_name, pp_edit_job, [new_item_name])
    del_item: FunctionItem = FunctionItem(new_item_name, pp_del_job, [new_item_name])
    view_item: FunctionItem = FunctionItem(new_item_name, pp_view_job, [new_item_name])
    add_item_to_menus(menus, run_item, ['Run Job'], False)
    add_item_to_menus(menus, edit_item, ['Edit Job'], False)
    add_item_to_menus(menus, del_item, ['Delete Job'], False)
    add_item_to_menus(menus, view_item, ['View Job'], False)
    wait_key()

def pp_add_source() -> None:
    new_item_name: str = "Source " + UUID()
    print(f"{new_item_name} added.")
    wait_key()

def pp_set_crypto_key() -> None:
    print("Crypto key setted.")
    wait_key()

def pp_add_target() -> None:
    new_item_name: str = "Target " + UUID()
    print(f"{new_item_name} added.")
    wait_key()
    
