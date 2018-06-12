def michael_pays(costs):
	# only need to know how much michael will pay
	kate_payment =  costs/3
	michael_payment = (costs - kate_payment)
	if costs < 5:
		print (float("%.2f" % costs) ) # michael pays the full price
	elif kate_payment <= 10:
		temp = costs - kate_payment
		print (float("%.2f" % temp) ) # michael pays the full price
	else:
		temp = costs - 10
		print(float("%.2f" % temp) )

	#print("%.2f" % kate_payment)
	#print("%.2f" % michael_payment)



michael_pays(28.789) # test case


# below is a cleaner and more efficient verison

def michael_pays(cost):
    return round(cost if cost <= 5 else max(cost*2/3, cost-10), 2)

michael_pays(28.789) # testing method