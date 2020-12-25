# Aliases

List all the contents in the current directory (`ls`)
  * including hidden files that start with a . (`-a`)
  * using a long listing format (`-l`)
  * printing sizes in human readable format (`-h`)

`ls -lah`

It might be hard to remember long commands. We can use *aliases* to make things easier in these cases.

`alias` is a command to map short sequence of characters to a longer sequence. For example,

`alias ll="ls -lah"`

is going to update the environment to remember the short name `ll` that I gave to the longer command. It can be really handy but remember not to put any spaces in between because `alias` takes only one argument.

`alias gs="git status"` is another useful one. Type this and then check `gs` to see if it gives the same output as `git status`.

If you make certain typos frequently, for example type `sl` instead of `ls`, `alias` is here for you:

`alias sl=ls`

Later, you can check the value of an alias you've already created, for example by typing:

`alias gs` or `alias ll`

If you close the terminal or refresh the page in case of repl.it, all aliases you created will be gone. You don't want to retype them every time.


# Dot Files

Most shells have text-based configuration files called *dot files* because they start with a dot (`.`).

For bash, we have ".bashrc". You can see the content of your ".bashrc" file by typing:

`cat ~/.bashrc` and edit it using vim. It lives in your home directory (`~/`) and it is executed every time you start bash interactively.

Just a reminder:

> bash and sh are two different shells. Basically bash is sh, with more features and better syntax. Most commands work the same, but they are different.Bash (bash) is one of many available (yet the most commonly used) Unix shells. Bash stands for "Bourne Again SHell",and is a replacement/improvement of the original Bourne shell (sh).

> Shell scripting is scripting in any shell, whereas Bash scripting is scripting specifically for Bash. In practice, however, "shell script" and "bash script" are often used interchangeably, unless the shell in question is not Bash.


You can also source it by typing `. ~/.bashrc`. Type it and see what happens. This is what we've been doing with the `$SHELL` command since the beginning! In other words, it is an alias for the `/bin/bash` command. When it is executed, or each time we start bash, the ".bashrc" file in your home directory is executed.

As you can see in your ".bashrc" file, starting in l.90, there are some `ls` aliases that are already defined for you.

You can define more aliases in the file ".bash_aliases". As you can see in l.105, it is sourced in your ".bashrc" file if it exists (`. ~/.bash_aliases`). For example, let's add an alias to it:

`echo alias sl=ls > ~/.bash_aliases`

Then start the bash (`$SHELL`) and check if `sl` works like an `ls` now. 

You can keep modifying it by adding new aliases and they stay (at least until you refresh the page for repl.it but they stay forever in your local machine). For example, add a new alias for `git status` now.

You similarly have dot files for vim, git, etc. to store their configurations. There are many useful configurations to organize dot files. Search for dotfiles on github for some examples. Or here are the ones from the instructors of the Missing Semester:

[Anish](https://github.com/anishathalye/dotfiles), [Jon](https://github.com/jonhoo/configs), [Jose](https://github.com/jjgo/dotfiles)