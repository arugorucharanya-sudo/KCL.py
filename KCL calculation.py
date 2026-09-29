 Kirchhoff's Current Law (KCL) Calculation

 Input currents entering the junction
I1 = float(input("Enter current I1 entering (A): "))
I2 = float(input("Enter current I2 entering (A): "))

 Input current leaving the junction
I3 = float(input("Enter current I3 leaving (A): "))
I4 = float(input("Enter current I4 leaving (A): "))

 Calculate total entering and leaving currents
total_entering = I1 + I2
total_leaving = I3 + I4

 Calculate KCL error
error = total_entering - total_leaving

Display results
print("\n--- KCL Calculation ---")
print("Total Current Entering =", total_entering, "A")
print("Total Current Leaving  =", total_leaving, "A")
print("KCL Difference =", error, "A")

if abs(error) < 0.000001:
    print("KCL is satisfied.")
else:
    print("KCL is not satisfied.")
