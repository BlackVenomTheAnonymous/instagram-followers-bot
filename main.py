import config, aux_funcs, json, sys
from LevPasha.InstagramAPI import InstagramAPI

followers = []
followings = []
api = InstagramAPI(config.USERNAME, config.PASSWORD)

def info():
	print("\nI follow them but they dont follow me:\n")
	tot = 0
	for i in followings:
		if i not in followers:
			tot=tot+1
			print(str(tot)+" "+i)		
	print("\nTotal: "+str(tot))

	print("\n\nThey follow me but i dont follow them:\n")
	tot = 0
	for i in followers:
		if i not in followings:
			tot=tot+1
			print(str(tot)+" "+i)	
	print("\nTotal: "+str(tot))

def unfollowNotFollowers():
	for i in followings:
			if i not in followers:
				user_id = aux_funcs.get_id(i)
				print("Unfollowing "+i+"(with id "+user_id+")")
				api.unfollow(user_id)

def unfollowOneFollower(username):
	user_id = aux_funcs.get_id(username)
	api.unfollow(user_id)
	print("Unfollowing "+username+" (with id "+user_id+")")

def followOneFollower(username):
	user_id = aux_funcs.get_id(username)
	api.follow(user_id)
	print("Following "+username+" (with id "+user_id+")")	

def printUsage():
	print("Usage: \npython main.py info - Show report about who doesnt follow you back. \npython main.py unfollow USERNAME - Unfollow a user.")
	print("python main.py follow USERNAME - Follow a user. \npython main.py unfollowAll - Unfollow all the users who dont follow you back")
	return
	
def main():

	if len(sys.argv) == 1:
		printUsage()

	api.login()

	for i in api.getTotalSelfFollowers():
		followers.append(i.get("username") )

	for i in api.getTotalSelfFollowings():
		followings.append(i.get("username") )


	if( sys.argv[1] == "info"):
		info()

	elif( sys.argv[1] == "unfollow"):
		unfollowOneFollower(sys.argv[2])

	elif( sys.argv[1] == "follow"):
		followOneFollower(sys.argv[2])

	elif( sys.argv[1] == "unfollowAll"):
		unfollowNotFollowers()

	else:
		printUsage()

if __name__ == "__main__":
    main()