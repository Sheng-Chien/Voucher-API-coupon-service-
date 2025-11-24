from __future__ import annotations

import enum
from datetime import datetime 

from sqlalchemy import String, DateTime, Boolean, Integer, Numeric, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .extensions import db

class Base(DeclarativeBase):
    """Base model for SQLAlchemy 2.0 style."""

    id:Mapped[int] = mapped_column(primary_key = True,)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )    
    update_at : Mapped[datetime] = mapped_column(

        DateTime, default = datetime.utcnow, onupdate= datetime.utcnow

    )
    
    def to_dict(self, *fields: str) -> dict:
        """
        簡單序列化工具
        這裡有使用到*args(fields)符合題目要求
        """

        data = {}
        if fields: 
            for f in fields:
                data[f] = getattr(self,f)
        
        else:
            for col in self.__table__.columns:
                data[col.name] = getattr(self,col.name)
        return data 
    

class CouponStatus (str, enum.Enum):

    UNUSED = "unused"
    used = "used"
    EXPIRED = "expired"

class Coupon(Base,db.model):
    """
    優惠券資料表。
    依照題目要求包含：
    - 唯一編號 code
    - 名稱 name
    - 價格 price
    - 折扣 discount_percent
    - 有效期 valid_from / valid_to
    - 是否可用 is_active
    - 狀態 status
    """

    __tablename__ = "coupons"

    # 優惠券編號：唯一
    code: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    # 優惠券名稱
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    # 優惠券價格
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    # 折扣百分比
    discount_percent: Mapped[int] = mapped_column(Integer, nullable=False)

    # 有效期起訖
    valid_from: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    valid_to: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # 是否可用
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # 優惠券使用狀態
    status: Mapped[CouponStatus] = mapped_column(
        Enum(CouponStatus),
        default=CouponStatus.UNUSED,
        nullable=False,
    )