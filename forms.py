from wtforms import Form, StringField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class Blogform(Form):
    datum = DateField('datum', validators=[DataRequired()])
    titel = StringField('titel', validators=[DataRequired()])
    kategorie = IntegerField('kategorie', validators=[DataRequired()])
    eintrag = TextAreaField('eintrag', validators=[DataRequired()])


class Kategorieform(Form):
    kategorie = StringField('kategorie', validators=[DataRequired()])