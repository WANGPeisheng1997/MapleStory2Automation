from simulate import *


class Key:
    x = 0x2d
    space = 0x39
    up = 0xc8
    lalt = 0x38
    backslash = 0x2b
    enter = 0x1c


enter_pos_x, enter_pos_y = 1000, 1000 #进入副本按钮位置
running_time = 1 #进图跑动时间
interact_key = Key.lalt #过图按钮
exit_key = Key.backslash #染色工坊
enter_key = Key.enter #确认回车按钮


def go_to_ranse():
    tap_key(exit_key)
    tap_key(enter_key)


def huoxiyi_graph():
    enter_hall()
    sleep(3)
    run_to_the_entrance()
    enter_raid()
    sleep(30)
    go_to_ranse()



while(True):
    print(mouse_position())
    # mouse_click(1000, 1000)
    # tap_key(Key.x)
    # hold_key(Key.up, 1)

    # go_to_ranse()
    sleep(1)

