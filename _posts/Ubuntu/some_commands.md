# Some interesting command in ubuntu
## Control operators

### List terminators

- `;`  : Will run one command after another has finished, irrespective of the outcome of the first.

    ```bash
    command1 ; command2
    ```
    First *command1* is run, in the foreground, and once it has finished, *command2* will be run.

    A newline that isn't in a string literal or after certain keywords is not equivalent to the semicolon operator. A list of ; delimited simple commands is still a list - as in the shell's parser must still continue to read in the simple commands that follow a ; delimited simple command before executing, whereas a newline can delimit an entire command list - or list of lists. The difference is subtle, but complicated: given the shell has no previous imperative for reading in data following a newline, the newline marks a point where the shell can begin to evaluate the simple commands it has already read in, whereas a ; semi-colon does not.

- `&` : This will run a command in the background, allowing you to continue working in the same shell.

    ```bash
    command1 & command2
    ```
    Here, command1 is launched in the background and command2 starts running in the foreground immediately, without waiting for command1 to exit.

    A newline after command1 is optional.

### Logical operators
- `&&` : Used to build AND lists, it allows you to run one command only if another exited successfully.

    ```bash
    command1 && command2
    ```
    Here, *command2* will run after *command1* has finished and only if *command1* was successful (if its exit code was 0). Both commands are run in the foreground.

    This command can also be written:
    ```bash
    if command1
    then command2
    else false
    fi
    ```
    Or simply like below if the return status is ignored: 
    ```bash
    if command1; 
    then command2; 
    fi 
    ```

- `||` : Used to build OR lists, it allows you to run one command only if another exited unsuccessfully.

    ```bash
    command1 || command2
    ```
    Here, *command2* will only run if *command1* failed (if it returned an exit status other than 0). Both commands are run in the foreground.

    This command can also be written

    ```bash
    if command1
    then true
    else command2
    fi
    or in a shorter way if ! command1; then command2; fi.
    ```

**Note**:  && and || are left-associative

- `!`: This is a reserved word which acts as the “not” operator (but must have a delimiter), used to negate the return status of a command — return 0 if the command returns a nonzero status, return 1 if it returns the status 0. Also a logical NOT for the test utility.

    ```bash
    ! command1
    [ ! a = a ]
    ```
    And a true NOT operator inside Arithmetic Expressions:
    ```bash
    $ echo $((!0)) $((!23))
    1 0
    ```

### Pipe operator
- `|` : The pipe operator, it passes the output of one command as input to another. A command built from the pipe operator is called a pipeline.

    ```bash
    command1 | command2
    ```

    Any output printed by *command1* is passed as input to *command2*.

- `|&` : This is a shorthand for 2>&1 | in bash and zsh. It passes both standard output and standard error of one command as input to another.
    ```bash
    command1 |& command2
    ```


## Redirection Operators
In the shell command language, a token that performs a redirection function. It is one of the following symbols:

```
<     >     >|     <<     >>     <&     >&     <<-     <>
```

- `<` : Gives input to a command.

    ```bash
    command < file.txt
    ```
    The above will execute command on the contents of file.txt.

- `<>` : same as above, but the file is open in read+write mode instead of read-only:

    ```bash
    command <> file.txt
    ```
    If the file doesn't exist, it will be created.

    That operator is rarely used because commands generally only read from their stdin

- `>` : Directs the output of a command into a file.

    ```bash
    command > out.txt
    ```

    The above will save the output of *command* as out.txt. If the file exists, its contents will be overwritten and if it does not exist it will be created.

    This operator is also often used to choose whether something should be printed to standard error or standard output:

    ```bash
    command >out.txt 2>error.txt
    ```

    In the example above, `>` will redirect standard output and `2>` redirects standard error. Output can also be redirected using `1>` but, since this is the default, the `1` is usually omitted and it's written simply as `>.`

    So, to run command on *file.txt* and save its output in *out.txt* and any error messages in *error.txt* you would run:

    ```bash
    command < file.txt > out.txt 2> error.txt
    ```
- `>|` : Does the same as `>`, but will overwrite the target, even if the shell has been configured to refuse overwriting (with set -C or set -o noclobber).

    ```bash 
    command >| out.txt
    ```
    If *out.txt* exists, the output of command will replace its content. If it does not exist it will be created.

- `>>` : Does the same as `>`, except that if the target file exists, the new data are appended.

    ```bash
    command >> out.txt
    ```
    If out.txt exists, the output of *command* will be appended to it, after whatever is already in it. If it does not exist it will be created.

