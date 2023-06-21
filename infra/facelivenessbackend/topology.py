import builtins

from infra.facelivenessbackend.functions.topology import FaceLivenessFunctionSet
from infra.facelivenessbackend.gateway.topology import FaceLivenessGateway
from json import dumps
from infra.interfaces import IRflStack
from constructs import Construct

class FaceLiveness(Construct):
  def __init__(self, scope: Construct, id: builtins.str, rfl_stack:IRflStack) -> None:
    super().__init__(scope, id)
    
    '''
    Declare the function set that powers the backend
    '''
    self.functions = FaceLivenessFunctionSet(self,'Functions',
      rfl_stack=rfl_stack)

    '''
    Create an Amazon API Gateway 
    '''
    self.api_gateway = FaceLivenessGateway(self,'Gateway', rfl_stack=rfl_stack)

    self.api_gateway.bind_start_liveness_session(self.functions)

    self.api_gateway.bind_liveness_session_result(self.functions)

