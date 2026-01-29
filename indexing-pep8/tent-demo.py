# ==========================================
# PART 1: INDEXING & SLICING (The Surgical Knife)
# Speaker: Joshua
# ==========================================

drone_data = ["Drone-X1", "Manila_Sector_4", 85, "Active", "2026-02-02"]

print("Full Data Stream:", drone_data)

drone_id = drone_data[0]
print(f"Drone ID: {drone_id}")

timestamp = drone_data[-1]
print(f"Timestamp: {timestamp}")

core_status = drone_data[1:3] 
print(f"Core Status: {core_status}")


quick_check = drone_data[0::2]
print(f"Quick Scan: {quick_check}")

# ==========================================
# PART 2: PEP 8 (The Professional Standard)
# Speaker: 
# ==========================================

def calculate_accuracy(  predictions,targets):x=0;y=len(predictions)
  for i in range(y):
     if predictions[i]==targets[i]:x+=1
  return x/y

def calculate_model_accuracy(predictions, targets):
    """
    Calculates the accuracy of the model predictions.
    """
    correct_predictions = 0
    total_samples = len(predictions)

    for i in range(total_samples):
        if predictions[i] == targets[i]:
            correct_predictions += 1
            
    return correct_predictions / total_samples