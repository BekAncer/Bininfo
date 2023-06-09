import fastapi


router = fastapi.APIRouter(
    prefix="/statgov",
    tags=["statgov"],
)


@router.get("/{bin}")
async def get_info_by_biniin(
    biniin: str = fastapi.Path(
        ..., description="БИН/ИИН компании", regex=r"^[\d]{12}$", alias='bin'
    ),
):
    return {
        "bin": biniin
    }

