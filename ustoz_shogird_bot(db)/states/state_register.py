from aiogram.dispatcher.filters.state import State,StatesGroup


class Ustoz(StatesGroup):
    us_surname = State()
    us_yosh = State()
    us_phone = State()
    us_texno = State()
    us_hudut = State()
    us_narx = State()
    us_kasp = State()
    us_murojat = State()
    us_fikr = State()
    admin_yubor = State()

class Shogird(StatesGroup):
    surname = State()
    yosh = State()
    phone = State()
    texnologiya = State()
    hudud = State()
    narx = State()
    kasp = State()
    m_vaqti = State()
    maqsad = State()
    admin_set = State()


class Sherig(StatesGroup):
    sh_name = State()
    sh_yosh = State()
    sh_phone = State()
    sh_texnologiya = State()
    sh_hudud = State()
    sh_narx = State()
    sh_kasp = State()
    sh_m_vaqti = State()
    sh_shmaqsad = State()
    sh_admin_set = State()



class Hodim(StatesGroup):
    h_name = State()
    h_yosh = State()
    h_phone = State()
    h_texnologiya = State()
    h_hudud = State()
    h_narx = State()
    h_kasp = State()
    h_m_vaqti = State()
    h_shmaqsad = State()
    h_admin_set = State()



class Ishchi(StatesGroup):
    i_name = State()
    i_yosh = State()
    i_phone = State()
    i_texnologiya = State()
    i_hudud = State()
    i_narx = State()
    i_kasp = State()
    i_m_vaqti = State()
    i_shmaqsad = State()
    i_admin_set = State()
