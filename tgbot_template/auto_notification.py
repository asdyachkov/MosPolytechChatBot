import schedule

def notificate():
    with open("subscription.json", "r") as file:


schedule.every().day.at('8.45', '10.25', '12.05', '14.15', '15.55', '17.35', '19.15').do(notificate)