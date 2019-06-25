import aiosqlite
setup_sql = """
create table if not exists roles(
    id int,
    guild_id int,
    roles char
);
"""
db_name = 'keeper.db'
add_sql = "insert into roles values(?, ?, ?);"
get_sql = "select * from roles where id = ? and guild_id = ?;"
delete_sql = "delete from roles where id = ? and guild_id = ?;"


async def setup():
    async with aiosqlite.connect(db_name) as db:
        await db.execute(setup_sql)
        await db.commit()


async def add_roles(user_id, guild_id, role_id_list):
    roles = ",".join(str(i) for i in role_id_list)
    async with aiosqlite.connect(db_name) as db:
        await db.execute(add_sql, (user_id, guild_id, roles))
        await db.commit()


async def get_roles(user_id, guild_id):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute(get_sql, (user_id, guild_id)) as cursor:
            row = await cursor.fetchone()
    if not row:
        return False
    await delete_roles(user_id, guild_id)
    return [int(i) for i in row[2]]


async def delete_roles(user_id, guild_id):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(delete_sql, (user_id, guild_id))
        await db.commit()
