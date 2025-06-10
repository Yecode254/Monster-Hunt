from sqlalchemy import Table,Column,Integer,Float,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer ,primary_key = True )
    username = Column(String , unique = True , nullable = False )
    email = Column(String, unique = True , nullable = False)
    password = Column(String, nullable= False)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer,primary_key = True)
    username = Column(String, nullable = False)
    level = Column(Integer, default =0)
    exp = Column (Integer)
    money = Column(Float,default= 100.0)
    achievements = relationship("Achievement", secondary="player_achievements")
    

class MonsterSpecies(Base):
    __tablename__ = 'monster_species'
    id = Column(Integer,primary_key = True)
    name = Column (String, nullable = False)
    type = Column(String, nullable=False)  
    base_stats = Column(String)  
    rarity = Column(Float)  
    abilities = Column(String)  

class PlayerMonster(Base):
    __tablename__ = 'player_monsters'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    species_id = Column(Integer, ForeignKey('monster_species.id'))
    level = Column(Integer, default=1)
    current_hp = Column(Integer)
    player = relationship("Player", back_populates="monsters")
    species = relationship("MonsterSpecies")

Player.monsters = relationship("PlayerMonster", back_populates="player")

class MonsterSpecies(Base):
    __tablename__ = 'monster_species'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)  
    base_stats = Column(String)  
    rarity = Column(Float)  
    abilities = Column(String)  # Special monster abilities
# type attributes= Fire, Water, Earth, earth
#base_stats = jsON format storing HP, Attack, Defense
#rarity = Probability of encountering/catching

class PlayerMonster(Base):
    __tablename__ = 'player_monsters'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    species_id = Column(Integer, ForeignKey('monster_species.id'))
    level = Column(Integer, default=1)
    current_hp = Column(Integer)
    player = relationship("Player", back_populates="monsters")
    species = relationship("MonsterSpecies")

Player.monsters = relationship("PlayerMonster", back_populates="player")


class Battle(Base):
    __tablename__ = 'battles'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    winner_id = Column(Integer, ForeignKey('players.id'))
    battle_log = Column(String) 


class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    from_player_id = Column(Integer, ForeignKey('players.id'))
    to_player_id = Column(Integer, ForeignKey('players.id'))
    offered_monsters = Column(String)  
    requested_monsters = Column(String)  
    status = Column(String, default="Pending")  


class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)


class PlayerAchievement(Base):
    __tablename__ = 'player_achievements'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    achievement_id = Column(Integer, ForeignKey('achievements.id'))

if __name__ == '__main__':
    pass
engine= create_engine('sqlite:///Monster_inc.db')
Base.metadata.create_all(engine)
