
import traceback
from typing import Optional, Sequence, Mapping, Any
from consolemenu import *
from consolemenu.items import *
import importlib

func_modules: list[str] = []
menus: list[ConsoleMenu] = []

def add_to_mod_list(module: str) -> None:
    if module in func_modules:
        return None
    func_modules.append(module)

def add_to_mnu_list(menu: ConsoleMenu) -> None:
    if (menu):
        menus.append(menu)

def add_to_modules_mnu_list() -> None:
    for mod in func_modules:
        for mnu in menus:
            func = get_func_ref(f"{mod}.mnu_add_to_list")
            if func:
                func(mnu)

def get_func_ref(func_name: str):

    try:
        parts: list[str] = func_name.split('.')
        if parts and (len(parts) == 2):
            module = importlib.import_module(parts[0])
            func = getattr(module, parts[1])
            if func:
                add_to_mod_list(parts[0])
                return func
            else:
                return None
        else:
            return None
    except Exception:
        return None

def run_menu(menu: ConsoleMenu) -> Optional[str]:
    try:
        return menu.show()
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        filename, line, fn, code = tb[-1]
        desc = str(e)
        return f"[{filename}, {fn}, {line}] {desc}"

def create_menu(mnu: dict, err: list, screen = None, formatter = None, clear_screen = True, show_exit_option = True, exit_option_text = 'Exit', exit_menu_char = None) -> Optional[ConsoleMenu]:
    
    try:

        err[0] = False
        err[1] = None
        err[2] = None
        title = None
        subtitle = None
        prologue_text = None
        epilogue_text = None

        if "title" in mnu.keys():
            title = mnu["title"]

        if "subtitle" in mnu.keys():
            subtitle = mnu["subtitle"]

        if "prologue_text" in mnu.keys():
            prologue_text = mnu["prologue_text"]

        if "epilogue_text" in mnu.keys():
            epilogue_text = mnu["epilogue_text"]

        menu: ConsoleMenu = ConsoleMenu (
                                            title = title, 
                                            subtitle = subtitle, 
                                            screen = screen, 
                                            formatter = formatter,
                                            prologue_text = prologue_text, 
                                            epilogue_text = epilogue_text, 
                                            clear_screen = clear_screen,
                                            show_exit_option = show_exit_option, 
                                            exit_option_text = exit_option_text, 
                                            exit_menu_char = exit_menu_char
                                        )
        
        if "items" in mnu.keys():
            items = mnu["items"]
            if isinstance(items, str):
                func = get_func_ref(items)
                if func:
                    items: list[dict] = func()
                else:
                    raise Exception("Bad value for 'items' in menu " + title)
            for item in items:
                item_title: str = None
                if "title" in item.keys():
                    item_title = item["title"]
                exec: str = None
                if "exec" in item.keys():
                    exec = item["exec"]
                args: Sequence[Any] = None
                if "args" in item.keys():
                    args = item["args"]
                kwargs: Mapping[str, Any] = None 
                if "kwargs" in item.keys():
                    kwargs = item["kwargs"]
                if "submenu" in item.keys():
                    err: list = [False, None, None]
                    submenu: ConsoleMenu = create_menu   (
                                                item["submenu"], 
                                                err, 
                                                screen, 
                                                formatter, 
                                                clear_screen, 
                                                show_exit_option, 
                                                exit_option_text, 
                                                exit_menu_char
                                            )
                    if submenu:
                        new_item: SubmenuItem = SubmenuItem(item_title, submenu, menu)
                        menu.append_item(new_item)
                    else:
                        if err[0] == True:
                            raise Exception(err[1])
                        else:
                            raise Exception(f"Not recognized error creating subdomain for item '{item_title}' in menu '{title}'.")
                else:
                    if "type" in item.keys():
                        type: str = item["type"]
                        if type == 'func':
                            if exec:
                                item_func = get_func_ref(exec)
                                if item_func:
                                    menu.append_item(FunctionItem(item_title, item_func, args, kwargs))
                                else:
                                    raise Exception(f"Bad exec for item '{item_title}' in menu '{title}'.")
                            else:
                                raise Exception(f"Exec not found for item '{item_title}' in menu '{title}'.")
                        elif type == 'cmd':
                            if exec:
                                ...
                            else:
                                raise Exception(f"Exec not found for item '{item_title}' in menu '{title}'.")
                        else:
                            raise Exception(f"Bad type for item '{item_title}' in menu '{title}'.")
                    else:
                        raise Exception(f"Type not found for item '{item_title}' in menu '{title}'.")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        filename, line, fn, code = tb[-1]
        desc = str(e)
        err[0] = True
        err[1] = f"[{filename}, {fn}, {line}] {desc}"
        err[2] = e
        menu = None
    finally:
        add_to_mnu_list(menu)
        add_to_modules_mnu_list()
        return menu
