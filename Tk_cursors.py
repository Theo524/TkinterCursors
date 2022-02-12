from tkinter import *

cursors = ['X_cursor', 'arrow', 'based_arrow_down', 'based_arrow_up', 'boat',
           'bogosity', 'bottom_left_corner', 'bottom_right_corner', 'bottom_side',
           'bottom_tee', 'box_spiral', 'center_ptr', 'circle', 'clock',
           'coffee_mug', 'cross', 'cross_reverse', 'crosshair', 'diamond_cross',
           'dot', 'dotbox', 'double_arrow', 'draft_large', 'draft_small', 'draped_box',
           'exchange', 'fleur', 'gobbler', 'gumby', 'hand1', 'hand2', 'heart',
           'icon', 'iron_cross', 'left_ptr', 'left_side', 'left_tee', 'leftbutton',
           'll_angle', 'lr_angle', 'man', 'middlebutton', 'mouse', 'pencil', 'pirate',
           'plus', 'question_arrow', 'right_ptr', 'right_side', 'right_tee',
           'rightbutton', 'rtl_logo', 'sailboat', 'sb_down_arrow', 'sb_h_double_arrow',
           'sb_left_arrow', 'sb_right_arrow', 'sb_up_arrow', 'sb_v_double_arrow',
           'shuttle', 'sizing', 'spider', 'spraycan', 'star', 'target', 'tcross',
           'top_left_arrow', 'top_left_corner', 'top_right_corner', 'top_side', 'top_tee',
           'trek', 'ul_angle', 'umbrella', 'ur_angle', 'watch', 'xterm']


winn = Tk()
winn.title('Tkinter cursors')
Label(winn, text='Glide your cursor through the buttons to see how the cursor looks like', font='arial 20 bold').pack()
cursors_frame = Frame(winn)
cursors_frame.pack()
x = 0
y = 0

for item in cursors:
    Button(cursors_frame, cursor=item, text=item, width=15, height=3).grid(column=x, row=y, pady=5, padx=5)

    if x == 9:
        x = 0
        y += 1
        continue

    x += 1

winn.mainloop()
