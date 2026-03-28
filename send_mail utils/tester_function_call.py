


from send_email import send_email   #makes the function send_email available

health = False   # example

def main():
    if not health:                 #sends email only if False (there is a problem)
        send_email(
            subject="Health Monitor Alert",
            body="AI Assist server is not responding",
            sender="pwilford5@gmail.com",
            receivers=["paul@withleverage.ai"]
        )

if __name__ == "__main__":
    main()
