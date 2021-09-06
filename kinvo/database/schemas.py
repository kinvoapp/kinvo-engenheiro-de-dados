import datetime
import pydantic

from typing import List


MONTHS = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,  'mai': 5,  'jun': 6,
          'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
FULL_MONTHS = {'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
               'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
               'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12}


class EntityCreate(pydantic.BaseModel):
    text: str
    entity: str
    news_id: int


class Entity(pydantic.BaseModel):
    id: int
    text: str
    entity: str

    news_id: int

    class Config:
        orm_mode = True


class NewsBase(pydantic.BaseModel):
    title: str
    link: str
    content: str
    pub_date: datetime.datetime

    @pydantic.validator("pub_date", pre=True)
    def parse_pub_date(cls, value):
        date_info = value.lower().split()

        if date_info.count('de') == 2 or len(date_info) == 3:
            if ',' in date_info[0]:
                value = value.split(',')[1]

            date_info = value.lower().replace('de ', '').split()
            day, month, year = date_info

            month = MONTHS[month] if len(month) == 3 \
                else FULL_MONTHS[month]

            date_iso = f'{year}-{month:02d}-{int(day):02d}'

            return datetime.datetime.strptime(date_iso, '%Y-%m-%d')
        else:
            _, day, month, year, hour_minute_second, offset = date_info

            if offset.lower() == 'gmt':
                offset = '+0000'

            signal = int(offset[0] + '1')
            hours = int(offset[1:3])
            minutes = int(offset[3:5])
            seconds = signal * (hours * 3600 + minutes * 60)
            
            offset = seconds / (3600.0 * 24)

            month = MONTHS[month]

            datetime_iso = (f'{year}-{month:02d}-{int(day):02d}'
                            f'T{hour_minute_second}')
            
            datetime_object = datetime.datetime.\
                strptime(datetime_iso, '%Y-%m-%dT%H:%M:%S')

            return datetime_object - datetime.timedelta(offset)


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
    entities: List[Entity] = []

    class Config:
        orm_mode = True
