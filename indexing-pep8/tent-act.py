
corrupted_signal = "W##e## ##a##r##e## ##D##A##I##!"

decoded_message = corrupted_signal[::3]  # need to write this line
print("Decrypted Message:", decoded_message)


def showmessage(msg):print("Incoming Transmission: "+msg)



def show_message(msg):
    print("Incoming Transmission: " + msg)

# Test the work:
show_message(decoded_message)