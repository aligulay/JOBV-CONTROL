# Terminal Multiplexer (tmux)

Different workspaces for having different sessions

Tutorial on [`tmux`](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)
More common alternative: [`screen`](http://linuxcommand.org/lc3_adv_termmux.php)

* **Sessions**
A session is an independent workspace with one or more windows

  * `tmux` starts a new session.
  * `tmux new -s NAME` starts it with that name
  * `tmux ls` lists the current sessions
  * `CTRL+b` + `d` detaches the current session

  * `tmux a` attaches the last session.
  Use `-t` flag to specify which session to attach:
  `tmux a -t 0`

* **Windows**
Equivalent to tabs in editors or browsers, they are visually separate parts of the same session.

  * `CTRL+b` + `c` creates a new window
  * `CTRL+d` to close it
  * `CTRL+b` + `N` to go to the N'th window
  * `CTRL+b` + `p` to go the previous window
  * `CTRL+b` + `n` to go the next window
  * `CTRL+b` + `,` to name the current window
  * `CTRL+b` + `w` to list current windows

* **Panes**
Like vim splits, panes let you have multiple shells in the same visual display.
  * `CTRL+b` + `"` to split the current pane horizontally
  * `CTRL+b` + `%` to split the current pane vertically
  * `CTRL+b` + `<direction>` to move to the pane in the specified direction using arrow keys
  * `CTRL+b` + `z` to toggle zoom for the current pane
  * `CTRL+b` + `[` to start scrollback Press `<space>` to start a selection and `<enter>` to copy that selection
  * `CTRL+b` + `<space>` to cycle through pane arrangements