from typing import Mapping
from infra.default_lambda import DefaultFunction
from infra.interfaces import IRflStack
import aws_cdk as core
from constructs import Construct
from aws_cdk import (
  aws_iam as iam,
)

class FaceLivenessBackendFunction(DefaultFunction):
  '''
  Represents the base template for a UserPortal Lambda function.
  ''' 
  @property
  def component_name(self)->str:
    return self.__class__.__name__

  @property
  def function_name(self) -> str:
    return '{}-UserPortal-{}'.format(
        self.rfl_stack.rfl_stack_name,
        self.component_name)

  @property
  def function_timeout(self)->core.Duration:
    return core.Duration.seconds(30)
  
  def __init__(self, scope: Construct, id: str, rfl_stack:IRflStack,env:Mapping[str,str]={}, **kwargs) -> None:
    super().__init__(scope, id, rfl_stack=rfl_stack, env=env, **kwargs)

    '''
    Attach any shared Amazon IAM policies here.
    '''
    self.function.role.add_managed_policy(
      policy=iam.ManagedPolicy.from_aws_managed_policy_name('AmazonRekognitionFullAccess'))

  



class FaceLivenessStartLivenessSession(FaceLivenessBackendFunction):
  def __init__(self, scope: Construct, id:str, rfl_stack:IRflStack,env:Mapping[str,str]={}, **kwargs) -> None:
    super().__init__(scope, id, rfl_stack=rfl_stack, env=env)

  @property
  def source_directory(self)->str:
    return 'src/backend/start-liveness-session'

  @property
  def component_name(self)->str:
    return 'FaceLivenessStartLivenessSession'

class FaceLivenessSessionResult(FaceLivenessBackendFunction):
  def __init__(self, scope: Construct, id:str, rfl_stack:IRflStack,env:Mapping[str,str]={}, **kwargs) -> None:
    super().__init__(scope, id, rfl_stack=rfl_stack, env=env)

  @property
  def source_directory(self)->str:
    return 'src/backend/liveness-session-result'

  @property
  def component_name(self)->str:
    return 'FaceLivenessSessionResult'

