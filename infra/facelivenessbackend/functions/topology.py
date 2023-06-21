
from infra.facelivenessbackend.functions.definitions import FaceLivenessStartLivenessSession,FaceLivenessSessionResult
from infra.interfaces import IRflStack
import aws_cdk as core
from constructs import Construct

class FaceLivenessFunctionSet(Construct):
  def __init__(self, scope: Construct, id:str, rfl_stack:IRflStack, **kwargs) -> None:
    super().__init__(scope, id)

    '''
    Define the functions...
    '''
    default_environment_var = {
      'REGION': core.Stack.of(self).region,
      'rfl_stack_NAME': rfl_stack.rfl_stack_name,
    }

    
    self.start_liveness_session = FaceLivenessStartLivenessSession(self,'StartFaceLivenessSession',
      rfl_stack=rfl_stack,  env=default_environment_var)

    self.liveness_session_result = FaceLivenessSessionResult(self,'FaceLivenessSessionResult',
      rfl_stack=rfl_stack, env=default_environment_var)
    
    

    '''
    Grant additional permissions...
    '''




