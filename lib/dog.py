from models import Dog


def create_table(base,engine):
    pass
    base.metadata.create_all(engine)
   

def save(session, dog):
    pass
    session.add(dog)
    session.commit()

def get_all(session):
    pass
    return session.query(Dog).all()

def find_by_name(session, name):
    pass
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    pass
    return session.query(Dog).filter_by(id=id).first()


def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def update_breed(session, dog, breed):
    pass
    dog.breed = breed
    session.commit()