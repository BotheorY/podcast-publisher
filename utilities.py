import os
from consolemenu import *
from consolemenu.items import *
import uuid

if os.name == 'nt':  # Windows
    import msvcrt
elif os.name == 'posix':  # Unix, Linux, macOS
    import sys
    import termios
    import tty
else:
    raise Exception("Operating system not supported")

def wait_for_key_press(prompt: str = None) -> None:    
    if prompt != None:
        print(prompt)
    if os.name == 'nt':  # Windows
        msvcrt.getch()
    elif os.name == 'posix':  # Unix, Linux, macOS
        # Save current terminal settings
        fd = sys.stdin.fileno()
        settings = termios.tcgetattr(fd)
        try:
            # Put the terminal in raw mode to read the pressed keys
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)  # Waits for a key press
        finally:
            # Restore the terminal settings
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)

def remove_item_from_menus(menus: list[ConsoleMenu], item: str) -> None:    
    if menus:
        item = item.upper()
        remove_items: list[MenuItem] = []
        for menu in menus:
            for mnu_item in menu.items:
                if mnu_item.text.upper() == item:
                    remove_items.append(mnu_item)
            for mnu_item in remove_items:
                menu.remove_item(mnu_item)
                no_items: int = 0
                if menu.show_exit_option:
                    no_items = 1
                if len(menu.items) > no_items:
                    menu.current_option = 0
                else:
                    menu.selected_option = -1
            remove_items.clear()

def add_item_to_menus(menus: list[ConsoleMenu], item: MenuItem, include_by_names: list[str] = None, include_by_name_sub_str: bool = True, exclude_by_names: list[str] = None, exclude_by_name_sub_str: bool = True) -> None:
    
    if menus:
        for menu in menus:
            ok: bool = (include_by_names == None) and (exclude_by_names == None)
            if not ok:
                menu_name: str = menu.title.upper()
                if exclude_by_names:
                    exclude_by_names = [s.upper() for s in exclude_by_names]
                    if exclude_by_name_sub_str:
                        ok = False
                        for s in exclude_by_names:
                            if s in menu_name:
                                ok = True
                                break
                        ok = not ok
                    else:
                        ok = not (menu_name in exclude_by_names)
                else:
                    ok = True
                if ok and include_by_names:
                    include_by_names = [s.upper() for s in include_by_names]
                    if include_by_name_sub_str:
                        ok = False
                        for s in include_by_names:
                            if s in menu_name:
                                ok = True
                                break
                    else:
                        ok = menu_name in include_by_names
            if ok:
                found = False
                for mnu_item in menu.items:
                    if mnu_item.text == item.text:
                        found = True
                        break
                if not found:
                    menu.append_item(item)

def get_UUID(no_dashes: bool = True) -> str:
    res: str = str(uuid.uuid4())
    if no_dashes:
        res = res.replace('-', '')
    return res
