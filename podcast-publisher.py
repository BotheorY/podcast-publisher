from menu import run_menu as rm, create_menu as cm

def main() -> None:

    menu: dict =    {
                        "title": "MAIN MENU",
                        "items":    [
                                        {"title": "Run job",
                                            "submenu":  {
                                                            "title": "Run job",
                                                            "subtitle": "Choose the job to run:",
                                                            "items": "core.pp_get_mnu_run_jobs"
                                                        }
                                        },
                                        {"title": "Create job", "type": "func", "exec": "core.pp_create_job"},
                                        {"title": "Edit job",
                                            "submenu":  {
                                                            "title": "Edit job",
                                                            "subtitle": "Choose the job to edit:",
                                                            "items": "core.pp_get_mnu_edit_jobs"
                                                        }
                                        },
                                        {"title": "Delete job",
                                            "submenu":  {
                                                            "title": "Delete job",
                                                            "subtitle": "Choose the job to delete:",
                                                            "items": "core.pp_get_mnu_delete_jobs"
                                                        }
                                        }
                                    ]
                    }
    err: list = [False, None, None]
    err_msg: str = None
    res = rm(cm(menu, err))

    if err[0]:
        err_msg = err[1]

    if res:
        if err_msg:
            err_msg = err_msg + " \n" + res
        else:
            err_msg = res

    if err_msg:
        print("[ERROR] " + err_msg)

if __name__ == '__main__':
    main()
