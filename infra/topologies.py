#!/usr/bin/env python3

from typing import List

from infra.facelivenessbackend.topology import FaceLiveness
from infra.interfaces import IRflStack
import aws_cdk as core
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)



class DefaultRflStack(IRflStack):
  '''
  Represents the simple deployment environment for Rfl.
  '''
  def __init__(self, scope:Construct, id:str, rfl_stack_name:str, **kwargs)->None:
    self.__zone_name = rfl_stack_name
    super().__init__(scope, id, **kwargs)
    
    assert self.rfl_stack_name is not None
    
  
    # Create the FaceLiveness
    faceliveness = FaceLiveness(self,'FaceLiveness', rfl_stack=self)


    #Setup FE

    from infra.frontend.topology import FaceLivenessFrontEnd
    from infra.frontend.topology import TriggerFrontEndBuild
    from infra.frontend.topology import FaceLivenessFrontEndBuildStatus
    from infra.frontend.cognito.topology import FaceLivenessCognito

    # setup Amazon Cognito for Face Liveness

    cognito = FaceLivenessCognito(self,"RflCognito",rfl_stack=self )

    feapp = FaceLivenessFrontEnd(self,"RflWebAPP",rfl_stack=self, apigateway=faceliveness.api_gateway, cognito= cognito)

    triggerfeapp = TriggerFrontEndBuild(self,"RflWebAPPTrigger",rfl_stack=self,amplifyApp=feapp)
    # feapp = RflFrontEnd(self,"RflWebAPP",rfl_stack=self)
    triggerfeapp.node.add_dependency(feapp)
    feappstatus = FaceLivenessFrontEndBuildStatus(self,"RflWebAPPStatus",rfl_stack=self, amplifyApp=feapp , buildTrigger=triggerfeapp)
    feappstatus.node.add_dependency(triggerfeapp)


  @property
  def rfl_stack_name(self)->str:
    return self.__zone_name
