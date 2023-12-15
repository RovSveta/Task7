from icecream import ic

client_res: bool = input("Do you want to reserve?") == "y"

rest_res: list[bool] = [False, True]

for restaurant in rest_res:
	restaurant: bool

	client = int(client_res)
	ic(client_res)
	ic(client)
	rest = int(restaurant)
	ic(restaurant)
	ic(rest)

	ic(f"{client} <= {rest} -> {client <= rest}")
	if client <= rest:
		ic("(true) You are welcome!")
	else:
		ic("(false) We don't handle reservations.")

	input()
