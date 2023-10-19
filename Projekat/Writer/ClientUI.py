class ClientUI:

    def Options(self):
        print('1. Insert Measurement')
        print('2. Add worker')
        print('3. Manual input')
        print('4. Suspend worker')
        print('5. Close connection')

    def Handle(self, option, send_message):
        _ret_val = True
        if option == '1':
            print("Id: ")
            _id = input()
            print("Mesec: ")
            mesec = input()
            print("Potrosnja:")
            potrosnja = input()

            seq = (_id, mesec, potrosnja)
            msg = " ".join(seq)
            send_message(msg)
        elif option == '2':
            msg = "add"
            send_message(msg)
        elif option == '3':
            print("ID:")
            msg = "Manual"
            msg = msg + ':' + input()
            print("Mesec: ")
            msg = msg + ':' + input()
            print("Potrosnja:")
            msg = msg + ':' + input()
            send_message(msg)
        elif option == '4':
            print("Worker name:")
            msg = "Name "
            msg = msg + input()
            send_message(msg)
        elif option == '5':
            send_message("!DISC")
            _ret_val = False
        return _ret_val
