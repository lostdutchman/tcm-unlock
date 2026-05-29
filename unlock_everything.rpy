init 999 python:
    # A flag to ensure this only runs once per game session
    unlock_mod_has_run = False

    def auto_unlock_achievements():
        global unlock_mod_has_run
        if unlock_mod_has_run:
            return

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

    def auto_unlock_chapters():
        global unlock_mod_has_run
        if unlock_mod_has_run:
            return

        persistent.introunlocked=True
        persistent.meet_mori=True
        persistent.mori_introcomplete=True
        persistent.mori_ch1complete=True
        persistent.mori_ch2complete=True
        persistent.mori_ch3complete=True
        persistent.mori_ch4complete=True
        persistent.mori_ch5complete=True
        persistent.mori_ch6complete=True
        persistent.mori_ch7complete=True
        persistent.meet_amir=True
        persistent.amir_introcomplete=True
        persistent.amir_ch1complete=True
        persistent.amir_ch2complete=True
        persistent.amir_ch3complete=True
        persistent.amir_ch4complete=True
        persistent.amir_ch5complete=True
        persistent.amir_ch6complete=True
        persistent.amir_ch7complete=True
        persistent.meet_akello=True
        persistent.akello_introcomplete=True
        persistent.akello_ch1complete=True
        persistent.akello_ch2complete=True
        persistent.akello_ch3complete=True
        persistent.akello_ch4complete=True
        persistent.akello_ch5complete=True
        persistent.akello_ch6complete=True
        persistent.akello_ch7complete=True
        renpy.notify("Mod: All chapters have been unlocked")

    def auto_unlock_gallery():
        global unlock_mod_has_run
        if unlock_mod_has_run:
            return
        unlock_mod_has_run = True

        persistent.unlock_mori_intro_cg = True
        persistent.unlock_mori_ch2_cg = True
        persistent.unlock_mori_ch4_cg = True
        persistent.unlock_mori_ch6_cg = True
        persistent.unlock_mori_ch8_1cg = True
        persistent.unlock_mori_ch8_2cg = True
        persistent.unlock_amir_intro_cg = True
        persistent.unlock_amir_ch2_cg = True
        persistent.unlock_amir_ch4_cg = True
        persistent.unlock_amir_ch6_cg = True
        persistent.unlock_amir_ch8_1cg = True
        persistent.unlock_amir_ch8_2cg = True
        persistent.unlock_akello_intro_cg = True
        persistent.unlock_akello_ch2_cg = True
        persistent.unlock_akello_ch4_cg = True
        persistent.unlock_akello_ch6_cg = True
        persistent.unlock_akello_ch8_1cg = True
        persistent.unlock_akello_ch8_2cg = True
        renpy.notify("Mod: All gallery images have been unlocked")

screen auto_unlock():
    timer 10.0 action Function(auto_unlock_chapters)
    timer 10.0 action Function(auto_unlock_gallery)
    timer 10.0 action Function(auto_unlock_achievements)

init python:
    config.overlay_screens.append("auto_unlock")
