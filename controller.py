import tornado.ioloop
import tornado.web
import sqlite3
import short_url
import os

class MainHandler(tornado.web.RequestHandler):
	def get(self, short=None):
		if not short: 
			cursor.execute("select url,visit_count from domain")
			items=list(cursor.fetchall())
			self.render("index.html",title="Indice",items=items)
		else:
			id=short_url.decode_url(short)
			cursor.execute("select url from domain where rowid=?",[id])
			address=cursor.fetchone()[0]
			cursor.execute("update domain set visit_count=visit_count+1 where rowid=?",[id])
			self.redirect(address,True,301)
		
	def post(self,str):
		url=self.get_body_argument("url")
		if not url.startswith("http://") and not url.startswith("https://"):
			url="http://"+url
		cursor.execute("insert into domain(url,visit_count) values (?,0)",[url])
		cursor.execute("SELECT last_insert_rowid()")
		id1=cursor.fetchone()
		short1 = short_url.encode_url(id1[0])
		self.render("result.html",title="Indice",item=short1)
		
def make_app():
    return tornado.web.Application([(r"/([^/]*)", MainHandler)])	

if __name__ == "__main__":
	db="db_desafio_gupy.db"
	if os.path.isfile(db):
		os.remove(db)
	cursor = sqlite3.connect(db).cursor()
	cursor.execute("""create table domain(url text,visit_count int)""")
	app = make_app()
	app.listen(8080)
	tornado.ioloop.IOLoop.current().start()