from model import db, Person

db.create_all()

man1 = Person("Taro", 18)
man2 = Person("Jiro", 17)
man3 = Person("Saburo", 16)

db.session.add_all([man1, man2])
db.session.add(man3)

db.session.commit()
print(man1, man2, man3)