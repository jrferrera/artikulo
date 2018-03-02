from datetime import datetime
from artikulo import db

class BaseModel(object):
  id = db.Column(db.Integer, primary_key = True)
  created_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
  updated_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)

  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()