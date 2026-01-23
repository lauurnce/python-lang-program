import numpy as np

def solve_linear_transformation():
    # --- Part (a)
    A = np.array([
        [0, -1],
        [1,  0]
    ])
    
    print("--- Part (a) ---")
    print("Matrix of T in standard basis (A):")
    print(A)
    print("\n")

    # --- Part (b)
    v1 = np.array([1, 1])
    v2 = np.array([1, -1])

    P = np.column_stack((v1, v2))
    
    print("Change of Basis Matrix (P):")
    print(P)
    
    P_inv = np.linalg.inv(P)
    
    B = P_inv @ A @ P
    
    print("\n--- Part (b) ---")
    print("Matrix of T with respect to the new basis (B):")
    print(np.round(B, 2)) 
    print("\n")

    # --- Part (c)
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    
    print("--- Part (c) Verification ---")
    print(f"Determinant of A: {det_A:.2f}")
    print(f"Determinant of B: {det_B:.2f}")
    
    if np.isclose(det_A, det_B):
        print("Verdict: The matrices are similar (they represent the same transformation).")
    else:
        print("Verdict: Something went wrong.")

if __name__ == "__main__":
    solve_linear_transformation()