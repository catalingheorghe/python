from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for num, outlook in enumerate(weekly.forecast(), 1):
	print("%d : %s" % (num, outlook))

