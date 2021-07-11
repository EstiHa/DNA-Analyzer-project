from controller import Controller


class CLI:
    def __init__(self, command_handler):
        self.command_handler=command_handler
        self.exist_DNAs={}

    def run(self):
        while True:
            print("> cmd >>>", end=" ")
            command=input()
            controller.handle_command(command)


if __name__ == '__main__':
    controller=Controller()
    CLI =CLI(controller)
    CLI.run()



