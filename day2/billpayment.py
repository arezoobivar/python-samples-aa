
def zakipour_bill_payment_by_card(bid: str, pid: str, pan: str, pin: str):
     if (len(bid) == 0):
          print("please enter billing id")
          return

     print("ha ha ha")

billing_id: str
payment_id: str

billing_id = input("Enter Billing ID")
payment_id = input("Enter Payment ID")

card_pan: str
card_pin: str

card_pan = input("Give me Card PAN")
card_pin = input("Give me Card PIN")

zakipour_bill_payment_by_card(billing_id, payment_id, card_pan, card_pin)



