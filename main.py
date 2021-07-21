from models import *

result = session.query(User).where(User.id == 3).first()
sent_message = result.sent_message

for m in sent_message:
    print(m.sender_id, m.receiver_id, m.text)