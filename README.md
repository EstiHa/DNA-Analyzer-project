# DNA project - design patterns

### The goal of the system is to load, analyze, manipulate and save DNA sequences.

The command line interface allows interaction with the user. Throughout that
interface, the user can enter their input and see the application's output. The prompt
of the CLI is usually > cmd >>>; it might change when special type of input is
required.

There are several groups of commands, which are implemented.

When running the main function, the program creates a new controller object and send it to a new CLI.
The CLI class prints to the 'cmd'/'batch', waits to the input and then send it to the controller.
If the command is not one of few special commands (as explained below) the controllel creates a new command object (of the fit type).
Now - if the CLI mode is cmd- the controller runs the command, by calling to it's perform_action function.
Else - if the mode is batch - push it to the commands list of the batch.

There are some unique commands:
* 'batch' - change the mode to 'batch'. From now and on, the commands would be saved and run immediately.
* 'end' - run out of batch mode, back to the regular, cmd, mode.
* 'run' - run specific batch - few previous commands.

Each DNA sequence is an object of the DNA_sequence class that contains an id, name and the nucleotides sequence.
The existing DNA sequences are saved in two dictionaries:
one - the key is the seq id and the vlue is DNA_sequence object.
and the second - key of the seq name and value of id.
