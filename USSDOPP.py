
# import sys
# class Ussd():
#     def __init__(self):
#         self.name = "USSD"
#         print("DATA PLANS")
#         self.main()

#     def daily(self):
#         user = input("Daily Plans \n1.#50 for 40MB \n2.#100 for 100MB \n3.#100 for 350MB(IG/TikTok/Youtube) \n99.Next \n0.Main Menu \n      ")
#         # user = input("Select   ")
#         if user == "1":
#             print("Congratulation. You have successfully purchased 40MB")
#             user = input(" Press A to continue or Z to exit ")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#         elif user == "2":
#             print("Congratulation. You have successfully purchased 100MB")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "z":
#                 sys.exit()
#         elif user == "3":
#             print("Congratulation. You have successfully purchased 350MB(IG/TikTok/Youtube)")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "a":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#         elif user == "99":
#             user = input("5. FREE Youtube \n6.Manage Data \n0.Back  ")
#             if user == "5":
#                 print("You have been give free YouTube Data")
#                 user = input(" Press A to continue or Z to exit")
#                 if user.capitalize() == "A":
#                     self.data_bundles()
#                 elif user.capitalize() == "Z":
#                     sys.exit()
#                 else:
#                     user = input("Try again")
#             elif user == "6":
#                 print("You can Manage your Data here")
#                 user = input(" Press A to continue or Z to exit")
#             if user == "A":
#                 self.main()
#             elif user == "Z":
#                 sys.exit()
#             elif user == "0":
#                 self.daily()
#             else: 
#                 user = input("Invalid try again ")
#         elif user == "0":
#             self.data_bundles()
#         else:
#             print("Invalid input, Try again")
#             self.daily()

#     def weekly(self):
#         user = input("WEEKLY PLANS \n1.#200 for 1GB(IG/TikTok/Youtube) ONLY \n2.#300 for 350MB \n3.#500 for 750MB(2-Week plan) \n4.#500 for 750MB+#500 Talktime (Val/14days) \n99.Next \n0.Back \n00.EXIT \n       ")
#         # user = input("Select   ")
#         if user == "1":
#             print("Congratulation! You have successfully purchased #200 for 1GB(IG/TikTok/Youtube) ONLY")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "2":
#             print("Congratulation! You have successfully purchased #300 for 350MB")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "3":
#             print("Congratulation! You have successfully purchased #500 for 750MB(2-Week plan)")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "4":
#             print("Congratulation! You have successfully purchased #500 for 750MB+#500 Talktime (Val/14days)")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "99":
#             print("5.#1,500 for 6GB \n6.#1,800 for 7GB \n7.#1,000 for 2GB \n8.#500 for 1GB \n0.Back")
#             user = input("Select    ")
#             if user == "5":
#                 print("Congratulation! You have successfully purchased #1,500 for 6GB")
#                 user = input(" Press A to continue or Z to exit")
#                 if user.capitalize() == "A":
#                     self.data_bundles()
#                 elif user.capitalize() == "Z":
#                     sys.exit()
#                 else:
#                     user = input("Try again")
#             elif user == "6":
#                 print("Congratulation! You have successfully purchased #1,800 for 7GB")
#                 user = input(" Press A to continue or Z to exit")
#                 if user.capitalize() == "A":
#                     self.data_bundles()
#                 elif user.capitalize() == "Z":
#                     sys.exit()
#                 else:
#                     user = input("Try again")
#             elif user == "7":
#                 print("Congratulation! You have successfully purchased #1,000 for 2GB")
#                 user = input(" Press A to continue or Z to exit")
#                 if user.capitalize() == "A":
#                     self.data_bundles()
#                 elif user.capitalize() == "Z":
#                     sys.exit()
#                 else:
#                     user = input("Try again")
#             elif user == "8":
#                 print("Congratulation! You have successfully purchased #500 for 1GB")
#                 user = input(" Press A to continue or Z to exit")
#                 if user.capitalize() == "A":
#                     self.data_bundles()
#                 elif user.capitalize() == "Z":
#                     sys.exit()
#                 else:
#                     user = input("Try again")
#             elif user == "0":
#                 self.weekly()
#             else:
#                 user("Invalid Input, Try again  ")
#         elif user == "0":
#             self.data_bundles()
#         elif user == "00":
#                 sys.exit()
#         else:
#             print("Invalid input. Try again")
#             self.weekly()

#     def monthly(self):
#         monthly = {"1":"1. #1000 f0r 1.5GB", "2":"2. #1200 for 2GB", "3":"3. #1500 for 3GB", "99":"99. NEXT", "0":"0. Back", "00":"00.   EXIT" }
#         for x,y in monthly.items():
#             print(y)
#         user = input("Select  ")
#         if user == "1":
#             print("Congratulation! You have successfully purchased #1000 f0r 1.5GB")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "2":
#             print("Congratulation! You have successfully purchased #1200 f0r 2GB")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "3":
#             print("Congratulation! You have successfully purchased #1500 f0r 3GB")
#             user = input(" Press A to continue or Z to exit")
#             if user.capitalize() == "A":
#                 self.data_bundles()
#             elif user.capitalize() == "Z":
#                 sys.exit()
#             else:
#                 user = input("Try again")
#         elif user == "99":
#             print("4. #10,000 for 40GB \n5. #15,000  for 75GB \n0. Back \n00. Main menu")
#             user = input("Select  ")
#             if user == "4":
#                 print("Congratulation! You have successfully purchased #10,000 for 40GB")
#             elif user == "5":
#                 print("Congratulation! You have successfully purchased #15,000  for 75GB")
#             elif user == "0":
#                 self.monthly()
#             else:
#                 user = input("Invalid input, Try again ")
#         elif user == "0":
#                 self.data_bundles()
#         elif user == "00":
#                 sys.exit()
#         else:
#             print("Invalid input, Try again ")
#             self.monthly()


#     def main(self):
#         user = input("Dial USSD code  ")
#         while user != "*121#":
#             user = input("Invalid input, Try again ")
#         self.data_bundles()
        
       
#     def data_bundles(self):
#         print("1.Daily Plan \n2.Weekly Plan \n3.Monthly \n4.EXIST ")
#         user = input("Select    ")
#         user_list = ["1", "2", "3", "4"]
#         while user not in user_list:
#             user = input("Try again ")
#         if user == "1":
#             self.daily()
#         elif user == "2":
#             self.weekly()
#         elif user == "3":
#             self.monthly()
#         elif user == "4":
#             sys.exit()
            

            
# code = Ussd()