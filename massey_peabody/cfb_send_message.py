from twilio.rest import TwilioRestClient


target = open("/Users/creich/practice/mmm/massey_peabody/cfb_flag.txt", "r")

for line in target:
    if "YES" in line:


        client = TwilioRestClient("AC483b03580e667c1c8f45780a5d4e71ba", "1120ffeb5b2ed7a5def26e219afc8e06")

        client.messages.create(to="+18572250054", from_="+18575870687",
               body="Massey-Peabody College FB Rankings are up")

target.close()
