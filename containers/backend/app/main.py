from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Dev2Blu Backend",
    version="0.1.0",
    description="Backend de exemplo para orquestração docker-compose."
)


class Pizza(BaseModel):
    name: str
    description: str
    price: float


MENU: List[Pizza] = [
    Pizza(name="Margherita", description="Molho de tomate, mussarela e manjericão", price=39.9),
    Pizza(name="Calabresa", description="Calabresa artesanal com cebola roxa", price=44.9),
    Pizza(name="Quatro Queijos", description="Blend especial de queijos", price=49.9),
]


@app.get("/", response_model=dict)
def read_root() -> dict:
    return {"message": "API da Pizzaria do Adriano", "menu_size": len(MENU)}


@app.get("/menu", response_model=List[Pizza])
def list_menu() -> List[Pizza]:
    return MENU


@app.get("/health", response_model=dict)
def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/order", response_model=dict)
def create_order(pizza: Pizza) -> dict:
    if pizza.name not in {item.name for item in MENU}:
        return {"accepted": False, "reason": "Pizza indisponível"}
    return {"accepted": True, "pizza": pizza.name}
