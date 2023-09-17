from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.setlist import Setlist
from models.gig import Gig
from models.song import Song
from app import db

setlists_blueprint = Blueprint("setlists", __name__)

@setlists_blueprint.route('/setlists')
def all_setlists():
    setlists_returned = Setlist.query.all()
    return render_template('/setlists/index.jinja', setlists = setlists_returned)
    # return "Setlists page"

@setlists_blueprint.route("/setlists/new", methods=['GET'])
def new_setlist():
    songs = Song.query.all()
    gigs = Gig.query.all()
    return render_template("setlists/new.jinja", songs=songs, gigs=gigs)

@setlists_blueprint.route("/setlists",  methods=['POST'])
def create_setlist():
    song_id = request.form['song_id']
    gig_id = request.form['gig_id']
    setlist = Setlist(song_id=song_id, gig_id=gig_id)
    db.session.add(setlist)
    db.session.commit()
    return redirect('/setlists')

@setlists_blueprint.route("/setlists/<id>/delete", methods=['POST'])
def delete_setlist(id):
    Setlist.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/setlists')