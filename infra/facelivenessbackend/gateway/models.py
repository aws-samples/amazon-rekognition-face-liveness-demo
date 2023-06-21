import builtins
from json import dumps
import aws_cdk as core
from constructs import Construct
from aws_cdk import (
  aws_apigateway as api,
)

class GatewayModels(Construct):
  '''
  Represents the UserPortal API Gateway service contracts.
  '''
  def __init__(self, scope: Construct, id: builtins.str, rest_api:api.IRestApi) -> None:
    '''
    Initializes the models for a given API Gateway.
    :param scope: - 
    :param id: -
    :param rest_api: The User Portal API Gateway Construct.
    '''
    super().__init__(scope, id)

    '''
    This online tool was helpful defining the json schema models.
      Note: It is an external resource and has no affiliation with Amazon.
      https://www.liquid-technologies.com/online-json-to-schema-converter
    '''
    self.auth_response_model = api.Model(self,'AuthenticateUserResponse',
      rest_api=rest_api,
      model_name='AuthenticateUserResponse',
      description='Output from the Authentication operation.',
      schema= api.JsonSchema(
        type=api.JsonSchemaType.OBJECT,
        description='The response from a auth user flow.',
        required=[
          'UserId',
          'Status'
        ],
        properties={
          'UserId': api.JsonSchema(
            type=api.JsonSchemaType.STRING,
            description='Primary identifier for the user.'),
          'Status': api.JsonSchema(
            type=api.JsonSchemaType.BOOLEAN,
            description='Outcome of the Authenticate operation.'),
        }))
