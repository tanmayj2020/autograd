import numpy as np
from typing import List 





class Tensor:
    def __init__(self,data:np.ndarray ,requires_grad: bool=False , depends_on:List[Dependency]=None) -> None:
        self.data = data
        self.requires_grad = requires_grad
        self.depends_on = depends_on
        self.shape = data.shape
         




#Depends on is used when say we take two tensors and do their sum to get their new tensor so we can get to know that the sum depends on previosu two tensors
