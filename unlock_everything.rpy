init 999 python:
    unlock_mod_has_run = False
    all_mod_unlocks = [
        ("introunlocked", "Prologue"),
        ("meet_mori", "Mori Intro"),
        ("mori_introcomplete", "Mori Chapter 1"),
        ("mori_ch1complete", "Mori Chapter 2"),
        ("mori_ch2complete", "Mori Chapter 3"),
        ("mori_ch3complete", "Mori Chapter 4"),
        ("mori_ch4complete", "Mori Chapter 5"),
        ("mori_ch5complete", "Mori Chapter 6"),
        ("mori_ch6complete", "Mori Chapter 7"),
        ("mori_ch7complete", "Mori Chapter 8"),
        
        ("meet_amir", "Amir Intro"),
        ("amir_introcomplete", "Amir Chapter 1"),
        ("amir_ch1complete", "Amir Chapter 2"),
        ("amir_ch2complete", "Amir Chapter 3"),
        ("amir_ch3complete", "Amir Chapter 4"),
        ("amir_ch4complete", "Amir Chapter 5"),
        ("amir_ch5complete", "Amir Chapter 6"),
        ("amir_ch6complete", "Amir Chapter 7"),
        ("amir_ch7complete", "Amir Chapter 8"),
        
        ("meet_akello", "Akello Intro"),
        ("akello_introcomplete", "Akello Chapter 1"),
        ("akello_ch1complete", "Akello Chapter 2"),
        ("akello_ch2complete", "Akello Chapter 3"),
        ("akello_ch3complete", "Akello Chapter 4"),
        ("akello_ch4complete", "Akello Chapter 5"),
        ("akello_ch5complete", "Akello Chapter 6"),
        ("akello_ch6complete", "Akello Chapter 7"),
        ("akello_ch7complete", "Akello Chapter 8"),

        ("unlock_mori_intro_cg", "Mori Intro CG"),
        ("unlock_mori_ch2_cg", "Mori Chapter 2 CG"),
        ("unlock_mori_ch4_cg", "Mori Chapter 4 CG"),
        ("unlock_mori_ch6_cg", "Mori Chapter 6 CG"),
        ("unlock_mori_ch8_1_cg", "Mori Chapter 8 Monster CG"),
        ("unlock_mori_ch8_2_cg", "Mori Chapter 8 Human CG"),
        
        ("unlock_amir_intro_cg", "Amir Intro CG"),
        ("unlock_amir_ch2_cg", "Amir Chapter 2 CG"),
        ("unlock_amir_ch4_cg", "Amir Chapter 4 CG"),
        ("unlock_amir_ch6_cg", "Amir Chapter 6 CG"),
        ("unlock_amir_ch8_1_cg", "Amir Chapter 8 Monster CG"),
        ("unlock_amir_ch8_2_cg", "Amir Chapter 8 Human CG"),
        
        ("unlock_akello_intro_cg", "Akello Intro CG"),
        ("unlock_akello_ch2_cg", "Akello Chapter 2 CG"),
        ("unlock_akello_ch4_cg", "Akello Chapter 4 CG"),
        ("unlock_akello_ch6_cg", "Akello Chapter 6 CG"),
        ("unlock_akello_ch8_1_cg", "Akello Chapter 8 Monster CG"),
        ("unlock_akello_ch8_2_cg", "Akello Chapter 8 Human CG")
    ]

    pending_mod_unlocks = []
    for lock, lock_description in all_mod_unlocks:
        if getattr(persistent, lock) != True:
            pending_mod_unlocks.append((lock, lock_description))

    def process_next_unlock():
        global unlock_mod_has_run
        
        if pending_mod_unlocks:
            lock, lock_description = pending_mod_unlocks.pop(0)
            setattr(persistent, lock, True)
            renpy.notify("Unlock_Mod: " + lock_description + " has been unlocked")
        
        elif not unlock_mod_has_run:
            auto_unlock_achievements()
            unlock_mod_has_run = True

    def auto_unlock_achievements():
        if achievement.steam is not None:
            steam_achievements = achievement.steam.list_achievements()
            if steam_achievements:
                unlocked_count = 0
                for ach_id in steam_achievements:
                    if not achievement.has(ach_id):
                        achievement.grant(ach_id)
                        unlocked_count += 1
                
                if unlocked_count > 0:
                    achievement.sync()
                    renpy.notify(f"Mod: Unlocked {unlocked_count} Steam Achievements!")
                else:
                    renpy.notify("Mod: All Steam achievements were already unlocked.")
            else:
                renpy.notify("Mod: No achievements found on Steam.")
        else:
            renpy.notify("Mod: Steam API not detected.")


screen auto_unlock():
    if pending_mod_unlocks or not unlock_mod_has_run:
        timer 4.0 action Function(process_next_unlock) repeat True

init python:
    config.overlay_screens.append("auto_unlock")