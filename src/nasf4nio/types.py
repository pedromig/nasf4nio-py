from abc import ABC
from dataclasses import dataclass
from typing import Optional, TypeVar, Self, Iterable

TBound = TypeVar('TBound')
TObjective = TypeVar('TObjective')

@dataclass(order=True)
class Component(ABC): 
  ...

@dataclass(order=True)
class LocalMove(ABC):
  ...
   
@dataclass 
class Solution(ABC):
  # Iterators
  
  def enum_add_moves(self: Self) -> Iterable[Component]:
    raise NotImplementedError

  def enum_heuristic_add_moves(self: Self) -> Iterable[Component]:
    raise NotImplementedError

  def enum_remove_moves(self: Self) -> Iterable[Component]:
    raise NotImplementedError

  def enum_local_moves(self: Self) -> Iterable[LocalMove]:
    raise NotImplementedError

  def enum_random_local_moves_wor(self: Self) -> Iterable[LocalMove]:
    raise NotImplementedError
 
  # Constructive Moves

  def add(self: Self, component: Component) -> None:
    raise NotImplementedError

  def remove(self: Self, component: Component) -> None:
    raise NotImplementedError

  # Local Moves
  
  def step(self: Self, move: LocalMove) -> None:
    raise NotImplementedError

  def perturb(self: Self) -> None:
    raise NotImplementedError
   
  # Random Moves
  
  def random_add_move(self: Self) -> Component:
    raise NotImplementedError

  def random_remove_move(self: Self) -> Component:
    raise NotImplementedError

  def random_local_move(self: Self) -> LocalMove:
    raise NotImplementedError
  
  # Evaluation

  def objective_increment_local(self: Self, move: LocalMove) -> Optional[TObjective]:
    raise NotImplementedError

  def objective_increment_add(self: Self, component: Component) -> Optional[TObjective]:
    raise NotImplementedError

  def objective_increment_remove(self: Self, component: Component) -> Optional[TObjective]:
    raise NotImplementedError

  def upper_bound_increment_add(self: Self, component: Component) -> Optional[TBound]:
    raise NotImplementedError

  def upper_bound_increment_remove(self: Self, component: Component) -> Optional[TBound]:
    raise NotImplementedError
 
  # Inspection  
  
  def feasible(self: Self) -> bool:
    raise NotImplementedError
   
  def objective_value(self: Self) -> Optional[TObjective]:
    raise NotImplementedError
    
  def upper_bound(self: Self) -> Optional[TBound]:
    raise NotImplementedError
 
  # Util
   
  def copy(self: Self) -> Self:
    raise NotImplementedError

@dataclass
class Problem(ABC):
  def empty_solution(self: Self) -> Solution:
    raise NotImplementedError

  def random_solution(self: Self) -> Solution:
    raise NotImplementedError 
    
  def heuristic_solution(self: Self) -> Solution:
    raise NotImplementedError