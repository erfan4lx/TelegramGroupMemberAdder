from pyrogram import Client
import time

app = Client('etacobot',1278585,'35e431c13ad73a5acf5912143b873222')

class GroupToGroup_AddMember():

	def __init__(self):
		return None

	def Get_group_chat_id(self,Link):
		global app
		with app as bot:
			self.Group_ChatID = bot.get_chat(Link)
			print("\nThis is the group chatID : {}\n".format(self.Group_ChatID.id))

	def Add_To_Group(self,Source,Destination):
		global app
		with app as bot:
			members = bot.iter_chat_members(Source) 
			for member in members:
				Members_ChatID = member.user.id
				try:
					Adding = bot.add_chat_members(Destination,Members_ChatID)
					print("OK : {}".format(Members_ChatID))
				except:
					print("None"," : {}".format(Members_ChatID))
				time.sleep(30)

while True:
	print("""	\n\tThe application is going to start ...
	for just getting group chatID give me 1
	and for gettin group chatID and use it for
	adding members give me 2 and for exit
	give me 3""")

	To_Do = input("\nSo function 1 or 2 or 3 ? : ")

	if To_Do == "1":
		Invite_Link = input("\nPlease Give me the group invite link = ")
		App_Start = GroupToGroup_AddMember()
		App_Start.Get_group_chat_id(Invite_Link)
		print("\n Successfully Done.")

	elif To_Do == "2":
		SourceGroup_ChatID = int(input("\nPlease give me the source group chatID = "))
		DestinationGroup_ChatID = int(input("\nPlease give me the destination group chatID = "))
		App_Start.Add_To_Group(SourceGroup_ChatID,DestinationGroup_ChatID)
		print("\n Successfully Done.")

	elif To_Do == "3":
		print("\nThanks for using this app ... goodbye\n")
		exit()

	else:
		print("\nPlease give me a correct option.\n")


# print_or_not = input("For print members info give me pyes or pno = ")
# if print_or_not == "pyes":
# global app
# with app as bot:
# 	Members_info = bot.iter_chat_members(-100**********)
# 	for Members_View in Members_info:
# 		Members_ID = Members_View.user.id
# 		Members_Name = Members_View.user.first_name+Members_View.user.last_name
# 		Members_Username = Members_View.user.username
# 		print("\nName : {} --- Username {} --- ID {}\n".format(Members_Name,Members_Username,Members_ID))
# elif print_or_not == "pno":
# 	return None
# else:
# 	print("Give me correct option.")
