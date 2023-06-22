#!/usr/bin/env python3
from os import environ
from typing import List
import aws_cdk as core
from infra.topologies import DefaultRflStack
import os


def get_environment()->core.Environment:
  '''
  Determines which region and account to deploy into.
  '''
  region = os.environ.get("CDK_DEFAULT_REGION")
  if  region is None:
    region = core.Aws.REGION

  account = os.environ.get('CDK_DEFAULT_ACCOUNT')

  if account is None:
    account = core.Aws.ACCOUNT_ID


  return core.Environment(
    region=region,
    account=account)

class RFLApp(core.App):
  '''
  Represents the root CDK entity.
  '''
  def __init__(self, **kwargs) ->None:
    super().__init__(**kwargs)

    env = get_environment()

    rfl_stack_name = environ.get('RFL_STACK_NAME')
    if rfl_stack_name is None:
      rfl_stack_name = 'Rfl-Prod'
    self.rfl_stack = DefaultRflStack(self,rfl_stack_name, rfl_stack_name=rfl_stack_name, env=env)

app = RFLApp()
assembly = app.synth()

