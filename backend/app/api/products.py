from fastapi import APIRouter

from ..tools.product_tools import get_product_detail, search_products

router = APIRouter()


@router.get("")
def list_products(q: str = ""):
    return search_products(q)


@router.get("/{sku_id}")
def product_detail(sku_id: str):
    return get_product_detail(sku_id)
