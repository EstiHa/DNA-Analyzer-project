DNA project

When runnung the main the program creates a new controller object and send it to a new CLI.
The CLI class prints to the 'cnd'/'batch', waits to the input and then send it to the controller.
If the command is not one of few special commands (as explained below) the controllel creates a new command object (of the fit type).
Now - if the CLI mode is cmd- the controller runs the command, by calling to it's perform_action function.
Else - if the mode is batch - push it to the commands list of the batch.
There is some unique command:
batch - change the mode to 'batch' from now on' the commands would be saved and run immediately.
end - run out of batch mode, back tothe regular, cmd, mode.
run - run specific batch - few previous commands.

Each DNA sequence is an object of the DNA_sequence class that contains an id, name and the nucleotides sequence.
The existing DNA sequences are saved in two dictionaries:
one - the key is the seq id and the vlue is DNA_sequence object.
and the second - key of the seq name and value of id.
