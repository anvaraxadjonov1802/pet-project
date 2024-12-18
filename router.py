from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]

)


@router.post("/creat")
async def create_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id" : task_id}



@router.get("/all")
async def get_all() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
