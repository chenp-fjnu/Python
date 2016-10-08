import time, uuid

from orm import Model, StringField, DateTimeField, TextField, LongTextField, IntegerField, TinyTextField, BigIntField

# def next_id():
#     return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'wp_users'
    id = BigIntField(primary_key=True)
    user_login = StringField(ddl='varchar(20)')
    user_pass = StringField(ddl='varchar(25550)')
    user_nicename = StringField(ddl='varchar(50)')
    user_email = StringField()
    user_url = StringField()
    user_registered = DateTimeField(default=time.time)
    user_activation_key = StringField(ddl='varchar(255)')
    user_status = IntegerField()
    display_name = StringField(ddl='varchar(250)')

class Post(Model):
    __table__ = 'wp_posts'

    id = BigIntField(primary_key=True)
    post_author= BigIntField()
    post_date=DateTimeField()
    post_date_gmt=DateTimeField()
    post_content= LongTextField()
    post_title= TextField()
    post_excerpt= TextField()
    post_status= StringField(ddl='varchar(20)')
    comment_status= StringField(ddl='varchar(20)')
    ping_status= StringField(ddl='varchar(20)')
    post_password= StringField(ddl='varchar(20)')
    post_name= StringField(ddl='varchar(200)')
    to_ping=TextField()
    pinged=TextField()
    post_modified=DateTimeField()
    post_modified_gmt=DateTimeField()
    post_content_filtered=LongTextField()
    post_parent=BigIntField()
    guid=StringField(ddl='varchar(255)')
    menu_order=IntegerField()
    post_type=StringField(ddl='varchar(20)')
    post_minme_type=StringField()
    comment_count=BigIntField()

class Comment(Model):
    __table__ = 'wp_comments'
    comment_id = BigIntField(primary_key=True)
    comment_post_ID = BigIntField()
    comment_author = TinyTextField()
    comment_author_email = StringField()
    comment_author_url = StringField(ddl='varchar(200)')
    comment_author_IP = StringField()
    comment_date = DateTimeField()
    comment_date_gmt = DateTimeField()
    comment_content = TextField()
    comment_karma = IntegerField()
    comment_approved = StringField(ddl='varchar(20)')
    comment_agent = StringField(ddl='varchar(255)')
    comment_type = StringField(ddl='varchar(20)')
    comment_parent = BigIntField()
    user_id = BigIntField()