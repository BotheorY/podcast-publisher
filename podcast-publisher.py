from menu import run_menu as rm, create_menu as cm

def main() -> None:

    menu: dict =    {
                        "title": "MAIN MENU",
                        "items":    [
                                        {"title": "Run Job",
                                            "submenu":  {
                                                            "title": "Run Job",
                                                            "subtitle": "Choose the job to run:",
                                                            "items": "core.pp_get_mnu_run_jobs"
                                                        }
                                        },
                                        {"title": "Create Job", "type": "func", "exec": "core.pp_create_job"},
                                        {"title": "Edit Job...",
                                            "submenu":  {
                                                            "title": "Edit Job",
                                                            "subtitle": "Choose the job to edit:",
                                                            "items": "core.pp_get_mnu_edit_jobs"
                                                        }
                                        },
                                        {"title": "View Job...",
                                            "submenu":  {
                                                            "title": "View Job",
                                                            "subtitle": "Choose the job to view:",
                                                            "items": "core.pp_get_mnu_view_jobs"
                                                        }
                                        },
                                        {"title": "Delete Job...",
                                            "submenu":  {
                                                            "title": "Delete Job",
                                                            "subtitle": "Choose the job to delete:",
                                                            "items": "core.pp_get_mnu_delete_jobs"
                                                        }
                                        },
                                        {"title": "Settings...",
                                            "submenu":  {
                                                            "title": "Settings",
                                                            "items":    [
                                                                                                                    {"title": "Set Cryptographic Key", "type": "func", "exec": "core.pp_set_crypto_key"},

                                                                            {"title": "Set Sources...",
                                                                                "submenu":  {
                                                                                                "title": "Set Sources",
                                                                                                "items":    [
                                                                                                                {"title": "Add Source", "type": "func", "exec": "core.pp_add_source"},
                                                                                                                {"title": "Edit Source...",
                                                                                                                    "submenu":  {
                                                                                                                                    "title": "Edit Source",
                                                                                                                                    "subtitle": "Choose the source to edit:",
                                                                                                                                    "items": "core.pp_get_mnu_edit_sources"
                                                                                                                                }
                                                                                                                },
                                                                                                                {"title": "View Source...",
                                                                                                                    "submenu":  {
                                                                                                                                    "title": "View Source",
                                                                                                                                    "subtitle": "Choose the source to view:",
                                                                                                                                    "items": "core.pp_get_mnu_view_sources"
                                                                                                                                }
                                                                                                                },
                                                                                                                {"title": "Delete Source...",
                                                                                                                    "submenu":  {
                                                                                                                                    "title": "Delete Source",
                                                                                                                                    "subtitle": "Choose the source to delete:",
                                                                                                                                    "items": "core.pp_get_mnu_delete_sources"
                                                                                                                                }
                                                                                                                }

                                                                                                            ]
                                                                                            }
                                                                            },
                                                                            {"title": "Set Targets...",
                                                                                                                                                                                                "submenu":  {
                                                                                                                                                                                                                "title": "Set Targets",
                                                                                                                                                                                                                "items":    [
                                                                                                                                                                                                                                {"title": "Add Target", "type": "func", "exec": "core.pp_add_target"},
                                                                                                                                                                                                                                {"title": "Edit Target...",
                                                                                                                                                                                                                                    "submenu":  {
                                                                                                                                                                                                                                                    "title": "Edit Target",
                                                                                                                                                                                                                                                    "subtitle": "Choose the target to edit:",
                                                                                                                                                                                                                                                    "items": "core.pp_get_mnu_edit_targets"
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                },
                                                                                                                                                                                                                                {"title": "View Target...",
                                                                                                                                                                                                                                    "submenu":  {
                                                                                                                                                                                                                                                    "title": "View Target",
                                                                                                                                                                                                                                                    "subtitle": "Choose the target to view:",
                                                                                                                                                                                                                                                    "items": "core.pp_get_mnu_view_targets"
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                },
                                                                                                                                                                                                                                {"title": "Delete Target...",
                                                                                                                                                                                                                                    "submenu":  {
                                                                                                                                                                                                                                                    "title": "Delete Target",
                                                                                                                                                                                                                                                    "subtitle": "Choose the target to delete:",
                                                                                                                                                                                                                                                    "items": "core.pp_get_mnu_delete_targets"
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                }

                                                                                                                                                                                                                            ]
                                                                                                                                                                                                            }
                                                                                                                                                        }                                                                            
                                                                        ]
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
