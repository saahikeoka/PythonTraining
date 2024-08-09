score = int(input("What is the student's score? "))

# if score >= 90:
#     print("The student received an A grade.")
# else:
#     if score >= 80:
#         print("The student received a B grade.")
#     else: 
#         if score >= 70:
#             print("The student received a C grade.")
#         else: 
#             if score >= 60:
#                 print("The student received a D grade.")
#             else:
#                 print("The student received a F grade.")

if score >= 90:
    print("The student received an A grade.")
elif score >= 80:
    print("The student received a B grade.")
elif score >= 70:
    print("The student received a C grade.")
elif score >= 60:
    print("The student received a D grade.")
else:
    print("The student received a F grade.")