create table connection (
    cid int primary key,
    user text not null,
    host text not null,
    port int not null,
    is_blocked boolean not null,
    is_muted boolean not null
);

create table message (
    mid int primary key,
    cid int not null,
    time_seen datetime not null,
    content text not null,
    is_received boolean not null
);