import curses

menu_options = ["Option 1: View Profile", 
                "Option 2: Edit Settings", 
                "Option 3: Log Out", 
                "Option 4: Exit"]

def navigate_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    current_option = 0  # Initial option

    while True:
        stdscr.clear()  # Clear the screen

        # Display menu and highlight the selected option
        for idx, option in enumerate(menu_options):
            if idx == current_option:
                stdscr.addstr(idx, 0, option, curses.A_REVERSE)  # Highlight current option
            else:
                stdscr.addstr(idx, 0, option)

        stdscr.refresh()  # Refresh the screen

        key = stdscr.getch()  # Capture key press

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1  # Move up the list
        elif key == curses.KEY_DOWN and current_option < len(menu_options) - 1:
            current_option += 1  # Move down the list
        elif key == ord('\n'):  # If ENTER is pressed
            stdscr.addstr(len(menu_options) + 1, 0, f"Selected: {menu_options[current_option]}")
            stdscr.refresh()
            stdscr.addstr(len(menu_options) + 2, 0, "Press any key to return to the menu.")
            stdscr.getch()  # Wait for another key press after selection to continue navigating
        elif key == ord('q'):  # Press 'q' to quit
            break

curses.wrapper(navigate_menu)
