from typing import List

from sqlalchemy import Date, ForeignKeyConstraint, Index, LargeBinary, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
import datetime

class Base(MappedAsDataclass, DeclarativeBase):
    pass


class UserData(Base):
    __tablename__ = 'UserData'
    __table_args__ = (
        Index('id_UNIQUE', 'id', unique=True),
        Index('userMail_UNIQUE', 'userMail', unique=True)
    )

    id: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    userMail: Mapped[str] = mapped_column(String(45))
    Blacklisted: Mapped[int] = mapped_column(TINYINT(4))
    encryptionMethod: Mapped[str] = mapped_column(String(10))

    Certificates: Mapped[List['Certificates']] = relationship('Certificates', back_populates='UserData_')


class Certificates(Base):
    __tablename__ = 'Certificates'
    __table_args__ = (
        ForeignKeyConstraint(['uID'], ['UserData.id'], ondelete='CASCADE', onupdate='CASCADE', name='fk_Certificates_1'),
        Index('fk_Certificates_1_idx', 'uID'),
        Index('id_UNIQUE', 'id', unique=True)
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    uID: Mapped[int] = mapped_column(INTEGER(10))
    CertType: Mapped[str] = mapped_column(String(10))
    CertContent: Mapped[bytes] = mapped_column(LargeBinary)
    CertificateExpire: Mapped[datetime.date] = mapped_column(Date)
    CertDateAdded: Mapped[datetime.date] = mapped_column(Date, server_default=text('current_timestamp()'))

    UserData_: Mapped['UserData'] = relationship('UserData', back_populates='Certificates')
