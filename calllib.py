# library that makes context appropriate calls (Needs organizing and refactoring)

from twilio.rest import Client
from pprint import pprint
from time import sleep

account_sid = 'ACb3dfa6e8ee8a7a8f07c0c184a470b1f4'
auth_token = 'e9c088827db31404cae51182fe4b5999'
client = Client(account_sid, auth_token)

#print(call.sid)
rpt = "Repeating once."
   
def make_call(srvc: str , loc):
    
    #getLoc = loc.geocode
    if srvc == "fire":
        msg = f"There is a fire at {loc}. Requesting the fire department."
    elif srvc == "police":
        msg = f"There is an emergency at {loc}, and the police are needed"
    elif srvc == "emt":
        msg = f"EMT is needed at {loc}. Requesting immediate assistance"
    frmt = f'''
    <Response>
        <Say>Guard dog</Say>
        <Pause length="1"/>
        <Say>{msg}</Say>
        <Pause length="1"/>
        <Say>Again</Say>
        <Pause length="1"/>
        <Say>{msg}</Say>
    </Response>
    '''
    call = client.calls.create(
        twiml=frmt,
        to='+13185572743',
        from_='+19206884198'
    )
    # prints to confirm that the call has been placed
    print(call.sid)
    
make_call("emt", "Louisiana Tech university")