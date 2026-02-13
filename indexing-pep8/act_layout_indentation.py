# Apply 79 Characters Limit, Indentation, Wrapping 
# Item 1:
def send_alert(message, user_id, timestamp, urgency_level, device_type, location_data):  
    print("Alert sent!")

# Item 2: 
if score > 50:
 print("You passed!") 
 return True


# Correct
def send_alert(message, user_id, timestamp, 
               urgency_level, device_type, location_data):
    print("Alert sent!")


if score > 50:
    print("You passed!")  # 4 spaces here (Good!)
    return True 