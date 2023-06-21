import builtins
from infra.facelivenessbackend.functions.topology import FaceLivenessFunctionSet
from json import dumps
from infra.interfaces import IRflStack
from constructs import Construct
from aws_cdk import (
  aws_iam as iam,
  aws_apigateway as api,
  aws_ssm as ssm,
)



class FaceLivenessGateway(Construct):
  '''
  Represents the root User Portal using API Gateway Construct.
  '''  
  @property
  def component_name(self)->str:
    return self.__class__.__name__

  def __init__(self, scope: Construct, id: builtins.str, rfl_stack:IRflStack) -> None:
    super().__init__(scope, id)
    
    # Define the gateway...
    self.rest_api = api.RestApi(self,'FaceLiveness',
      rest_api_name='{}-FaceLiveness'.format(rfl_stack.rfl_stack_name),
      description='Gateway for {}'.format(self.component_name))
    
    # Specify the role to use with integrations...
    self.role = iam.Role(self,'Role',
      assumed_by=iam.ServicePrincipal(service='apigateway'),
   )


  def rest_api_url(self):
        return self.rest_api.url
  

  def bind_start_liveness_session(self, functions: FaceLivenessFunctionSet) -> api.ProxyResource:
      """
      Configure the service integration
      :param integration_http_method: The http method 
      """
      self.__bind_lambda_function(
          "createfacelivenesssession", functions.start_liveness_session.function, "GET"
      )

  def bind_liveness_session_result(self, functions: FaceLivenessFunctionSet) -> api.ProxyResource:
      """
      Configure the service integration
      :param integration_http_method: The http method 
      """
      self.__bind_lambda_function(
          "getfacelivenesssessionresults", functions.liveness_session_result.function, "POST"
      )


  def __bind_lambda_function(self,resource_name: str,functions: FaceLivenessFunctionSet,integration_http_method: str,) -> None:
      integration = api.LambdaIntegration(
          functions,
          proxy=False,
          integration_responses=[
              api.IntegrationResponse(
                  status_code="200",
                  response_parameters={
                      "method.response.header.Access-Control-Allow-Origin": "'*'"
                  },
              ),
              api.IntegrationResponse(
                  status_code="500",
                  response_parameters={
                      "method.response.header.Access-Control-Allow-Origin": "'*'"
                  },
              ),
          ],
      )

      """
      Configure the /resource-name...
      """
      resource = self.rest_api.root.add_resource(
          path_part=resource_name,
          default_cors_preflight_options=api.CorsOptions(
              allow_origins=api.Cors.ALL_ORIGINS,
              allow_methods=["OPTIONS", integration_http_method],
          ),
      )

      resource.add_method(
          http_method=integration_http_method,
          integration=integration,
          method_responses=[
              api.MethodResponse(
                  status_code="200",
                  response_parameters={
                      "method.response.header.Access-Control-Allow-Origin": True
                  },
              ),
              api.MethodResponse(
                  status_code="500",
                  response_models={"application/json": api.Model.ERROR_MODEL},
                  response_parameters={
                      "method.response.header.Access-Control-Allow-Origin": True
                  },
              ),
          ],
      )
