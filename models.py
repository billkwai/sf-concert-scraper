from app import db

class EventModel(db.Model):
  """
  Event Model
  """

  # table name
  __tablename__ = 'events'

  # composite primary key: (title, venue, date)
  title = db.Column(db.String(), unique=False, nullable=False, primary_key=True)
  venue = db.Column(db.String(), unique=False, nullable=False, primary_key=True)
  url = db.Column(db.String(), unique=False, nullable=True)

  #change to datetime
  date = db.Column(db.Date, unique=False, nullable=False, primary_key=True)

  # time will always be in pacific time because this is for SF venues.
  # Will update if expanding to other regions
  time = db.Column(db.Time(), unique=False, nullable=False)

  # precision(x) scale(y) xxxx.yy
  # No sitatuion where a ticket price should exceed $9999.99
  price = db.Column(db.Integer, unique=False, nullable=False)

  def __init__(self, title, venue, url, date, time, price):
    self.title = title
    self.venue = venue
    self.url = url
    self.date = date
    self.time = time
    self.price = price

  def save(self):
    db.session.add(self)
    db.session.commit(self)

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_events():
    return EventModel.query.all()

  @staticmethod
  def get_venue_events(venue):
    return EventModel.query.filter(self.venue == venue).all()

  def __repr__(self):
    return '<id {title, venue, url, date, time, price}>'.format(title=self.title, venue=self.venue, url=self.url, date=self.date, time=self.time, price=self.price)
