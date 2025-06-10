from sqlalchemy import Table,Column,Integer,Float,String,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer,primary_key = True)
    username = Column(String, nullable = False)
    level = Column(Integer, default =0)
    exp = Column (Integer)
    money = Column(Float,default= 100.0)
    achievements = relationship("Achievement", secondary="player_achievements")




if __name__ == '__main__':
    pass
engine= create_engine('sqlite:///Monster_inc.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
