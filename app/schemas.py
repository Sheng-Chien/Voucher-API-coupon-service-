from datetime import datetime
from apiflask import Schema
from apiflask.fields import Integer, String, Boolean, DateTime, Float
from apiflask.validators import Range, Length, OneOf
from .models import CouponStatus


class CouponCreateSchema(Schema):
    """建立優惠券 API 的輸入驗證 Schema"""

    code = String(required=True, validate=Length(max=64))
    name = String(required=True, validate=Length(max=128))

    price = Float(required=True, validate=Range(min=0))
    discount_percent = Integer(required=True, validate=Range(min=0, max=100))

    valid_from = DateTime(required=False)
    valid_to = DateTime(required=False)

    is_active = Boolean(required=False, load_default=True)

    # 狀態可不傳，預設 unused
    status = String(
        required=False,
        validate=OneOf([s.value for s in CouponStatus]),
        load_default=CouponStatus.UNUSED.value,
    )


class CouponUpdateSchema(Schema):
    """
    PATCH/PUT 更新優惠券資料的 Schema。
    全部非必填，因為是部分更新。
    """

    name = String(validate=Length(max=128))
    price = Float(validate=Range(min=0))
    discount_percent = Integer(validate=Range(min=0, max=100))
    valid_from = DateTime(required=False)
    valid_to = DateTime(required=False)
    is_active = Boolean(required=False)
    status = String(validate=OneOf([s.value for s in CouponStatus]))


class CouponOutSchema(Schema):
    """API 輸出格式"""

    id = Integer()
    code = String()
    name = String()
    price = Float()
    discount_percent = Integer()

    valid_from = DateTime(allow_none=True)
    valid_to = DateTime(allow_none=True)

    is_active = Boolean()
    status = String()

    created_at = DateTime()
    updated_at = DateTime()


class CouponQuerySchema(Schema):
    """GET /coupons 查詢條件 Schema"""

    code = String()
    name = String()
    min_price = Float()
    max_price = Float()
    status = String(validate=OneOf([s.value for s in CouponStatus]))
    is_active = Boolean()
