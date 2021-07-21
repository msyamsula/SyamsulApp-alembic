from models import *
from sqlalchemy.orm import joinedload

''' 
stage 1
add syamsul, sugih, and yusri
add sugih and yusri to syamsul.folowers
'''
# syamsul = User(
#     username="syamsul",
#     password="password",
#     email="syamsul",
#     is_active=True
# )

# sugih = User(
#     username="sugih",
#     password="password",
#     email="sugih",
#     is_active=True
# )

# yusri = User(
#     username="yusri",
#     password="password",
#     email="yusri",
#     is_active=True
# )

# syamsul.followers.append(yusri)

# syamsul.followers.append(sugih)

# session.add_all([syamsul, sugih, yusri])
# try:
#     session.commit()
# except Exception as e:
#     loggin.warning(e.__str__())
#     session.rollback()


''' 
stage 2
query sugih
print sugih.followings
sugih follow yusri
'''
# sugih = session.query(User).where(User.username=="sugih").first()
# yusri = session.query(User).where(User.username=="yusri").first()

# sugih.followings.append(yusri)

# # session.add_all([syamsul, sugih, yusri])
# try:
#     session.commit()
# except Exception as e:
#     loggin.warning(e.__str__())
#     session.rollback()

''' 
stage 3
delete yusri
expected: user yusri deleted, follower_following contain user_id == yusri deleted
'''

# yusri = session.query(User).where(User.username=="yusri").first()
# session.delete(yusri)

# try:
#     session.commit()
# except Exception as e:
#     loggin.warning(e.__str__())
#     session.rollback()


''' 
stage 4. clean all user
'''

# yusri = session.query(User).where(User.username=="yusri").first()
# syamsul = session.query(User).where(User.username=="syamsul").first()
# sugih = session.query(User).where(User.username=="sugih").first()
# delete_list = [syamsul, sugih, yusri]
# for item in delete_list:
#     if item == None: continue
#     session.delete(item)

# try:
#     session.commit()
# except Exception as e:
#     logging.warning(e.__str__())
#     session.rollback()


''' 
stage 5
send message from syamsul to sugih
'''
# sugih = session.query(User).where(User.username=="sugih").first()
# syamsul = session.query(User).where(User.username=="syamsul").first()
# msg = PrivateMessage(
#     text="halo"
# )
# msg.sender = syamsul
# msg.receiver = sugih

# session.add(msg)

# try:
#     session.commit()
# except Exception as e:
#     logging.warning(e.__str__())
#     session.rollback()


''' 
stage 6
sugih reply to syamsul
check sugih received message
check sugih sent message
check syamsul received message
check syamsul sent message
'''
sugih = session.query(User).where(User.username=="sugih").first()
syamsul = session.query(User).where(User.username=="syamsul").first()

# msg = PrivateMessage(text="damang?")
# msg.sender = sugih
# msg.receiver = syamsul

# session.add(msg)

# msg = PrivateMessage(text="damang ka sorangan?")
# msg.sender = sugih
# msg.receiver = sugih

# session.add(msg)
# try:
#     session.commit()
# except Exception as e:
#     logging.warning(e.__str__())
#     session.rollback()

# sugih_to_syamsul = session.query(
#     PrivateMessage
# ).filter(
#     PrivateMessage.sender_id == sugih.id,
#     PrivateMessage.receiver_id == syamsul.id
# ).all()

# for m in sugih_to_syamsul:
#     m.text = "gelo ngomong sorangan"

# try:
#     session.commit()
# except Exception as e:
#     session.rollback()
#     logging.warning(e.__str__())
