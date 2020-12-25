# JOB CONTROL

**Our Goal**: Learn how to run several processes at the same time while keeping track of them, how to stop or pause a specific process and how to make a process run in the background or foreground.

**Why?** In some cases you will need to interrupt a job while it is executing, for instance if a command is taking too long to complete (such as a `find` with a very large directory structure to search through). Most of the time, you can do `Ctrl+C` and the command will stop. But how does this actually work and why does it sometimes fail to stop the process?

---

Let's start with an example:

1. Run `sleep 20`
2. Use `CTRL+C` to stop it if you do not want to wait for 20 sec.

What happened?

---

Shell uses a UNIX communication mechanism called a [signal](https://en.wikipedia.org/wiki/Signal_(IPC)) to communicate information to the process. When a process receives a signal, it stops its execution, deals with the signal and potentially changes the flow of execution based on the information that the signal delivered. For this reason, signals are software interrupts.

Typing `Ctrl+C` prompts the shell to deliver a `SIGINT` (interrupt) signal to stop execution of the process.

Run `man signal` to see a list of all signals on your local terminal. `kill -l` will do the job on repl.it.

You should see a number (id), name, default action, and description:

```
     No    Name         Default Action       Description
     1     SIGHUP       terminate process    terminal line hangup
     2     SIGINT       terminate process    interrupt program
     3     SIGQUIT      create core image    quit program
     4     SIGILL       create core image    illegal instruction
     5     SIGTRAP      create core image    trace trap
     6     SIGABRT      create core image    abort program (formerly SIGIOT)
     7     SIGEMT       create core image    emulate instruction executed
     8     SIGFPE       create core image    floating-point exception
     9     SIGKILL      terminate process    kill program
     10    SIGBUS       create core image    bus error
     11    SIGSEGV      create core image    segmentation violation
     12    SIGSYS       create core image    non-existent system call invoked
     13    SIGPIPE      terminate process    write on a pipe with no reader
     14    SIGALRM      terminate process    real-time timer expired
     15    SIGTERM      terminate process    software termination signal
     16    SIGURG       discard signal       urgent condition present on socket
     17    SIGSTOP      stop process         stop (cannot be caught or ignored)
     18    SIGTSTP      stop process         stop signal generated from keyboard
     19    SIGCONT      discard signal       continue after stop
     20    SIGCHLD      discard signal       child status has changed
     21    SIGTTIN      stop process         background read attempted from control terminal
     22    SIGTTOU      stop process         background write attempted to control terminal
     23    SIGIO        discard signal       I/O is possible on a descriptor (see fcntl(2))
     24    SIGXCPU      terminate process    cpu time limit exceeded (see setrlimit(2))
     25    SIGXFSZ      terminate process    file size limit exceeded (see setrlimit(2))
     26    SIGVTALRM    terminate process    virtual time alarm (see setitimer(2))
     27    SIGPROF      terminate process    profiling timer alarm (see setitimer(2))
     28    SIGWINCH     discard signal       Window size change
     29    SIGINFO      discard signal       status request from keyboard
     30    SIGUSR1      terminate process    User defined signal 1
     31    SIGUSR2      terminate process    User defined signal 2
```

Useful ones to know:
* `SIGINT` to interrupt execution
* `SIGQUIT` to quit the execution of the program
* `SIGTERM` to terminate process (software termination)
* `SIGHUP` to communicate hang up in the command line (closing terminal when there are processes that are still running)
* `SIGSTOP` and `SIGCONT` to pause and continue execution

---

"sigint.py"

A small Python example that captures `SIGINT` and ignores it, no longer stopping. 
To kill this program, use the `SIGQUIT` signal instead, by typing `Ctrl+\`.

---

Other than killing, we can pause processes using `SIGSTOP`. In the terminal, typing `Ctrl+Z` will prompt the shell to send a `SIGTSTP` signal, short for Terminal Stop (i.e. the terminal's version of `SIGSTOP`):

---

1. Run `sleep 1000` to sleep for a long time.

2. Type `CTRL+Z` to suspend the process by sending a `SIGSTOP` signal, i.e. put it in the background.

---

We can then continue the paused job in the foreground or in the background using `fg` or `bg`, respectively.

`jobs` command lists the unfinished jobs associated with the current terminal session. You can refer to a process using the percent symbol followed by its job number (displayed by jobs), for example `%1` to refer to the job with id 1.

---

3. Run `jobs` to see the list of jobs and their status.

4. Run `bg %1` to continue running the first job (`%1`) in the background. Similarly, `fg` will bring it to the foreground.

5. Look at the jobs again.

---

Appending `&` to the end of a command will run the command in the background, i.e. you can continue using the prompt. It still uses the STDOUT, i.e. it can print things but you can redirect them to a file, for example.

Let's say you have a running program. You can do `Ctrl+Z` to first suspend it and then do `bg` to continue running it in the background. Backgrounded processes are child processes of the same terminal, i.e. they die if you close the terminal because of `SIGHUP` signal. If you do not want that, run the program with `nohup` (a wrapper to ignore `SIGHUP`). 

---

6. Start running the program in the background: `nohup sleep 2000 &`. We still have access to the prompt by using `&` in the end.

7. `kill -STOP %1` to pause the first job. Check the jobs again.

8. What happens when you close the shell? 
Run `kill -HUP %1` to send a hangup signal to the first job. Check jobs again.

9. `kill -HUP %2` will be ignored by the second job because of `nohup`, which means ignore hangup signal, keep running. 

10. `kill %2` or `kill -KILL %2` will kill the job no matter what.

---

**Alternatively**: Terminal multiplexer (the second part)


