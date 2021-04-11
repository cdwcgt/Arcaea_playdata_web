create table IF NOT EXISTS '[user_id]'
(
songname text not null,
songdiff text,
songrating real,
score int not null,
getptt real,
pure int,
purep int,
far int,
lost int,
time int primary key not null,
userptt real,
score_str text,
time_str text
);
INSERT INTO userinfo (name,id,ptt) VALUES ('[name]','[id]',[ptt]);
update userinfo set name='[name]',id='[id]',ptt=[ptt] where id like '[id]';
INSERT INTO '[user_id]' (songname,songdiff,songrating,score,getptt,pure,purep,far,lost,time,userptt,score_str,time_str)
VALUES ('[songname]','[songdiff]',[songrating],[score],[getptt],[pure],[purep],[far],[lost],[time],[userptt],'[score_str]','[time_str]');
