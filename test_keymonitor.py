import utilitySuite as utilsuite
km = utilsuite.keyMonitor()
print(f"Type any number key to change km.option()")
while True:
    print(f"Current km.option: {km.option()}")