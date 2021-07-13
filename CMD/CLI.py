from controller import Controller


class CLI:
    def __init__(self, controller):
        self.controller=controller
        self.exist_DNAs={}

    def run(self):
        while True:
            if controller.mode=='cmd':
                print("> cmd >>>", end=" ")
            else:
                print("> batch >>>", end=" ")
            command=input()
            self.controller.handle_command(command)

if __name__ == '__main__':
    controller=Controller()
    CLI =CLI(controller)
    CLI.run()