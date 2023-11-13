import curses
import time




# Define multiple levels
levels = [
    [
        "***************************************************************************************************",
        "*       *****   *                *                   ***                                          *",
        "*          **             *                         *                  *                          *",
        "*    *     **   *    *       **                             **        *                           *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*    *     **     ****      *** ***             *                             **                  *",
        "*     *******               *          ***                           **                           *",
        "*         **                *                        * *****                *                     *",
        "***       **                ***                      *                                            *",
        "*                            **                    ***                                            *",
        "*    **            **         ***                   **               **                    __QQ   *",
        "*    **                         *                   **                                 ___(_)_ '> *",
        "***************************************************************************************************",
    ],
    [
        "***************************************************************************************************",
        "*       *****   *                *             *     ***                                  *       *",
        "*          **             *                    *    *                  *                  *       *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*    *     **   *    *       **                *             **        *        *                 *",
        "*    *     **     ****      *** ***             *                              **                 *",
        "*     *******               *          ***            ***             **                          *",
        "*         **        *       *     ***          ***   * *****                *                     *",
        "***       **        *       ***                      *                                            *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*          **             *                         *                  *                          *",
        "*                   *        **                    ***                                            *",
        "*    **            **         ***                   **               **                    __QQ   *",
        "*    **                         *                   **                                 ___(_)_ '> *",
        "***************************************************************************************************",
    ],
        [
        "***************************************************************************************************",
        "*       *****   *    *           *                   ***                                          *",
        "*     *******          *    *          ***                           **                           *",
        "*         **       *        *                        * *****                *                     *",
        "*                    *    *                         *                  *                          *",
        "*     *******          *    *          ***                           **                           *",
        "*         **       *        *                        * *****                *                     *",
        "*    *     **   *    *       **                             **        *                           *",
        "*    *     ****** ****      *** ***             *                             **                  *",
        "*     *******          *    *          ***                           **                           *",
        "*         **       *        *                        * *****                *                     *",
        "*     *******          *    *          ***                           **                           *",
        "*         **       *        *                        * *****                *                     *",
        "***       **       *        ***                      *                                            *",
        "*     *******          *    *          ***                           **                           *",
        "*         **       *        *                        * *****                *                     *",
        "*           *      *         **                    ***                                            *",
        "*    **     *      *****      ***                   **               **                    __QQ   *",
        "*    **               *        *                   **                                  ___(_)_ '> *",
        "***************************************************************************************************",
    ],
            [
        "***************************************************************************************************",
        "*       *****   *                      *                   *** **                        **       *",
        "*     *******                *            ***              **     **    **                        *",
        "*     *******               *          ***              **     **    **                           *",
        "*          **             *                 **      *    **                      *          **    *",
        "*     *******               *          ***                        **     **    **                 *",
        "*     *******               *                    ***              **     **    **                 *",
        "*    *     **   *    *                 **                          ** **        *                 *",
        "*    *               **     ****      *** ***             *       **                    **        *",
        "*     ***          ****               *          ***              **     **    **                 *",
        "*     *******                         *          ***              **     **    **                 *",
        "*     *******               *          ***                        **     **    **                 *",
        "*         **                *                                  * *****                *           *",
        "*     *******                         *          ***              **     **    **                 *",
        "*     *******                         *          ***              **     **    **                 *",
        "***       **                          ***          **          *                         **       *",
        "*                            **                    ***       **                        **         *",
        "*     *******               *                    ***              **     **    **                 *",
        "*    **            **         ***               **  **              **         **          __QQ   *",
        "*    **                                   *                   **                       ___(_)_ '> *",
        "***************************************************************************************************",
    ],
]




def main(stdscr):
    # Setup
    curses.start_color()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)    # Non-blocking input
    stdscr.timeout(30)  # Set a timeout for getch()




    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    sh, sw = stdscr.getmaxyx()




    current_level = 0
    maze = levels[current_level]  # Start with the first level




    # Player position
    player_y, player_x = 1, 1




    game_over = False




    while True:
        while not game_over:
            stdscr.clear()




            # Draw the maze
            for y, row in enumerate(maze):
                for x, char in enumerate(row):
                    stdscr.addch(y, x, char, curses.color_pair(1))




            # Draw the player
            stdscr.addch(player_y, player_x, '!')




            # Display the current level
            level_str = f"Level {current_level + 1}"
            stdscr.addstr(0, sw // 3 - len(level_str) // 3, level_str)




            stdscr.refresh()




            key = stdscr.getch()




            if key == ord('q'):
                break  # Quit the game




            new_y, new_x = player_y, player_x




            if key == curses.KEY_UP:
                new_y -= 1
            elif key == curses.KEY_DOWN:
                new_y += 1
            elif key == curses.KEY_LEFT:
                new_x -= 1
            elif key == curses.KEY_RIGHT:
                new_x += 1




            if maze[new_y][new_x] != '*':
                player_y, player_x = new_y, new_x




            if (player_y, player_x) == (len(maze) - 2, len(maze[0]) - 2):
                game_over = True




        # Display a "You won!" message
        stdscr.addstr(sh // 2, sw // 2 - 5, "You won!", curses.A_BOLD)
        stdscr.refresh()




        # Add a pause to display the message
        time.sleep(2)




        current_level += 1




        if current_level < len(levels):
            maze = levels[current_level]
            player_y, player_x = 1, 1
            game_over = False
        else:
            break






    stdscr.refresh()
    stdscr.clear()
    pretty_text = """GAME OVER!"""


    stdscr.addstr(sh // 2, sw // 2 - len(pretty_text) // 2, pretty_text)


    stdscr.refresh()
    time.sleep(10)




curses.wrapper(main)





